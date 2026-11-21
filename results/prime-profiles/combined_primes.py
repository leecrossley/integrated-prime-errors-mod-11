"""Certify strict profile signs on contiguous real intervals using all prime powers.

Requires python-flint 0.9.0 and verify_prime_side.py. The input names the first
grid's unresolved classes or is the JSON output of an earlier continuous scan.
Binary floating point only proposes a rational evaluation point. An Arb value
at that point proves positivity, or its tangent bounds the entire interval.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpz

from verify_prime_side import constants, prime_powers


def sieve_data(q, limit):
    primes = [n for n, p in prime_powers(math.isqrt(limit)) if n == p]
    sieve = [(p, pow(q, -1, p)) for p in primes if p != q]
    higher = {}
    for p in primes:
        n = p * p
        while n <= limit:
            higher.setdefault(n % q, []).append((n, p))
            n *= p
    common = [(q, q)] if q <= limit else []
    common += higher.get(0, [])
    return sieve, higher, common


def progression(q, a, limit, data, first=1):
    sieve, higher, common = data
    offset = max(0, (first-a+q-1)//q)
    initial = a+offset*q
    count = (limit-initial)//q + 1
    candidates = bytearray([1]) * max(count, 0)
    for p, inv in sieve:
        if p*p > limit:
            break
        t = (-initial*inv) % p
        start = max(0, (p*p-initial+q-1)//q)
        if t < start:
            t += ((start-t+p-1)//p)*p
        if t < count:
            candidates[t::p] = bytes((count-1-t)//p+1)
    terms = [(initial+t*q, initial+t*q) for t, hit in enumerate(candidates) if hit and initial+t*q >= 2]
    extra = [t for t in higher.get(a, []) + common if first <= t[0] <= limit]
    return sorted(terms + extra)


def event_stream(q, a, limit, data):
    # Bound live memory even when searching at a trillion or more.
    span = 250_000*q
    for first in range(1, limit+1, span):
        yield from progression(q, a, min(first+span-1, limit), data, first)
    yield limit, 0


def candidate(left, right, slope):
    if slope(left) <= 0:
        return float(left)
    if slope(right) >= 0:
        return float(right)
    lo, hi = float(left), float(right)
    for _ in range(48):
        mid = (lo+hi)/2
        if slope(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def segment(left, right, mass, moment, logq, c, d, bias, forward):
    if forward:
        linear = mass+logq+c
        offset = moment+logq+d
        alpha, beta = float(linear), 1.5*float(bias)
        z = candidate(left, right, lambda t: alpha-math.log(t)-t-beta*math.sqrt(t))
    else:
        linear = moment-d
        alpha, beta = float(linear), float(bias)/2
        z = candidate(left, right, lambda t: alpha+1/t+0.5/t**2+beta/(t*math.sqrt(t)))
    numerator, denominator = z.as_integer_ratio()
    y = arb(numerator)/denominator
    root, ell = y.sqrt(), y.log()
    if forward:
        value = y*(linear+1-ell-y/2-bias*root)-offset
        grad = linear-ell-y-3*bias*root/2
    else:
        value = 1+ell+c-mass+y*linear-1/(2*y)-bias/root
        grad = linear+1/y+1/(2*y*y)+bias/(2*y*root)
    if value > 0:
        profile = value/(y*root) if forward else value*root
        return {"numerator": numerator, "denominator": denominator,
                "direction": "forward" if forward else "reflected",
                "profile": profile.str(16)}
    if value+grad*(left-y) < 0 and value+grad*(right-y) < 0:
        return None
    raise ArithmeticError(f"tangent did not certify a strict sign on [{left},{right}]")


def examine(q, a, limit, data, c, d):
    b = pow(a, -1, q)
    logq = arb(q).log()
    bias = arb(4)/3 if pow(a, (q-1)//2, q) == 1 else arb(0)
    count = 0
    for forward, residue in ((True, a), (False, b)):
        lo, mass, moment = 1, arb(0), arb(0)
        for hi, p in event_stream(q, residue, limit, data):
            if hi > lo:
                count += 1
                hit = segment(lo, hi, mass, moment, logq, c[b], d[b], bias, forward)
                if hit is not None:
                    return hit, count
            if p:
                weight = logq if hi % q == 0 else (q-1)*arb(p).log()
                if forward:
                    mass += weight
                    moment += hi*weight
                else:
                    mass += weight/hi
                    moment += weight/(hi*hi)
            lo = hi
    return None, count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--limit", type=int, default=2_000_000)
    parser.add_argument("--bits", type=int, default=128)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    inp = json.loads(raw)
    if "scan" in inp:
        q, classes = inp["scan"]["prime"], inp["scan"]["missing_positive"]
    else:
        q, classes = inp["prime"], inp["negative_throughout"]
    if not (fmpz(q).is_prime() and q >= 11 and args.bits >= 96 and 1 < args.limit < 2**52):
        raise ValueError("invalid verification parameters")
    if len(set(classes)) != len(classes) or not all(1 < a < q-1 for a in classes):
        raise ValueError("expected distinct nonexceptional classes")
    ctx.prec, ctx.cap = args.bits, 2
    c, d = constants(q)
    data = sieve_data(q, args.limit)
    # Compare the progression sieve with the separately implemented global sieve.
    stop = min(200_000, args.limit)
    check_data = sieve_data(q, stop)
    reference = list(prime_powers(stop))
    for a in sorted(set(classes[:5]) | {pow(a, -1, q) for a in classes[:5]}):
        if progression(q, a, stop, check_data) != [t for t in reference if t[0] % q in (0, a)]:
            raise ArithmeticError(f"sieves disagree at {q}, {a}")
    positive, negative, pieces = {}, [], 0
    for a in classes:
        hit, tested = examine(q, a, args.limit, data, c, d)
        pieces += tested
        if hit is None:
            negative.append(a)
        else:
            positive[a] = hit
    result = {"prime": q, "limit": args.limit, "bits": args.bits,
              "input_sha256": hashlib.sha256(raw).hexdigest(), "intervals_checked": pieces,
              "classes_tested": len(classes), "positive": positive, "negative_throughout": negative}
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"q={q}, y<= {args.limit}, bits={args.bits}, classes tested={len(classes)}, "
          f"positive={len(positive)}, strictly negative in both directions throughout={len(negative)}, "
          f"intervals checked={pieces}", flush=True)


if __name__ == "__main__":
    main()
