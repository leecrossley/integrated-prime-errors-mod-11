"""Check the strict margins in the choice between the classes 2 and 4."""
from math import isqrt

from flint import arb, ctx

from verify_prime_side import constants, profiles


def check_profiles(q):
    ell = arb(q).log()
    a = 2
    classes = []
    while a*50*ell < q:
        if (q+a) % 3 == 0:
            classes.append(a)
        a *= 2
    named = 2 if q % 3 == 1 else 4
    if named not in classes:
        raise ArithmeticError("named class missing from numerical comparison")
    c, d = constants(q)
    scales = sorted({2*a for a in classes} | {3*q})
    for y, a, forward, _ in profiles(q, c, d, scales, classes):
        if y == 2*a:
            if not (forward > q/(4*arb(2*a).sqrt()) and (a != named or forward > arb(q)/10)):
                raise ArithmeticError(f"positive witness failed at q={q}, a={a}")
        if y == 3*q:
            if not forward < -arb(q).sqrt()/(60 if a == named else 120):
                raise ArithmeticError(f"negative witness failed at q={q}, a={a}")
    print(f"q={q}, forward formula confirmed both margins in classes {classes}")


def check_weights(limit):
    largest = 2*limit+4
    primes = bytearray([1])*(largest+1)
    primes[:2] = bytes(2)
    powers = {}
    for p in range(2, isqrt(largest)+1):
        if primes[p]:
            primes[p*p::p] = bytes((largest-p*p)//p+1)
            n = p*p
            while n <= largest:
                powers[n] = p
                n *= p
    counts = {2: 0, 4: 0}
    for q in range(11, limit+1):
        if not primes[q]:
            continue
        a = 2 if q % 3 == 1 else 4
        n, m = q+a, 2*q+a
        first = n if primes[n] else powers.get(n, 0)
        second = m if primes[m] else powers.get(m, 0)
        if first not in (0, 3) or second not in (0, 2) or (first and second):
            raise ArithmeticError(f"unexpected prime-power pair at {q}, {a}")
        counts[a] += 1
    print(f"integer check for 11 <= q <= {limit}: {counts} ({sum(counts.values())} primes)")


def main():
    ctx.prec, ctx.cap = 160, 2
    q = arb(10000)
    ell = q.log()
    log2 = arb(2).log()
    loss = arb(3)/2 - log2 - 2*arb(3).log()/3
    error = 2*ell**2 + 24*ell
    # The error terms divided by q decrease beyond this endpoint.
    if not (2*ell**2 + 24*ell + 17 > 4*ell + 24):
        raise ArithmeticError("monotonicity at the endpoint failed")
    # t^2*2 + 20*t - 7 has positive derivative for t >= log(10000).
    if not (4*ell+20 > 0):
        raise ArithmeticError("monotonicity of the derivative bound failed")
    if not (arb(3935)/1000 + arb(1427)/100 + arb(161)/10/q.sqrt() < 19
            and arb(1625)/100 + arb(1783)/100/q.sqrt() < 17):
        raise ArithmeticError("Fiorilli--Martin coefficient bounds failed")
    d_tail = (2*(2*q).log()+2)/q + ell/(q*q-1)
    if not d_tail < 1:
        raise ArithmeticError("logarithmic derivative at two has excessive tail")
    pos = ((1-1/q)*log2/2 - (error+28)/q) / arb(8).sqrt()
    neg = (loss - (error+17)/q) / arb(3).sqrt()
    if not (pos > arb(1)/10 and neg > arb(1)/60):
        raise ArithmeticError("the two excursion margins did not pass")
    powers_pos = (1-1/q)*log2/2 - (error+20)/q - 7/(150*ell)
    powers_neg = (loss - arb(1)/50 - (2*ell**2+20*ell+17)/q)/arb(3).sqrt()
    if not (powers_pos > arb(1)/4 and powers_neg > arb(1)/120):
        raise ArithmeticError("power-of-two extension failed")
    print("q >= 10000, verified at 160 bits")
    print("uniform lower bound for limsup E / q:", pos.str(18))
    print("uniform lower bound for -liminf E / sqrt(q):", neg.str(18))
    print("both exceed the stated 1/10 and 1/60, respectively")
    print("power-of-two margins at the endpoint:", powers_pos.str(15), powers_neg.str(15))
    check_weights(2_000_000)
    for modulus in (10_009, 10_037):
        check_profiles(modulus)


if __name__ == "__main__":
    main()
