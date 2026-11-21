"""Compare the two prime-square coefficients in Zhao's Table 1 under GRH."""

from fractions import Fraction
from functools import cache
from math import gcd

from flint import acb_series, arb, ctx, dirichlet_char


@cache
def primitive_characters(conductor):
    characters = []
    for label in range(1, conductor):
        if gcd(label, conductor) == 1:
            character = dirichlet_char(conductor, label)
            if character.is_primitive():
                characters.append(character)
    return characters


@cache
def primitive_mass(conductor, position):
    """Sum 1/(x² + γ²) over the primitive factors of this conductor."""
    angle = arb(position.numerator) / (2 * position.denominator)
    x = (arb(1) / 4 + 2 * angle.sin_pi()**2).sqrt()
    s = arb(1) / 2 + x
    if conductor == 1:
        if position == 0:
            # The pole of zeta cancels the zero of s - 1 at this endpoint.
            derivative = 1 + arb.const_euler() / 2 - (4 * arb.pi()).log() / 2
        else:
            jet = acb_series([s, 1], 2).zeta()
            derivative = 1/s + 1/(s-1) + ((s/2).digamma() - arb.pi().log())/2 + (jet[1]/jet[0]).real
    else:
        derivative = arb(0)
        for character in primitive_characters(conductor):
            jet = acb_series([s, 1], 2).dirichlet_l(character)
            gamma_term = ((s + character.parity()) / 2).digamma()
            derivative += ((arb(conductor) / arb.pi()).log() + gamma_term) / 2 + (jet[1] / jet[0]).real
    return derivative / x


def bounds(conductors, intervals):
    samples = []
    for index in range(intervals + 1):
        position = Fraction(index, intervals)
        samples.append(sum(primitive_mass(f, position) for f in conductors))
    if not all(left > right for left, right in zip(samples, samples[1:])):
        raise ArithmeticError("The interval evaluations did not separate adjacent samples.")
    return sum(samples[1:]) / intervals, sum(samples[:-1]) / intervals


def below(lower, upper, threshold):
    if upper < threshold:
        return True
    if lower > threshold:
        return False
    return None


PRINTED_ROWS = {
    2: [1],
    3: [1],
    4: [1],
    5: [1, 4],
    7: [1, 2, 4],
    8: [1],
    9: [1, 4, 7],
    10: [1, 9],
    11: [1, 3, 4, 5, 9],
    12: [1],
    14: [1, 9, 11],
    15: [1, 4],
    16: [1, 9],
    18: [1, 7, 13],
    20: [1, 9],
    21: [1, 4, 16],
    22: [1, 3, 5, 9, 15],
    24: [1],
    28: [1, 9, 25],
    30: [1, 19],
    36: [1, 13, 25],
    40: [1, 9],
    42: [1, 25, 37],
    48: [1, 25],
    60: [1, 49],
    84: [1, 25, 37],
    120: [1, 49],
}


def enumerate_moduli(retained, limit):
    """Apply the small-modulus and doubling rule described in Zhao's Theorem 4 notebook."""
    direct = {q: classes for q, classes in retained.items() if q >= 5 and q % 4 != 2}
    result = dict(direct)
    for q, classes in direct.items():
        if q % 2 and 2 * q <= limit:
            result[2 * q] = sorted(a if a % 2 else a + q for a in classes)
    for q in (2, 3, 4):
        result[q] = retained[q]
    return result


def compare():
    retained, integrated = {}, {}
    for q in range(2, 121):
        units = [r for r in range(1, q) if gcd(r, q) == 1]
        squares = sorted({r*r % q for r in units})
        roots = sum(r*r % q == 1 for r in units)
        conductors = [f for f in range(1, q + 1) if q % f == 0]
        if 1 + sum(len(primitive_characters(f)) for f in conductors if f > 1) != len(units):
            raise ArithmeticError(f"Wrong number of primitive factors for modulus {q}.")
        for intervals in (4, 8, 16, 32, 64, 128):
            lower, upper = bounds(conductors, intervals)
            earlier = below(lower, upper, 2*roots)
            prime_integral = below(lower, upper, arb(2)*roots/3)
            if earlier is not None and prime_integral is not None:
                break
        else:
            raise ArithmeticError(f"Threshold undecided for modulus {q}.")
        if earlier:
            retained[q] = squares
        if prime_integral:
            integrated[q] = squares
        if q in (11, 22):
            lower, upper = bounds(conductors, 128)
            if not (arb("3.77") < lower and upper < arb("3.78")):
                raise ArithmeticError(f"Absolute zero sum outside the stated bounds for {q}.")
            print(f"q = {q}, square classes {squares}, 3.77 < S < 3.78, bias 4/3")

    if retained != {**PRINTED_ROWS, 6: [1]}:
        raise ArithmeticError("The unrestricted comparison differs from the printed rows plus (6, 1).")
    if enumerate_moduli(retained, 120) != PRINTED_ROWS:
        raise ArithmeticError("The notebook's enumeration differs from the published table.")
    print("Moduli passing with 2C:", sorted(retained))
    print("Moduli passing with 2C/3:", sorted(integrated))
    print("All 63 printed pairs pass with 2C. The extra pair through modulus 120 is (6, 1).")
    print("The notebook enumeration reproduces all 63 pairs exactly, including the omission of (6, 1).")


if __name__ == "__main__":
    with ctx.workprec(128):
        compare()
