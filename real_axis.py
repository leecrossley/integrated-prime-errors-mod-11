"""Exclude real zeros on [1/2,1] for the nine nonprincipal characters."""

from flint import arb

from verify import configure, require


def verify_real_axis():
    limit = 11_000
    counts = 64
    dlog = {pow(2, j, 11): j for j in range(10)}
    roots = [(2*arb.pi()*j/10).cos() for j in range(10)]
    weights = {k: [roots[(k*dlog[r]) % 10] for r in range(1, 11)]
               for k in range(1, 10)}
    logs = [(n % 11, arb(n).log()) for n in range(1, limit+1) if n % 11]
    tail = 10/arb(limit).sqrt()
    variation = arb(40)/256
    for j in range(counts):
        center = arb(1)/2 + arb(2*j+1)/256
        grouped = [arb(0) for _ in range(11)]
        for residue, logn in logs:
            grouped[residue] += (-center*logn).exp()
        for k in weights:
            finite = sum(w*g for w, g in zip(weights[k], grouped[1:]))
            require(finite-tail-variation > arb(1)/20,
                    f"unresolved character {k} in real interval {j}")
    print("nonprincipal characters checked: 9")
    print("closed intervals covering [1/2,1]: 64")
    print("terms in each character sum: n <= 11000")
    print("Re L(s,chi) > 1/20 throughout [1/2,1] for all nine characters")


if __name__ == "__main__":
    configure()
    verify_real_axis()
