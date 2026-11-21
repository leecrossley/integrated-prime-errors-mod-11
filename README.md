# Integrated prime-counting errors for prime moduli

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24410803.svg)](https://doi.org/10.5281/zenodo.24410803)

The integrated prime-counting error changes sign infinitely often in **every reduced class modulo every prime from 11 through 10,007**. The proof is unconditional. It covers 1,226 prime moduli and 5,745,160 classes. The same result holds at twice each of those primes. The separate modulus-11 proof and its original certificate are preserved here.

Let $`\pi(t;q,a)`$ count primes up to $`t`$ in the class $`a\bmod q`$. For

```math
 E_{q,a}(x)=\frac{\log x}{x^{3/2}}\int_2^x
 \bigl(\varphi(q)\pi(t;q,a)-\mathrm{li}(t)\bigr)\thinspace{}dt,
```

every class in the stated range satisfies

```math
 \liminf_{x\to\infty} E_{q,a}(x)<-\tfrac32,\qquad
 \limsup_{x\to\infty} E_{q,a}(x)>\tfrac14 .
```

Thus the conclusion concerns arbitrarily large inputs $`x`$ at each modulus. Under the generalized Riemann hypothesis (GRH) for the inducing functions at that modulus, each of the two strict excursion sets has positive lower logarithmic density.

[Download the paper](range/paper.pdf) · [Read the full proof](range/PROOF.md) · [Certificate data](range/ordinates.tsv) · [Verification records](range/evidence)

Combining the proof with the Dirichlet GRH theorem announced by Levent Alpöge on 20 November 2026 gives **both signs in class 1 for every prime modulus from 11 onward**. The normalized upper limit in that class exceeds $`q/2-8\log q-16/3`$ for $`q\ge1000`$. The same combination proves positive excursions for $`-1`$ and the inverse of 2 at every prime from 11 onward, and for inverses of every prime power $`2\le b\le q/(40\log q)`$ when $`q\ge1000`$. The corollaries in this paragraph use `LFunction_ne_zero_of_half_lt_re`. [Exact Lean statements](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L6-L16) [Sutherland’s independent verification](https://math.mit.edu/~drew/grh/)

## Where the result extends

| Prime moduli | Classes | Conclusion and hypotheses |
| --- | --- | --- |
| $`11\le q\le10\thinspace{}007`$ | Every reduced class | Both quantitative bounds above, unconditionally |
| $`11\le q\le400\thinspace{}000`$ | Class 1 and every quadratic nonresidue | Both signs arbitrarily far out, unconditionally |
| $`11\le q\le400\thinspace{}000`$ | Every quadratic residue | The normalized lower limit is below $`-4/3`$, unconditionally |
| Every prime $`q\ge11`$ | Class 1 | Both signs if the inducing functions have no real zero in $`(1/2,1)`$. GRH suffices. |
| $`11\le q\le2\thinspace{}000\thinspace{}000`$ | Every quadratic nonresidue | Both signs under Dirichlet GRH and Platt’s central nonvanishing. Every square has a normalized lower limit below $`-4/3`$. |
| Every prime $`q\ge673`$ | Every reduced class | Both quantitative bounds given the finite zero conditions up to height 16 in Theorem 3 |
| Every prime $`q\ge8104`$ | Every reduced class | Under GRH there is a zero below height $`9/20`$ in absolute value. Central nonvanishing, one unshared positive zero that low and exclusion of its double give both signs. |

At every prime from 17 through 10,007 a single well-placed zero certifies all reduced classes at once. For example, at 10,007 the proof locates a zero near height 0.000463485, isolates its character, and excludes its double across the family. The resulting oscillatory contribution exceeds 1.8856 in either direction about the class mean. At 13 the test uses four zeros and at 11 a separate explicit-formula calculation. The prime range uses Platt's published real-axis and central nonvanishing results. [Proof of the finite test](range/PROOF.md#2-a-finite-set-of-ordinates-controls-every-class) · [Platt, Theorems 7.1–7.2](https://arxiv.org/pdf/1305.3087#page=14)

Daniel R. Johnston posed the classification question under GRH in 2024. Under GRH, Zhao's Table 1 lists eventual negativity for $1,3,4,5,9$ modulo 11 and $1,3,5,9,15$ modulo 22. The positive upper limit here conflicts with those entries for the same integral in equation (35). Under GRH the class-one limiting profile already has $1.65147046110676<F_1(0)<1.65147046110677$ by logarithmic derivatives, independently of the zero brackets. Almost periodicity gives arbitrarily close returns at late times. [Class-one calculation](PROOF.md#class-one-witness) Earlier work on finite-frequency tests, prime races and low zeros is credited in the proof. The all-class unconditional result for every sufficiently large prime remains open in this work. This preprint has a written analytic proof and reproducible interval calculations. Lean checks the real-axis specialization and the third-moment inequality. The full analytic argument is a written proof awaiting independent review. [Johnston, Problem 23](https://arxiv.org/pdf/2407.03530#page=9) [Zhao, §8](https://arxiv.org/html/2411.18903v2#S8) [Prior work and remaining question](range/PROOF.md#7-scope-and-prior-work)

## Reproduce the results

Use Python 3.10 or newer. The two range programs check the same integer certificate by different formulas using FLINT's outward-rounded ball arithmetic. Both use FLINT for the endpoint sign tests. The second uses an elementary alternating expansion over whole intervals for the family nonvanishing tests. The programs also accept an inclusive subrange such as `--start 10007 --stop 10007`.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python range/verify_range.py --bits 112
python range/crosscheck_range.py --bits 128
python -m range.check_identity
python verify.py --bits 128
python crosscheck.py --bits 160
python real_axis.py --bits 128
shasum -a 256 -c SHA256SUMS
```

For the two Lean lemmas, use the pinned Mathlib checkout at commit `0df444a360eaa60ab8c11dca51a86af692955474` with its Lean 4.33.1 toolchain and compiled Mathlib cache. From that checkout run `lake env python3 /path/to/repository/range/check_lean.py /path/to/upstream/lean/src`. The checker verifies the compiler and Mathlib commits, hashes the upstream definition file, compiles both modules and replays them through the kernel. It checks the axiom sets of both named lemmas. The first lemma assumes right-half-plane nonvanishing. The second proves a moment inequality. The unconditional finite-modulus theorem has a written proof. Sutherland records the independent checks of the announced upstream formal theorem. [Lean source](range/Oscillation.lean) [Replay record](range/evidence/lean-4.33.1.txt)

The three root-level programs check the original modulus-11 result, including a selection of 850 positive ordinate brackets below height 128, twenty signed inequalities and a real-axis exclusion. The original version also contains the comparison with the entries for 11 and 22 in Zhao's Table 1. [Modulus-11 proof](PROOF.md) [Original two-page note](research-note.pdf) [Modulus-11 verification records](evidence) [First release](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v1.0.0)
