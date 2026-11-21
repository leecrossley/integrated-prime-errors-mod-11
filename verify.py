"""Certify the twenty inequalities for the integrated prime error modulo 11."""

import argparse
import json
from pathlib import Path

from flint import acb, acb_series, arb, ctx, dirichlet_char


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def read_brackets():
    source = Path(__file__).with_name("zero-brackets.json")
    data = json.loads(source.read_text(encoding="ascii"))
    denominator = data["denominator"]
    require(type(denominator) is int and denominator > 0, "invalid denominator")
    rows = data["lower_numerators"]
    require(set(rows) == {str(i) for i in range(1, 11)}, "missing character")
    for label, nums in rows.items():
        previous = -1
        for n in nums:
            require(type(n) is int and n > 0 and n > previous + 1,
                    f"nonpositive or overlapping brackets for character {label}")
            require(n + 1 <= 128 * denominator, "ordinate above 128")
            previous = n
    return denominator, {int(label): nums for label, nums in rows.items()}


def witnesses():
    # Times are integers divided by four, except for the two prime-side checks.
    quarters = {1: (6436, 0), 2: (2675, 8992), 3: (1100, 6970),
                4: (3342, 4494), 5: (2002, 9830), 6: (2991, 8494),
                7: (2353, 1606), 8: (10378, 733), 10: (10529, 9703)}
    times = {a: (arb(left) / 4, arb(right) / 4)
             for a, (left, right) in quarters.items()}
    times[9] = (arb(31).log(), arb(21000).log())
    return times


def configure():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, default=128)
    args = parser.parse_args()
    require(args.bits >= 80, "use at least 80 bits")
    ctx.prec = args.bits
    ctx.cap = 2
    print(f"working precision: {args.bits} bits")


def center_interval(n, den):
    # An outward-rounded real ball containing [n/den, (n+1)/den].
    return arb(2 * n + 1, 1) / (2 * den)


def check_bounds(sums, remainder):
    print("class  upper bound at minus time  lower bound at plus time")
    for a in range(1, 11):
        upper = sums[a][0] + remainder
        lower = sums[a][1] - remainder
        require(upper < -arb(3)/2 and lower > arb(1)/4,
                f"theorem bound failed for class {a}: {upper}, {lower}")
        # The floats only suggest display endpoints. Certify each endpoint again.
        up = int(float(upper.upper()) * 1000) + 1
        down = int(float(lower.lower()) * 1000) - 1
        require(upper < arb(up)/1000 and lower > arb(down)/1000,
                "rounded display bounds failed")
        print(f"{a:>5} {up / 1000:>26.3f} {down / 1000:>25.3f}")


def verify():
    den, rows = read_brackets()
    times = witnesses()
    half = arb(1)/2
    bias = {a: -arb(2) * sum(r*r % 11 == a for r in range(1, 11))/3
            for a in range(1, 11)}
    sums = {a: [bias[a], bias[a]] for a in times}
    mass = 2 + arb.const_euler() - (4 * arb.pi()).log()
    retained_mass = arb(0)
    count = 0
    for label in range(1, 11):
        chi = dirichlet_char(11, label)
        if label == 1:
            conductor, parity = 1, 0
            lvalue = lambda s: s.zeta()
        else:
            conductor = chi.conductor()
            require(conductor == 11, "incorrect conductor")
            parity = int(chi(10).real < 0)
            lvalue = lambda s: s.dirichlet_l(chi)
            jet = acb_series([1, 1], 2).dirichlet_l(chi)
            mass += ((arb(11)/arb.pi()).log() - arb.const_euler()
                     - (1 + (-1)**parity)*arb(2).log() + 2*(jet[1]/jet[0]).real)
        weights = {a: chi(a).conjugate() for a in times}
        ref = lvalue(acb(half)).conjugate()
        require(ref.abs_lower() > 0, "vanishing or unresolved central value")
        log_factor = (arb(conductor)/arb.pi()).log()/2

        def hardy(t):
            s = acb(half, t)
            phase = log_factor*t + ((s+parity)/2).lgamma().imag
            return (acb(0, phase).exp()*lvalue(s)*ref).real

        for n in rows[label]:
            left = hardy(arb(n)/den)
            right = hardy(arb(n+1)/den)
            require(left * right < 0, f"unverified zero for character {label}, n={n}")
            g = center_interval(n, den)
            retained_mass += 2/(half**2 + g**2)
            rho = acb(half, g)
            coefficient = -2/(rho*(rho+1))
            for a, pair in times.items():
                for side, t in enumerate(pair):
                    sums[a][side] += (coefficient*weights[a]*acb(0, t*g).exp()).real
            count += 1
    omitted = mass - retained_mass
    require(omitted > 0 and omitted < arb(154)/1000, "missing mass bound failed")
    print(f"certified positive ordinates: {count}")
    print(f"upper estimate for total critical-line mass: {mass.str(15)}")
    print(f"upper estimate for unretained critical-line mass: {omitted.str(10)}")
    check_bounds(sums, arb(154)/1000)
    print("all twenty inequalities verified")


if __name__ == "__main__":
    configure()
    verify()
