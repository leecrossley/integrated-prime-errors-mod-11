"""Recompute the mod-11 certificate through Hurwitz zeta and a prime sum."""

from math import isqrt

from flint import acb, acb_series, arb, dirichlet_char

from verify import check_bounds, configure, read_brackets, require, witnesses


def prime_powers(limit):
    sieve = bytearray([1]) * (limit+1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit-p*p)//p+1)
    for p in range(2, limit+1):
        if sieve[p]:
            n = p
            while n <= limit:
                yield p, n
                n *= p


def prime_mass_upper(eta, limit):
    sigma = arb(1)/2 + eta
    pole = 1/sigma + 1/(sigma-1)
    arch = (9*arb(11).log() - 10*arb.pi().log()
            + 5*(sigma/2).digamma() + 5*((sigma+1)/2).digamma()) / 2
    ramified = arb(11).log()/(arb(11)**sigma-1)
    known = arb(0)
    for p, n in prime_powers(limit):
        if n % 11 == 1:
            known += arb(p).log() / arb(n)**sigma
    # The omitted terms of -sum(L'/L) are all nonnegative.
    return (pole + arch - ramified - 10*known)/eta


def arithmetic_profile(v):
    # Exact dual Riesz identity for a=9 and its inverse b=5 (see PROOF.md).
    jet_two = acb_series([2, 1], 2)
    zeta = jet_two.zeta()
    finite_part = -acb(arb.const_euler())
    d_two = -zeta[1]/zeta[0]
    for label in range(2, 11):
        chi = dirichlet_char(11, label)
        weight = chi(5).conjugate()
        one = acb_series([1, 1], 2).dirichlet_l(chi)
        two = jet_two.dirichlet_l(chi)
        finite_part -= weight*one[1]/one[0]
        d_two -= weight*two[1]/two[0]
    require(finite_part.imag.contains(0) and d_two.imag.contains(0), "nonreal dual constants")
    m = arb(0)
    for p, n in prime_powers(v):
        weight = 10*int(n % 11 == 9) + int(p == 11)
        m += weight*(v-n)*arb(p).log()
    x = arb(v)
    zero_residue = x*(x.log()-1-arb(11).log()-finite_part.real)
    return ((m-x*x/2-zero_residue-arb(11).log()-d_two.real)/(x*x.sqrt())
            - arb(4)/3)


def class_one_witness():
    """Evaluate the class-one limiting profile from completed logarithmic derivatives at 1 and 2."""
    half = arb(1) / 2
    zeta_at_two = acb_series([2, 1], 2).zeta()
    # The two derivatives of log xi share the constant from its power of pi.
    at_one = 1 + arb.const_euler() + half.digamma() / 2
    at_two = arb(3) / 2 + (zeta_at_two[1] / zeta_at_two[0]).real + arb(1).digamma() / 2
    for label in range(2, 11):
        chi = dirichlet_char(11, label)
        parity = chi.parity()

        def logarithmic_derivative(s):
            jet = acb_series([s, 1], 2).dirichlet_l(chi)
            return (jet[1] / jet[0]).real + (arb(s + parity) / 2).digamma() / 2

        at_one += logarithmic_derivative(1)
        at_two += logarithmic_derivative(2)
    value = -arb(4) / 3 - at_one + at_two
    print("Class-one limiting profile at time zero:", value.str(18))
    if not arb("1.65147046110676") < value or not value < arb("1.65147046110677"):
        raise ArithmeticError("Profile lies outside the quoted interval.")


def finite_prime_integral():
    x = 21_000
    prime_integral = 10 * sum(x - p for p, n in prime_powers(x) if n == p and p % 11 == 9)

    def antiderivative(t):
        log_t = arb(t).log()
        return t * log_t.ei() - (2 * log_t).ei()

    error = prime_integral - (antiderivative(x) - antiderivative(2))
    normalised = arb(x).log() * error / (x * arb(x).sqrt())
    print("Actual class-nine integral at 21000:", normalised.str(18))
    if not arb("-0.264084655513") < normalised or not normalised < arb("-0.264084655512"):
        raise ArithmeticError("Prime integral lies outside the quoted interval.")


def crosscheck():
    den, rows = read_brackets()
    times = witnesses()
    half = arb(1)/2
    eta = arb(3).sqrt()/2
    dlog = {pow(2, k, 11): k for k in range(10)}
    two_pi = 2*arb.pi()
    roots = [acb(0, two_pi*k/10).exp() for k in range(10)]
    fractions = [acb(r)/11 for r in range(1, 11)]
    # A class is a square exactly when its discrete logarithm is even.
    sums = {a: [(-arb(4)/3 if dlog[a] % 2 == 0 else arb(0)) for _ in range(2)]
            for a in times}
    retained = arb(0)
    for label, nums in rows.items():
        k = dlog[label]
        parity = k % 2
        conductor = 11 if k else 1
        weights = [roots[(k*dlog[r]) % 10] for r in range(1, 11)]

        def completed(t):
            s = acb(half, t)
            if k:
                value = sum(w*s.zeta(frac) for w, frac in zip(weights, fractions)) / acb(11)**s
            else:
                value = s.zeta()
            return value*((s+parity)/2).gamma()*acb(0, t*(arb(conductor)/arb.pi()).log()/2).exp()

        for n in nums:
            left, right = completed(arb(n)/den), completed(arb(n+1)/den)
            require((left*right.conjugate()).real < 0, f"Hurwitz endpoint test failed: {label}, {n}")
            g = (arb(n, 1) + 1) / den  # includes the certified bracket, with a wider upper end
            g2 = g*g
            retained += 2/(eta**2+g2)
            denominator = (g2+arb(1)/4)*(g2+arb(9)/4)
            for a, pair in times.items():
                for side, t in enumerate(pair):
                    angle = t*g - two_pi*((k*dlog[a]) % 10)/10
                    sin, cos = angle.sin_cos()
                    sums[a][side] += 2*((g2-arb(3)/4)*cos-2*g*sin)/denominator
    limit = 2_000_000
    omitted_bound = prime_mass_upper(eta, limit) - retained
    require(omitted_bound > 0 and omitted_bound < arb(17)/100, "prime remainder too wide")
    print(f"positive ordinates rechecked using Hurwitz zeta: {sum(map(len,rows.values()))}")
    print(f"prime powers sieved through: {limit}")
    print(f"upper estimate for unretained mass: {omitted_bound.str(10)}")
    check_bounds(sums, omitted_bound)
    for idx, v in enumerate([31, 21_000]):
        value = arithmetic_profile(v)
        lo, hi = ((-arb(2353)/1000, -arb(2352)/1000) if idx == 0
                  else (arb(4974)/10000, arb(4976)/10000))
        require(value > lo and value < hi, "dual Riesz bound failed")
        require(value > sums[9][idx]-omitted_bound and value < sums[9][idx]+omitted_bound,
                "prime and zero enclosures disagree")
        print(f"prime-side value for class 9 at log({v}): {value.str(14)}")
    print("all twenty inequalities and both prime-side checks verified")


if __name__ == "__main__":
    configure()
    crosscheck()
    class_one_witness()
    finite_prime_integral()
