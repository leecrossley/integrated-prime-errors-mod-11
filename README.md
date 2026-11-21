# Integrated prime-counting errors for prime moduli

The integrated prime-counting error changes sign infinitely often in **every reduced class modulo every prime from 11 through 10,007**. The proof is unconditional. It covers 1,226 prime moduli and 5,745,160 classes. The same result holds at twice each of those primes. The separate modulus-11 proof and its original certificate are preserved here.

Let $\pi(t;q,a)$ count primes up to $t$ in the class $a\bmod q$. For
$$
 E_{q,a}(x)=\frac{\log x}{x^{3/2}}\int_2^x
 \bigl(\varphi(q)\pi(t;q,a)-\operatorname{li}(t)\bigr)\,dt,
$$
every class in the stated range satisfies
$$
 \liminf_{x\to\infty} E_{q,a}(x)<-\tfrac32,\qquad
 \limsup_{x\to\infty} E_{q,a}(x)>\tfrac14 .
$$
Thus the conclusion concerns arbitrarily large inputs $x$ at each modulus. Under the generalized Riemann hypothesis (GRH) for the inducing functions at that modulus, each of the two strict excursion sets has positive lower logarithmic density.

[Download the paper](range/paper.pdf) · [Read the full proof](range/PROOF.md) · [Certificate data](range/ordinates.tsv) · [Verification records](range/evidence)

## Where the result extends

| Prime moduli | Classes | Conclusion and hypotheses |
| --- | --- | --- |
| $11\le q\le10\,007$ | Every reduced class | Both quantitative bounds above, unconditionally |
| $11\le q\le400\,000$ | Class 1 and every quadratic nonresidue | Both signs arbitrarily far out, unconditionally |
| $11\le q\le400\,000$ | Every quadratic residue | The normalized lower limit is below $-4/3$, unconditionally |
| Every prime $q\ge11$ | Class 1 | Both signs if the inducing functions have no real zero in $(1/2,1)$. GRH suffices. |
| Every prime $q\ge673$ | Every reduced class | Both quantitative bounds given the finite zero conditions up to height 16 in Theorem 3 |
| Every prime $q\ge8104$ | Every reduced class | Under GRH there is a zero below height $9/20$ in absolute value. Central nonvanishing, one unshared positive zero that low and exclusion of its double give both signs. |

At every prime from 17 through 10,007 a single well-placed zero certifies all reduced classes at once. For example, at 10,007 the proof locates a zero near height 0.000463485, isolates its character, and excludes its double across the family. The resulting oscillatory contribution exceeds 1.8856 in either direction about the class mean. At 13 the test uses four zeros and at 11 a separate explicit-formula calculation. The prime range uses Platt's published real-axis and central nonvanishing results. [Proof of the finite test](range/PROOF.md#2-a-finite-set-of-ordinates-controls-every-class) · [Platt, Theorems 7.1–7.2](https://arxiv.org/pdf/1305.3087#page=14)

Daniel R. Johnston posed the classification question under GRH in 2024. Tianyu Zhao subsequently discussed the same integral under equation (35) and gave a table of eventually negative classes. Earlier work on finite-frequency tests, prime races and low zeros is credited in the proof. The all-class unconditional result for every sufficiently large prime remains open in this work. This preprint has a written analytic proof and reproducible interval calculations. Independent peer review and formal proof-assistant verification remain outstanding. [Johnston, Problem 23](https://arxiv.org/pdf/2407.03530#page=9) · [Zhao, §8](https://arxiv.org/html/2411.18903v2#S8) · [Prior work and remaining question](range/PROOF.md#7-scope-and-prior-work)

## Reproduce the results

Use Python 3.10 or newer. The two range programs check the same integer certificate by different formulas using FLINT's outward-rounded ball arithmetic. The second uses an elementary alternating expansion over whole intervals for the family nonvanishing tests. The programs also accept an inclusive subrange such as `--start 10007 --stop 10007`.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python range/verify_range.py --bits 112
python range/crosscheck_range.py --bits 128
python verify.py --bits 128
python crosscheck.py --bits 160
python real_axis.py --bits 128
shasum -a 256 -c SHA256SUMS
```

The three root-level programs check the original modulus-11 result, including 850 positive ordinate brackets, twenty signed inequalities and a real-axis exclusion. The original version also contains the comparison with the entries for 11 and 22 in Zhao's Table 1. [Modulus-11 proof](PROOF.md) · [Original two-page note](research-note.pdf) · [Modulus-11 verification records](evidence) · [First release](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v1.0.0)
