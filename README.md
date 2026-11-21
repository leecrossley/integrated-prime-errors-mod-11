# Integrated prime-counting errors modulo 11 and 22

The integrated prime-counting error changes sign arbitrarily far out in **every reduced residue class modulo 11 and 22**. This holds unconditionally and gives the classification for both moduli in Daniel R. Johnston's Problem 23. [Original problem, p. 9](https://arxiv.org/pdf/2407.03530#page=9)

For $\pi(t;q,a)$ the number of primes up to $t$ in class $a$, define

$$
E_{q,a}(x)=\frac{\log x}{x^{3/2}}\int_2^x\bigl(\varphi(q)\pi(t;q,a)-\operatorname{li}(t)\bigr)\,dt.
$$

For each of the twenty reduced classes across the two moduli,

$$
\liminf_{x\to\infty}E_{q,a}(x)<-\frac32,\qquad
\limsup_{x\to\infty}E_{q,a}(x)>\frac14.
$$

The theorem requires no assumption on the location or independence of the zeros. Under GRH for $\zeta(s)$ and the nine primitive nonprincipal Dirichlet $L$-functions modulo 11, both excursion sets also have positive lower logarithmic density. The modulus-22 statement follows because the paired classes contain the same odd primes.

Tianyu Zhao's Table 1 lists five eventually negative classes for each modulus. Its equation (35) differs from the integral above only by the factor $\varphi(q)$. The positive excursions give the opposite answer for those ten entries. The comparison is with the table in the concluding section of that paper. [Equation (35) and Table 1](https://arxiv.org/html/2411.18903v2#S8)

[Read the proof and prior-work comparison](PROOF.md) · [Two-page research note](research-note.pdf) · [Numerical evidence](evidence)

## Reproduce the certificate

Use Python 3.10 or newer with the pinned package in an isolated environment.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python verify.py --bits 128
python crosscheck.py --bits 160
python real_axis.py --bits 128
shasum -a 256 -c SHA256SUMS
```

Two programs validate all 850 positive zero brackets and all twenty signed inequalities for the critical-line profile at modulus 11. The first bounds the omitted zeros using logarithmic derivatives at one. The second uses Hurwitz zeta, an upper bound from sieving prime powers through two million, and a separate prime-side calculation for class 9. A third program certifies nonvanishing on a whole real interval using finite character sums. All three use FLINT's outward-rounded ball arithmetic. The proof handles both possibilities for zeros off the critical line. If their contributions cancel for a class, recurrence gives both signs. If a pole survives, Landau's theorem gives still larger excursions. [First run](evidence/dirichlet-128.txt) · [Second run](evidence/hurwitz-160.txt) · [Real-axis check](evidence/real-axis-128.txt) · [FLINT documentation](https://flintlib.org/doc/acb_dirichlet.html)

This is a research preprint with a written proof and reproducible interval certificates. It has not been peer reviewed.
