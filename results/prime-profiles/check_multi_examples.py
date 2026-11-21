"""Independent sieve and interval checks for the twelve-prime and paired gap examples."""
from math import gcd

from flint import arb, ctx, fmpz

from verify_prime_side import constants, prime_powers


def twelve():
    q, a, k, limit = 10009, 1258, 12, 6_000_000
    assert fmpz(q).is_prime()
    primes = []
    for n, p in prime_powers(limit):
        if n % q == a:
            if n != p:
                raise ArithmeticError(f"unexpected proper prime power {n}")
            primes.append(n)
    assert len(primes) == 40
    c, d = constants(q)
    b = pow(a, -1, q)
    logq = arb(q).log()
    assert 1+logq+c[b] < 0 and d[b] > 0
    assert limit > 2*(q-1)*k*arb(limit).log() and limit > 2*(q-1)*k
    weights = [(q-1)*arb(p).log() for p in primes]
    tested = 0
    for width in range(1, k):
        for i in range(len(primes)-width+1):
            w = weights[i:i+width]
            moment = sum(p*v for p,v in zip(primes[i:i+width], w))
            assert sum(w)**2/2 < moment
            tested += 1
    y = arb(1_611_211)
    retained = [(p,w) for p,w in zip(primes,weights) if p < y]
    assert len(retained) == k and pow(a,(q-1)//2,q) == q-1
    total = sum(w*(y-p) for p,w in retained)
    assert total > y*y/2
    corrected = (total+logq*(y-q)-y*y/2+y*(1+logq-y.log()+c[b])-logq-d[b])/(y*y.sqrt())
    assert corrected > 1
    print(f"q={q}, a={a}, {len(primes)} primes and no higher powers to {limit}")
    print(f"all {tested} consecutive blocks of 1 through 11 fail the bare test")
    print("1 + log q + c_b:", (1+logq+c[b]).str(17))
    print("successful primes:", [p for p,_ in retained])
    print("corrected profile at y = 1611211:", corrected.str(17))


def paired():
    q, modulus, count = 1_000_003, 210, 9
    assert fmpz(q).is_prime()
    candidates = set(range((2*q) % modulus, q, modulus))-{0}
    pairs = {a for a in candidates if pow(a,-1,q) in candidates and 1 < a < q-1}
    assert all(gcd(2+j,modulus) > 1 for j in range(count))
    exceptions = set()
    for p in (2,3,5,7):
        n = p
        while n <= count*q:
            exceptions.add(n%q)
            n *= p
    surviving = sorted(a for a in pairs if a not in exceptions and pow(a,-1,q) not in exceptions)
    # This time run the independent global sieve and test all prime powers directly.
    check = set(surviving)
    for n,_ in prime_powers(count*q):
        assert n%q not in check
    assert len(surviving) == 10
    squares = sum(pow(a, (q-1)//2, q) == 1 for a in surviving)
    assert squares == 4
    print(f"q={q}, all 10 residues and inverses are prime-power-free up to {count*q}")
    print("quadratic types: 4 squares, 6 nonsquares")
    print(surviving)


def salie():
    # A polynomial of degree < q vanishes at a primitive q-th root of unity
    # exactly when its q integer coefficients are equal, for a prime q.
    tests = 0
    for q in (11, 13, 17, 19, 23):
        chi = [0] + [1 if pow(x, (q-1)//2, q) == 1 else -1 for x in range(1, q)]
        for u in range(q):
            for v in range(1, q):
                coefficients = [0]*q
                for a in range(1, q):
                    coefficients[(u*a+v*pow(a, -1, q)) % q] += chi[a]
                for z in range(q):
                    if (z*z-4*u*v) % q == 0:
                        for a in range(1, q):
                            coefficients[(a+z) % q] -= chi[v]*chi[a]
                assert len(set(coefficients)) == 1
                tests += 1
    print(f"Salié formula: {tests} exact cyclotomic checks, including u = 0")


if __name__ == "__main__":
    ctx.prec, ctx.cap = 160, 2
    twelve()
    paired()
    salie()
