"""Replay the ordinate exclusions by elementary alternating series on closed intervals.

This implementation uses an Euler transform, local Taylor polynomials and an
inverse Fourier transform. It does not call Hurwitz zeta for the exclusions.
"""
import argparse
from itertools import product
from math import comb

from flint import acb, acb_poly, arb, ctx, dirichlet_char

from verify_range import (
    DENOMINATOR, FIRST_PRIME, LAST_PRIME, primitive_root, read_certificates, require,
)


EULER_TERMS = 84
TAYLOR_TERMS = 24
BINS = 4


def euler_weights():
    return [arb((-1)**l * sum(comb(j, l) * 2**(EULER_TERMS-j-1)
                              for j in range(l, EULER_TERMS))) / 2**EULER_TERMS
            for l in range(EULER_TERMS)]


def local_polynomials(s, weights):
    rising = [acb(1)]
    for j in range(1, TAYLOR_TERMS):
        rising.append(-rising[-1]*(s+j-1)/j)
    polys = []
    for bin_i in range(BINS):
        v = 1 + arb(2*bin_i+1)/(2*BINS)
        sums = [acb(0) for _ in rising]
        for l, coeff in enumerate(weights):
            base = v+l
            term = coeff * (-s*base.log()).exp()
            inverse = 1/base
            for j in range(TAYLOR_TERMS):
                sums[j] += term
                term *= inverse
        polys.append(acb_poly([a*b for a, b in zip(rising, sums)]))
    return polys


def residues_for(q, g):
    table = []
    residue = 1
    for _ in range(q-1):
        x = arb(residue)/q
        slot = BINS*residue//q
        h = x - arb(2*slot+1)/(2*BINS)
        table.append((1 if residue % 2 else -1, x.log(), slot, h))
        residue = residue*g % q
    return table


def check_interval(q, table, center, radius, weights, skip=None):
    ordinate = arb(center, radius)/DENOMINATOR
    s = acb(arb(1)/2, ordinate)
    polys = local_polynomials(s, weights)
    values = [sign*((-s*logx).exp()-polys[slot](h)) for sign, logx, slot, h in table]
    # inverse=True divides by q-1. The uniform pointwise error therefore
    # bounds the error in every normalized character coefficient as well.
    transformed = acb.dft(values, inverse=True)
    bound = ((arb(1)/2**EULER_TERMS + (arb(1)/(2*BINS))**TAYLOR_TERMS)
             * (arb.pi()*ordinate).cosh().sqrt())
    for j, value in enumerate(transformed):
        if j != skip:
            # Some FFT factorizations widen a component near zero. A direct
            # sum of the same coefficient encloses the entire interval more tightly.
            if not value.abs_lower() > bound:
                h = len(values)
                angle = acb(0, 2*arb.pi()/h)
                total = sum(term*(angle*((j*k) % h)).exp()
                            for k, term in enumerate(values))
                value = total/h
            require(value.abs_lower() > bound,
                    f"alternating interval unresolved: q={q}, j={j}, center={center}")


def crosscheck_prime(q, rows, weights):
    # Use the inverse primitive root and positive-exponent transform.
    g = pow(primitive_root(q), -1, q)
    table = residues_for(q, g)
    amp = arb(0)
    for label, center, dim in rows:
        chi = dirichlet_char(q, label)
        j = int(chi.chi_exponent(g)) % (q-1)
        endpoints = []
        for offset in (-2, 2):
            t = arb(center+offset)/DENOMINATOR
            s = acb(arb(1)/2, t)
            phase = acb(0,t*(arb(q)/arb.pi()).log()/2).exp()
            endpoints.append(phase*((s+int(chi.parity()))/2).gamma()*s.dirichlet_l(chi))
        require((endpoints[0]*endpoints[1].conjugate()).real < 0,
                f"endpoint lines failed for q={q}")
        check_interval(q, table, center, 2, weights, skip=j)
        s_ball = acb(arb(1)/2, arb(center, 2)/DENOMINATOR)
        v = [(arb.pi()*k/(dim+1)).sin() for k in range(1, dim+1)]
        weight = 2*sum(a*b for a, b in zip(v, v[1:])) / sum(a*a for a in v)
        amp += weight/abs(s_ball*(1+s_ball))
    require(amp > arb(19)/12, f"alternating amplitude failed for q={q}")
    nchecks = len(rows)
    for v in product(*(range(1-d, d) for _, _, d in rows)):
        # Pick the opposite representative of each conjugate pair.
        if sum(abs(k) for k in v) < 2 or next(k for k in v if k) > 0:
            continue
        c = abs(sum(k*row[1] for k, row in zip(v, rows)))
        radius = sum(2*abs(k) for k in v)
        require(c > radius, "potential zero frequency")
        check_interval(q, table, c, radius, weights)
        nchecks += 1
    return nchecks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=FIRST_PRIME)
    parser.add_argument("--stop", type=int, default=LAST_PRIME)
    parser.add_argument("--bits", type=int, default=128)
    args = parser.parse_args()
    require(args.bits >= 96, "use at least 96 bits")
    require(FIRST_PRIME <= args.start <= args.stop <= LAST_PRIME, "invalid range")
    ctx.prec = args.bits
    data = read_certificates()
    primes = [q for q in sorted(data) if args.start <= q <= args.stop]
    require(primes, "empty range")
    weights = euler_weights()
    nchecks = sum(crosscheck_prime(q, data[q], weights) for q in primes)
    print(f"precision: {args.bits} bits")
    print(f"prime moduli verified by alternating sums: {len(primes)} ({primes[0]} to {primes[-1]})")
    print(f"reduced classes at these prime moduli: {sum(q-1 for q in primes)}")
    print(f"family interval exclusions rechecked: {nchecks}")
    print("all endpoint signs and amplitudes verified")


if __name__ == "__main__":
    main()
