"""Verify the bounded-height certificates for integrated prime-counting errors.

The prime 11 has its own two verifiers in the parent directory. This program
checks the additional primes, the trigonometric amplitude, and the numerical
constant in the separate, conditional large-prime criterion.
"""
import argparse
import csv
from itertools import product
from math import isqrt
from pathlib import Path

from flint import acb, arb, ctx, dirichlet_char


DENOMINATOR = 2**44
FIRST_PRIME = 13
LAST_PRIME = 10_007


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def primes_up_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit-p*p)//p + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def primitive_root(p):
    factors = set()
    remaining = p-1
    for divisor in range(2, isqrt(p-1) + 1):
        if remaining % divisor == 0:
            factors.add(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
    if remaining > 1:
        factors.add(remaining)
    return next(g for g in range(2, p)
                if all(pow(g, (p-1)//d, p) != 1 for d in factors))


def read_certificates():
    data = {}
    with Path(__file__).with_name("ordinates.tsv").open(encoding="ascii") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        require(reader.fieldnames == ["prime", "conrey_label", "center_numerator", "dimension"],
                "incorrect certificate schema")
        for row in reader:
            q, label, center, dim = (int(row[key]) for key in reader.fieldnames)
            require(1 < label < q and center > 2 and 2 <= dim <= 100, "invalid input row")
            data.setdefault(q, []).append((label, center, dim))
    expected = [p for p in primes_up_to(LAST_PRIME) if p >= FIRST_PRIME]
    require(sorted(data) == expected, "missing or unexpected prime modulus")
    return data


def exclude_zeros(q, fractions, center, radius, skip=None):
    t = arb(center)/DENOMINATOR
    delta = arb(radius)/DENOMINATOR
    s = acb(arb(1)/2, t)
    upper_abs_s = abs(acb(arb(1)/2, t+delta))
    variation = delta*(2 + 4*upper_abs_s)

    # Nonvanishing of eta suffices for zeta at real part 1/2.
    eta = (1 - acb(2)**(1-s))*s.zeta()
    require(eta.abs_lower() > variation, f"unresolved zeta for q={q}, center={center}")

    # DFT entry k corresponds to chi(g^j)=exp(-2*pi*i*k*j/(q-1)).
    # This transform is q^s L(s,chi). Its absolute scaling on the line is sqrt(q).
    transformed = acb.dft([s.zeta(r) for r in fractions])
    threshold = (q-1)*arb(q).sqrt()*variation
    for k in range(1, q-1):
        if k != skip:
            require(transformed[k].abs_lower() > threshold,
                    f"unresolved character for q={q}, k={k}, center={center}")


def verify_prime(q, rows):
    h = q-1
    g = primitive_root(q)
    fractions = [acb(pow(g, j, q))/q for j in range(h)]
    amplitudes = arb(0)
    for label, center, dim in rows:
        chi = dirichlet_char(q, label)
        k = (-int(chi.chi_exponent(g))) % h
        require(k != 0 and chi.conductor() == q, "wrong primitive character")
        require(chi(g).overlaps(acb(0, -2*arb.pi()*k/h).exp()), "character index mismatch")
        lower, upper = arb(center-2)/DENOMINATOR, arb(center+2)/DENOMINATOR
        left, right = chi.hardy_z(lower).real, chi.hardy_z(upper).real
        require(left*right < 0, f"Hardy signs failed for q={q}, label={label}")
        exclude_zeros(q, fractions, center, 2, skip=k)
        denom = ((arb(1)/4 + upper**2)*(arb(9)/4 + upper**2)).sqrt()
        amplitudes += 2*(arb.pi()/(dim+1)).cos()/denom
    require(amplitudes > arb(19)/12, f"insufficient excursion for q={q}")

    checks = len(rows)
    ranges = [range(1-dim, dim) for _, _, dim in rows]
    for vector in product(*ranges):
        # The family is closed under simultaneous conjugation of character and zero.
        # Unit vectors are precisely the selected frequencies already checked.
        norm = sum(abs(n) for n in vector)
        if norm <= 1 or next(n for n in vector if n) < 0:
            continue
        center = abs(sum(n*row[1] for n, row in zip(vector, rows)))
        radius = 2*norm
        require(center > radius, f"frequency combination can be zero for q={q}")
        exclude_zeros(q, fractions, center, radius)
        checks += 1
    return checks, amplitudes


def verify_uniform_constants():
    # Bennett, Martin, O'Bryant and Rechnitzer, Theorem 1.1, at T=4.
    q = arb(673)
    ell = (6*q/(2*arb.pi())).log()
    lower_count = (4/arb.pi()*(4*q/(2*arb.pi()*arb.const_e())).log() + arb(1)/4
                   - arb(22737)/100000*ell - 2*(1+ell).log())
    derivative = 4/arb.pi() - arb(22737)/100000 - 2/(1+ell)
    require(ell > arb(1567)/1000 and lower_count > 1 and derivative > 0,
            "zero-count lower bound failed")
    variance = 18*(q-2)/(65*73)
    require(variance > (arb(19)/12)**2, "variance lower bound failed")

    # Bounds for the residue class 1 at q >= 1000.
    q = arb(1000)
    logq = q.log()
    smoothing_error = ((arb(1427)/100*logq + arb(1625)/100)/q
                       + (arb(161)/10*logq + arb(1783)/100)/q**2)
    upper_d = (2*(2*q).log() + 2)/q + logq/(q**2-1)
    require(smoothing_error < 1 and upper_d < 1
            and q/2 - 8*logq - arb(16)/3 > 0, "class-one bounds failed")
    parity_gain = arb(2).log() - arb(1)/2
    require((q-1)*parity_gain - 8*logq - 5 > 0 and parity_gain > 8/q
            and arb(2).log() > arb(2)/3 and arb(1)/2-1/q**3 > arb(2)/5
            and arb(64)/25*logq > 5 and q/(40*logq) > 2,
            "inverse-class inequalities failed")

    # Compactly supported transform in the low-zero theorem.
    q = arb(8104)
    b, c = arb(9)/4, arb(9)/20
    integral = arb.pi()/b*(2*c**2/3 - 1/(2*b**2))
    slope = 3*arb.pi()/(8*b**4)
    psi_half = -arb.const_euler() - 2*arb(2).log()
    margin = (((q-2)/(q-1)*q.log() - (2*arb.pi()).log() + psi_half)*integral
              - slope*arb.pi()**2/2)
    first_harmonic = arb(2).sqrt()/((arb(1)/4 + c**2)*(arb(9)/4 + c**2)).sqrt()
    require(q > arb(9).exp() and integral > 0 and margin > arb(36)/1000
            and first_harmonic > arb(1342)/1000, "low-zero inequalities failed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=FIRST_PRIME)
    parser.add_argument("--stop", type=int, default=LAST_PRIME)
    parser.add_argument("--bits", type=int, default=112)
    args = parser.parse_args()
    require(args.bits >= 88, "use at least 88 bits")
    require(FIRST_PRIME <= args.start <= args.stop <= LAST_PRIME, "invalid range")
    ctx.prec = args.bits
    verify_uniform_constants()
    data = read_certificates()
    primes = [q for q in sorted(data) if args.start <= q <= args.stop]
    require(primes, "empty range")
    checks = 0
    for q in primes:
        count, _ = verify_prime(q, data[q])
        checks += count
    print(f"precision: {args.bits} bits")
    print(f"prime moduli verified: {len(primes)} ({primes[0]} to {primes[-1]})")
    print(f"reduced classes at these prime moduli: {sum(q-1 for q in primes)}")
    print(f"certified ordinate brackets: {sum(len(data[q]) for q in primes)}")
    print(f"family nonvanishing checks on closed ordinate intervals: {checks}")
    print("amplitude exceeds 19/12 for every listed modulus")
    print("analytic inequalities at q=673, q=1000 and q=8104 verified")


if __name__ == "__main__":
    main()
