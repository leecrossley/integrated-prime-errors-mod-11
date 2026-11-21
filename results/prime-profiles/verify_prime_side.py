"""Compare the reflected Riesz formulas with a certified zero sum, then scan a prime.

Run with Python and python-flint 0.9.0. The modulus-11 comparison uses the
published v2.0.0 zero-brackets.json from integrated-prime-errors-mod-11.
All sign decisions and numerical identities use outward-rounded balls.
"""
import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path

from flint import acb, acb_series, arb, ctx, dirichlet_char, fmpz


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def constants(q):
    """Return (finite part at 1, value at 2) of the character-weighted D_b."""
    h = q - 1
    factors = [int(prime) for prime, _ in fmpz(h).factor()]
    g = next(g for g in range(2, q) if all(pow(g, h // p, q) != 1 for p in factors))
    residues = [pow(g, j, q) for j in range(h)]
    at_one, at_two = acb_series([1, 1], 2), acb_series([2, 1], 2)
    one = [at_one.zeta(acb(r) / q, deflate=True) for r in residues]
    two = [at_two.zeta(acb(r) / q) for r in residues]
    logq = arb(q).log()

    def derivatives(jets, principal):
        values = acb.dft([jet[0] for jet in jets])
        slopes = acb.dft([jet[1] for jet in jets])
        individual = [principal]
        for k in range(1, h):
            require(values[k].abs_lower() > 0, "nonprincipal denominator unresolved")
            individual.append(logq - slopes[k] / values[k])
        transforms = acb.dft(individual, inverse=True)
        real_values = {}
        for r, z in zip(residues, transforms):
            require(z.imag.contains(0), "character transform should be real")
            real_values[r] = h * z.real
        return real_values

    zeta = at_two.zeta()
    return derivatives(one, -acb(arb.const_euler())), derivatives(two, -zeta[1] / zeta[0])


def prime_powers(bound):
    prime = bytearray([1]) * (bound + 1)
    prime[:2] = bytes(2)
    for p in range(2, isqrt(bound) + 1):
        if prime[p]:
            prime[p*p::p] = bytes((bound - p*p) // p + 1)
    higher = {}
    for p in range(2, isqrt(bound) + 1):
        if prime[p]:
            n = p*p
            while n <= bound:
                higher[n] = p
                n *= p
    for n in range(2, bound + 1):
        if prime[n]:
            yield n, n
        elif n in higher:
            yield n, higher[n]


def profiles(q, c, d, scales, classes):
    """At y=e^|u|, yield both profile values, retaining each ramified term."""
    logq = arb(q).log()
    powers = iter(prime_powers(max(scales)))
    term = next(powers, None)
    # Index zero holds the common contribution at q, q^2, ...
    mass, linear, inverse, square = ([arb(0) for _ in range(q)] for _ in range(4))
    inverse_class = {a: pow(a, -1, q) for a in classes}
    bias = {a: arb(4) / 3 if pow(a, (q-1)//2, q) == 1 else arb(0) for a in classes}
    for y in scales:
        while term is not None and term[0] <= y:
            n, p = term
            a = n % q
            weight = arb(p).log() * (q-1 if a else 1)
            mass[a] += weight
            linear[a] += weight * n
            inverse[a] += weight / n
            square[a] += weight / (n*n)
            term = next(powers, None)
        x = arb(y)
        root, logx = x.sqrt(), x.log()
        for a in classes:
            b = inverse_class[a]
            forward = (mass[a] + mass[0] - (linear[a] + linear[0]) / x - x/2
                       + 1 + logq - logx + c[b] - (logq + d[b])/x) / root - bias[a]
            backward = (root * (1 + logx + c[b] - inverse[b] - inverse[0]
                                 + x*(square[b] + square[0] - d[b]))
                        - 1/(2*root) - bias[a])
            yield y, a, forward, backward


def check_mod_11(brackets):
    q = 11
    c, d = constants(q)
    classes = list(range(2, 10))
    first, second = acb_series([1, 1], 2), acb_series([2, 1], 2)
    direct = []
    zeros = []
    data = json.loads(brackets.read_bytes())
    certificate = {key: data[key] for key in ("denominator", "height", "lower_numerators")}
    encoded = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode("ascii")
    require(hashlib.sha256(encoded).hexdigest() ==
            "9e5ad2be261cacacef761b8dfe830e18c9ac3237673da302b790d292f7a448e1",
            "expected the published modulus-11 brackets")
    den = data["denominator"]
    for label in range(1, q):
        chi = dirichlet_char(q, label)
        second_value = second.zeta() if label == 1 else second.dirichlet_l(chi)
        if label == 1:
            first_value = -acb(arb.const_euler())
        else:
            first_jet = first.dirichlet_l(chi)
            first_value = -first_jet[1]/first_jet[0]
        direct.append((chi, first_value, -second_value[1]/second_value[0]))
        char_zeros = []
        for n in data["lower_numerators"][str(label)]:
            gamma = arb(2*n+1, 1) / (2*den)
            rho = acb(arb(1)/2, gamma)
            char_zeros.append((gamma, -2/(rho*(rho+1))))
        zeros.append((chi, char_zeros))
    for b in range(1, q):
        for j, computed in ((1, c[b]), (2, d[b])):
            reference = sum(row[0](b).conjugate()*row[j] for row in direct)
            require(reference.real.overlaps(computed) and reference.imag.contains(0),
                    "Hurwitz and individual-character constants disagree")
    scales = [1, 2, 3, 5, 8, 11, 31, 121, 997, 21000]
    spectral = {}
    for y in scales:
        for sign in (1, -1):
            logx = sign * arb(y).log()
            partials = []
            for chi, char_zeros in zeros:
                subtotal = sum(coeff*acb(0, gamma*logx).exp() for gamma, coeff in char_zeros)
                partials.append((chi, subtotal))
            for a in classes:
                bias = -arb(4)/3 if pow(a, 5, 11) == 1 else arb(0)
                spectral[y, a, sign] = bias + sum((chi(a).conjugate()*z).real for chi, z in partials)
    for y, a, forward, backward in profiles(q, c, d, scales, classes):
        for sign, value in ((1, forward), (-1, backward)):
            require(abs(value-spectral[y, a, sign]) < arb(154)/1000,
                    f"outside the certified zero-sum tail at y={y}, a={a}, sign={sign}")
    return {"modulus": q, "constant_checks": 20, "spectral_comparisons": len(spectral),
            "brackets": sum(len(z) for _, z in zeros), "absolute_tail_bound": "0.154"}


def scan(q, limit):
    require(fmpz(q).is_prime() and q >= 11 and limit >= 2, "expected a prime and a positive bound")
    c, d = constants(q)
    classes = list(range(2, q-1))
    positive, negative = {}, {}
    scales = [1]
    while scales[-1] < limit:
        scales.append(min(limit, max(scales[-1]+1, (5*scales[-1])//4)))
    for y, a, forward, backward in profiles(q, c, d, scales, classes):
        for sign, value in ((1, forward), (-1, backward)):
            if a not in positive and value > 0:
                positive[a] = sign*y
            if a not in negative and value < 0:
                negative[a] = sign*y
    both = positive.keys() & negative.keys()
    return {"prime": q, "first_scale": scales[0], "last_scale": scales[-1], "scale_count": len(scales),
            "classes_tested": len(classes), "classes_excluded_by_formula": [1, q-1],
            "positive": len(positive), "negative": len(negative), "both": len(both),
            "missing_positive": sorted(set(classes)-positive.keys()),
            "missing_negative": sorted(set(classes)-negative.keys()),
            "positive_witness": positive, "negative_witness": negative}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brackets", type=Path, required=True)
    parser.add_argument("--prime", type=int, default=10009)
    parser.add_argument("--limit", type=int, default=2_000_000)
    parser.add_argument("--bits", type=int, default=128)
    parser.add_argument("--output", type=Path, required=True)
    opts = parser.parse_args()
    require(opts.bits >= 96, "use at least 96 bits")
    ctx.prec, ctx.cap = opts.bits, 2
    replay = check_mod_11(opts.brackets)
    print(json.dumps(replay), flush=True)
    result = scan(opts.prime, opts.limit)
    summary = {key: val for key, val in result.items() if not key.startswith(("missing_", "positive_", "negative_"))}
    print(json.dumps(summary), flush=True)
    opts.output.write_text(json.dumps({"bits": opts.bits, "mod_11": replay, "scan": result},
                                      separators=(",", ":")) + "\n")


if __name__ == "__main__":
    main()
