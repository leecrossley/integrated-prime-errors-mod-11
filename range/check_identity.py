"""Check the weighted logarithmic-derivative identity at zero for all classes mod 11.

Run from the repository root with python -m range.check_identity. The exact
profile value from Section 4 must agree with the signed sum over the certified
ordinates to within the independently established 0.154 tail bound.
"""
from flint import acb, acb_series, arb, ctx, dirichlet_char

from verify import center_interval, read_brackets, require


def negative_log_derivative(jet):
    return -jet[1] / jet[0]


def main():
    ctx.prec = 128
    ctx.cap = 2
    denominator, rows = read_brackets()
    first, second = acb_series([1, 1], 2), acb_series([2, 1], 2)
    characters = []
    for label, numerators in rows.items():
        chi = dirichlet_char(11, label)
        if label == 1:
            finite_part = -acb(arb.const_euler())
            at_two = negative_log_derivative(second.zeta())
        else:
            finite_part = negative_log_derivative(first.dirichlet_l(chi))
            at_two = negative_log_derivative(second.dirichlet_l(chi))
        subtotal = acb(0)
        for n in numerators:
            rho = acb(arb(1)/2, center_interval(n, denominator))
            subtotal -= 2/(rho*(rho+1))
        characters.append((chi, finite_part-at_two, subtotal))

    max_error = arb(154)/1000
    for a in range(1, 11):
        b = pow(a, -1, 11)
        derivatives = sum(chi(b).conjugate()*delta for chi, delta, _ in characters)
        require(derivatives.imag.contains(0), "weighted logarithmic derivative is unresolved")
        gamma_term = arb(0)
        if b == 1:
            gamma_term = arb(5)
        elif b == 10:
            gamma_term = 10*(arb(2).log()-arb(1)/2)
        prediction = arb(1)/2 + derivatives.real + gamma_term
        retained = sum((chi(a).conjugate()*subtotal).real for chi, _, subtotal in characters)
        require(abs(prediction-retained) < max_error, f"weighted identity failed for a={a}")
    print("precision: 128 bits")
    print("all ten weighted identities agree with the 850-bracket sums within 0.154")


if __name__ == "__main__":
    main()
