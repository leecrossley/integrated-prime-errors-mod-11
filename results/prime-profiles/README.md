# Sign changes in many residue classes

Lee Crossley · 21 November 2026

For a prime $`q`$ and a reduced class $`a`$, let $`E_{q,a}(x)`$ be the integral from $`2`$ to $`x`$ of $`(q-1)\pi(t;q,a)-\mathrm{li}(t)`$, multiplied by $`(\log x)/x^{3/2}`$. Daniel Johnston asked which classes eventually have negative integral. [Problem 23](https://arxiv.org/pdf/2407.03530#page=9) [Zhao's equation (35) and Table 1](https://arxiv.org/html/2411.18903v2#S8)

**Every class through modulus 10,009.** For each prime from 11 through 10,009, in every reduced class, $`\liminf E_{q,a}<-3/2`$ and $`\limsup E_{q,a}>1/4`$. This also holds at twice each prime. There are 1,227 prime moduli and 5,755,168 classes before lifting. The additional prime contributes 10,008 classes. Its zero lies in $`(402441651\pm2)/2^{44}`$ for Conrey character 9959. Two numerical implementations check the bracket and its double. This finite-modulus theorem uses Platt's published real-axis results and works independently of Dirichlet GRH. [Range proof](../../range/PROOF.md) · [Certificate](../../range/ordinates.tsv) · [Platt](https://arxiv.org/abs/1305.3087)

**Many classes at every prime.** Under Dirichlet GRH there are absolute constants $`\delta,\eta>0`$ such that at least $`\delta(q-1)`$ classes have lower limit below $`-\eta\sqrt{q\log q}`$ and upper limit above $`\eta\sqrt{q\log q}`$, for every prime $`q\ge11`$. All but $`O((\log q)^2)`$ classes have a negative lower limit. Class 2 takes both signs when $`q\equiv1\bmod3`$, and class 4 does so when $`q\equiv2\bmod3`$. The proof also gives a positive proportion in each fixed-index coset for sufficiently large $`q`$. The bounds allow central zeros and relations between ordinates. [Paper](integrated-prime-errors-many-classes.pdf) · [TeX](integrated-prime-errors-many-classes.tex)

**Twelve primes for one class.** At $`q=10009`$, $`a=1258`$, twelve progression terms are necessary and sufficient for the forward formula to certify positivity, with all common powers of $`q`$ retained. For two other classes, 148 and 9100, the limiting profile is strictly negative throughout $`|u|\le\log(10^{12})`$. The separate spectral certificate gives late positive excursions in both. The continuous computation covers all real arguments in that interval and makes a statement about the limiting profile. The paper also treats classes for which a growing number of prime-power terms is necessary to exceed the quadratic main term. [Paper](combined-prime-excursions.pdf) · [TeX](combined-prime-excursions.tex) · [Scan certificates](data/)

## Prior work

The question and the integral predate this work. The finite increment is an additional modulus for the family's published method. The all-prime proportion and the explicit choice of class are the substantive analytic additions. Erdős counted classes containing an early prime. Fiorilli and Martin estimated the character sums used here. Martin and Ng studied ordinary prime races. Li, Pratt and Shakan treated the largest least prime in a class. The literature checked did not give these integrated-error conclusions or the twelve-term minimum for this class. Absolute priority and independent peer review remain open. The all-prime conclusion for **every** reduced class still requires a proof. [Erdős](https://www.renyi.hu/~p_erdos/1949-05.pdf) · [Fiorilli and Martin](https://arxiv.org/abs/0912.4908) · [Martin and Ng](https://arxiv.org/abs/1710.00088) · [Li, Pratt and Shakan](https://arxiv.org/abs/1607.02543)

## Verification

From the repository root install the pinned dependency in requirements.txt, then run

~~~sh
python3 -B range/verify_range.py --start 10009 --stop 10009 --bits 112
python3 -B range/crosscheck_range.py --start 10009 --stop 10009 --bits 160
python3 -B results/prime-profiles/check_profiles.py
~~~

Add the --full option to the last command to regenerate all 18,578,682 continuous intervals at each of 128 and 160 bits. The default verifies the stored chains, regenerates the initial grids and checks the explicit prime examples. Both implementations for the all-class certificate use FLINT for endpoint signs. The continuous scans use the same algorithm at two precisions. The analytic implications have written proofs. Lean checks three elementary threshold and integer lemmas. [Replay record and Lean commands](CHECKS.txt) · [Lean source](PrimeExcursions.lean)
