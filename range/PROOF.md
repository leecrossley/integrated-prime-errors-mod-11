# Integrated prime-counting errors for prime moduli

Lee Crossley · 21 November 2026

Let $`\pi(t;q,a)`$ count primes $`p\le t`$ congruent to $`a\bmod q`$. Write

```math
 A_{q,a}(x)=\int_2^x\bigl(\varphi(q)\pi(t;q,a)-\mathrm{li}(t)\bigr)\thinspace{}dt,
 \qquad E_{q,a}(x)=x^{-3/2}\log x\thinspace{}A_{q,a}(x).
```

We use the ordinary logarithmic integral. Changing its additive constant has no effect on the conclusions. GRH for a modulus means the critical-line assertion for the primitive functions inducing its characters, including the Riemann zeta function. Each assertion concerns one class at a time.

**Theorem 1.** For every prime $`11\le q\le 10\thinspace{}007`$ and every reduced class $`a\bmod q`$,

```math
 \liminf_{x\to\infty} E_{q,a}(x)<-\tfrac32,\qquad
 \limsup_{x\to\infty} E_{q,a}(x)>\tfrac14. \tag{1}
```

This is unconditional. The same holds at $`2q`$ for every reduced class. Under GRH for that modulus, each of the two strict excursion sets in (1) has positive lower logarithmic density. There are 1,226 prime moduli and 5,745,160 classes before adjoining the odd lifts.

**Theorem 2.** For every prime $`q\ge11`$, class $`1\bmod q`$ takes both signs arbitrarily far out if the inducing functions have no real zero in $`(1/2,1)`$. In particular GRH suffices, with no assumption on central zeros or relations among ordinates. For $`11\le q\le400\thinspace{}000`$, the conclusion for class 1 is unconditional. In the same finite range, unconditionally, every quadratic nonresidue has $`\liminf E_{q,a}<0<\limsup E_{q,a}`$ and every quadratic residue has $`\liminf E_{q,a}<-4/3`$.

Combining the Dirichlet GRH theorem announced by Alpöge with §4 gives the all-primes conclusion for class 1 and rules out eventual negativity for $`-1`$ and inverses of small prime powers. Sections 5 and 6 give two further sufficient conditions for *all* classes at unbounded prime moduli. Their zero hypotheses are stated there. Section 7 explains the open part of Johnston's question. [Problem 23 (D. R. Johnston) in Hamieh, Kadiri, Martin and Ng](https://arxiv.org/pdf/2407.03530#page=9)

## 1. The explicit formula and the real axis

Fix an odd prime $`q`$, put $`h=q-1`$, and let $`C_a`$ be the number of square roots of $`a\bmod q`$. Thus $`C_a`$ is two for a square and zero for a nonsquare. With $`\chi^\ast`$ denoting the primitive character inducing $`\chi`$, set

```math
 D_a(s)=-\sum_{\chi\bmod q}\overline{\chi(a)}\frac{L'}{L}(s,\chi^\ast).
```

The principal factor is $`\zeta`$. A surviving pole at a nontrivial zero $`\rho`$ means that $`\sum_\chi\overline{\chi(a)}m_\chi(\rho)\ne0`$, where $`m_\chi`$ is its multiplicity. The following dichotomy is proved by the calculations in the [fixed-modulus proof, §§1, 3–4](../PROOF.md). For clarity, here are the details that depend on the modulus.

* If no nontrivial pole survives to the right of $`1/2`$, the reflection $`m_\chi(\rho)=m_\chi(1-\bar\rho)`$ cancels the left-side terms too. The coefficients of $`D_a`$ are $`d_a(n)=h1_{n\equiv a\bmod q}\Lambda(n)+1_{n=q^j,\ j\ge1}\log q`$. Moving the first Riesz-mean integral with kernel $`x^{s+1}/[s(s+1)]`$ to $`\Re s=-1/2`$ gives the main term $`x^2/2`$, the critical-line zero sum, and $`O_q(x\log(2x))`$. Removing prime squares contributes $`-(2/3)C_a x^{3/2}+o_q(x^{3/2})`$ by the prime number theorem in fixed progressions. Higher powers contribute $`O_q(x^{4/3}\log^2(2x))`$. Partial summation as in §1 of the fixed-modulus proof yields

```math
 E_{q,a}(x)=F_a(\log x)+o_q(1),\quad
 F_a(u)=-\tfrac23 C_a-
 \sum_\chi\overline{\chi(a)}
 \sum_{\rho=1/2+i\gamma}\frac{e^{i\gamma u}}{\rho(\rho+1)} . \tag{2}
```

  The sum counts multiplicities and only zeros on the line. It converges absolutely and uniformly by the zero count. Conjugation makes $`F_a`$ real. Its Bohr mean $`\mu_a`$ is $`-2C_a/3`$ when there are no central zeros. Any strict excursion of $`F_a`$ persists on intervals of fixed length with bounded gaps, by uniform almost periodicity. After retaining a smaller strict margin this implies positive lower logarithmic density for the corresponding excursion of $`E_{q,a}`$. Here the density is $`\liminf_{X\to\infty}(\log X)^{-1}\int_{[2,X]\cap S}dx/x`$.
* Suppose a nonreal pole survives with $`\beta=\Re\rho>1/2`$, and there are no real zeros in $`(1/2,1)`$. For $`1/2<r<\beta`$, apply Landau's nonnegative Mellin-transform theorem to $`x^{1+r}\pm A_{q,a}(x)`$. The derivative of the continued prime-counting transform equals $`-D_a(s)+2^{1-s}/(s-1)`$ plus a function holomorphic on $`\Re s>1/2`$. Indeed the remaining Euler-product powers have degree at least two, apart from the finite correction at $`q`$. Cancellation at one lets the transform continue along the real axis to $`r`$. Eventual nonnegativity with either sign would give holomorphy on $`\Re s>r`$, contradicting the surviving pole of the derivative. Thus $`\limsup E_{q,a}=+\infty`$ and $`\liminf E_{q,a}=-\infty`$.

For each prime $`q\le400\thinspace{}000`$, Platt's Theorem 7.1 excludes any real off-line zero for the primitive nonprincipal characters modulo $`q`$, and Theorem 7.2 excludes a central zero. His zero counts $`N_\chi(t_0)`$ include every zero with $`|\Im\rho|\le t_0`$, so they cover the real axis. The alternating eta series gives both facts for $`\zeta`$. Those published results are the external computational input for the unconditional extension. [Platt, Theorems 7.1 and 7.2](https://arxiv.org/pdf/1305.3087#page=14)

## 2. A finite set of ordinates controls every class

In the first case of §1 choose distinct positive ordinates $`\gamma_1,\ldots,\gamma_k`$. Suppose that at each positive $`\gamma_i`$ exactly one inducing character vanishes, with any multiplicity $`m_i\ge1`$. Choose integers $`d_i\ge2`$. For integer vectors $`n`$ with $`|n_i|<d_i`$, exclude $`n=0`$ and the signed unit vectors. Require that every remaining $`n\cdot\gamma`$ is nonzero and that $`|n\cdot\gamma|`$ is not a critical-line ordinate of the family. Define

```math
 B=\sum_{i=1}^k\frac{2\cos(\pi/(d_i+1))}
 {|(1/2+i\gamma_i)(3/2+i\gamma_i)|}.
```

Then $`\sup F_a\ge\mu_a+B`$ and $`\inf F_a\le\mu_a-B`$ for **every** reduced $`a`$.

To prove this write $`v_{ij}=(2/(d_i+1))^{1/2}\sin((j+1)\pi/(d_i+1))`$ for $`0\le j<d_i`$. For freely chosen angles $`\theta_i`$ the product

```math
 P(u)=\prod_i\left|\sum_{j=0}^{d_i-1}v_{ij}e^{ij(\gamma_i u-\theta_i)}\right|^2
```

is nonnegative. Its mean is one by the zero-frequency exclusion and $`\sum_j v_{ij}^2=1`$. The unit-vector coefficient in its $`i`$th factor has magnitude $`\sum_{j=0}^{d_i-2}v_{ij}v_{i,j+1}=\cos(\pi/(d_i+1))`$, by the sine addition formula. All cross terms except the signed unit vectors make zero contribution to the mean of $`F_aP`$. At $`\gamma_i`$ the magnitude of the coefficient of $`F_a`$ is exactly $`m_i/|\rho_i(\rho_i+1)|`$, since the character value has modulus one. Choose each angle to align the two complex coefficients. Shifting each angle by $`\pi`$ reverses the sign. The two means are $`\mu_a\pm\sum_i 2m_i\cos(\pi/(d_i+1))/|\rho_i(\rho_i+1)|`$. Positivity and mean one place both numbers between the infimum and supremum of $`F_a`$.

The certificate proves $`B>19/12`$. The upper excursion exceeds $`-4/3+19/12=1/4`$ for squares and $`19/12`$ for nonsquares. The lower excursion is below $`-19/12<-3/2`$ for either type of class. This establishes (1) in the first case. The other case is covered by §1. The finite-frequency argument belongs to the Ingham–Diamond tradition. The sine vector is the classical extremizer of Fejér's first-coefficient inequality. [Diamond, Theorem 1](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1971.Diamond.pdf) · [Krenedits and Révész on the Carathéodory–Fejér extremal problem](https://www.renyi.hu/~revesz/PtwLCA_JAT.pdf)

## 3. What the finite checks prove

The [certificate](ordinates.tsv) records the prime, Conrey character label, integer $`m`$ and dimension $`d`$. Each selected positive ordinate lies strictly between $`(m-2)/2^{44}`$ and $`(m+2)/2^{44}`$. Four ordinates suffice at 13. One suffices for each prime from 17 through 10,007. At 17 the dimension is four, at 23 it is 27 and at every other prime from 17 onward in the range it is three. At dimension three the only harmonic to exclude besides the chosen ordinate is its double. At 11 use the [separate certificate](../PROOF.md). For $`2q`$ there is exactly one reduced lift $`b`$ of each $`a`$. The lists of odd primes coincide and the normalized difference is $`-h1_{a=2}(x-2)\log x/x^{3/2}\to0`$.

For example, at $`q=10\thinspace{}007`$ the selected Conrey label is 8996 and the bracket is $`(8\thinspace{}153\thinspace{}712\thinspace{}093\pm2)/2^{44}`$. The ordinate is within $`2\times10^{-10}`$ of 0.000463485. Only this character can vanish there, and every inducing function is nonzero at twice that ordinate. With $`d=3`$ the certified amplitude exceeds 1.8856 for all 10,006 classes.

Both verifiers reconstruct the list of primes. Both enclose the endpoints at each target, exclude all *other characters* at that target, check every required combination against the whole family, and prove the strict amplitude bound. They require no completeness assertion for a list of zeros. Multiple zeros of the selected character inside its own target interval cause no problem. The checks on linear combinations apply to any selection of one zero from each bracket.

**First implementation.** Opposite signs of the real Hardy function give a zero on the critical line. For each family exclusion a Fourier transform of $`\zeta(s,r/q)`$ over powers of a primitive root gives $`q^s L(s,\chi)`$ at the midpoint. Periodicity bounds each nonprincipal character sum by $`q-1`$. Differentiating $`L(s,\chi)=s\int_1^\infty(\sum_{n\le y}\chi(n))y^{-s-1}dy`$ gives $`|L'(s,\chi)|\le(q-1)(2+4|s|)`$ on the critical line. Multiplication by the ordinate radius bounds the displacement from the midpoint. The factor $`\sqrt q`$ converts midpoint values to the transform's scale. For $`\zeta`$ use $`(1-2^{1-s})\zeta(s)`$, whose alternating coefficient sums are bounded by one. For a combination $`n`$ the possible ordinate radius is $`2\sum_i|n_i|/2^{44}`$. [First verifier](verify_range.py)

**Second implementation.** A completed $`L`$-function on the critical line has a constant phase modulo $`\pi`$. A negative real part of the product of opposite endpoint values, one conjugated, proves a change of sign on that line. For exclusions evaluate the entire interval at once. Put

```math
 U(s,x)=\sum_{n\ge0}(-1)^n(n+x)^{-s}
 =\frac1{\Gamma(s)}\int_0^\infty \frac{y^{s-1}e^{-xy}}{1+e^{-y}}\thinspace{}dy .
```

Grouping the alternating Dirichlet series by residue modulo odd $`q`$ gives

```math
 \sum_{r=1}^{q-1}\chi(r)(-1)^{r-1}U(s,r/q)
 =q^s(1-2^{1-s}\chi(2))L(s,\chi).
```

For the principal character the last factor is $`(1-q^{-s})\zeta(s)`$. None of the extra factors vanish on the critical line. The implementation uses the inverse primitive root and the normalized inverse Fourier transform.

Set $`x=r/q`$ and use $`U(s,x)=x^{-s}-U(s,1+x)`$. Partition $`[1,2]`$ into four equal bins of centres $`v`$. With $`h'=1+x-v`$ we have $`|h'|\le1/8`$ and $`v-|h'|\ge1`$. Expand $`e^{-h'y}`$ to degree 23 inside the integral. The coefficients are $`(-1)^j(s)_j U(s+j,v)/j!`$. In each coefficient use the first 84 terms of

```math
 (1+e^{-y})^{-1}=\tfrac12\sum_{r\ge0}\big((1-e^{-y})/2\big)^r .
```

Its pointwise remainder is at most $`2^{-84}`$. The Taylor remainder of the exponential is at most $`(|h'|y)^{24}e^{|h'|y}/24!`$. For $`\Re s=1/2`$ the sum of the integrated coefficient errors is bounded by $`2^{-84}\Gamma(1/2)/|\Gamma(s)|`$, since the absolute Taylor polynomial is bounded by $`e^{|h'|y}`$. The Taylor error is at most $`8^{-24}\Gamma(1/2)/|\Gamma(s)|`$, using $`\Gamma(24+1/2)/(24!\Gamma(1/2))\le1`$. The total error per normalized Fourier coefficient is at most $`(2^{-84}+8^{-24})\sqrt{\cosh(\pi t)}`$, uniformly for real $`t`$ in the input interval. On a wide Fourier enclosure the program recomputes the affected coefficient by direct summation. It also evaluates the first coefficient of each kernel directly from its sine vector. Both implementations use FLINT's outward-rounded ball arithmetic. [Second verifier](crosscheck_range.py) · [FLINT documentation](https://flintlib.org/doc/acb_dirichlet.html)

## 4. Class one and the range up to 400,000

For $`a=1`$ all character weights equal one. An off-line zero gives a surviving pole on the right, by reflection if necessary. With the real interval free of zeros the second case of §1 applies. In the remaining case GRH holds for this whole family. Central zeros are allowed.

Let $`f_\chi`$ and $`\kappa_\chi`$ be the conductor and parity of $`\chi^\ast`$. Complete the product by setting

```math
 H(s)=s(s-1)\prod_\chi(f_\chi/\pi)^{(s+\kappa_\chi)/2}
       \Gamma((s+\kappa_\chi)/2)L(s,\chi^\ast),\quad
 c=\lim_{s\to1}\left(D_1(s)-\frac1{s-1}\right),\quad d=D_1(2).
```

Here $`c`$ is the negative of the Euler–Kronecker constant of the prime cyclotomic field. Taking the difference of logarithmic derivatives of the order-one completed product cancels the Hadamard constant. Its zeros, with multiplicity, are invariant under $`\rho\mapsto1-\rho`$. Equation (2) at $`u=0`$ therefore gives

```math
 F_1(0)+\tfrac43
 =\frac{H'(2)}{H(2)}-\frac{H'(1)}{H(1)}
 =\tfrac q2+c-d . \tag{3}
```

Indeed the convergent zero sum of the difference is $`\sum_\rho[(2-\rho)^{-1}-(1-\rho)^{-1}]=-\sum_\rho1/[\rho(\rho+1)]`$. In the gamma factors half the characters are even and half odd. Their contribution to the difference is $`h[\psi(3/2)-\psi(1/2)]/4=h/2`$, where $`\psi=\Gamma'/\Gamma`$. The rational factors and the finite parts of the logarithmic derivatives supply $`1/2+c-d`$. [Euler–Kronecker constants for cyclotomic fields](https://arxiv.org/abs/2203.03589)

Here are convenient explicit bounds for $`q\ge1000`$. Apply Fiorilli and Martin's Proposition 3.10 to each nonprincipal character with $`Y=q^4`$. The absolute error in replacing $`-L'(1,\chi)/L(1,\chi)`$ by $`\sum_{n\ge1}\chi(n)\Lambda(n)e^{-n/Y}/n`$ is at most

```math
 e(q)=(14.27\log q+16.25)/q^2+(16.1\log q+17.83)/q^3 .
```

The proposition's proof uses GRH only for the factors being estimated. Orthogonality gives $`\sum_{\chi\ne1}\chi(n)=h1_{n\equiv1\bmod q}-1_{q\nmid n}`$. Also $`\sum_{n\le m}\Lambda(n)/n\le2\log m`$ for integers $`m\ge1`$, since $`\log(m!)=\sum_{n\le m}\Lambda(n)\lfloor m/n\rfloor`$ and $`\lfloor m/n\rfloor\ge m/(2n)`$. Average this inequality using weights $`e^{-m/Y}(1-e^{-1/Y})`$ for integers $`m\ge0`$, with the upper bound $`2\log(1+m)`$. Concavity and the mean $`1/(e^{1/Y}-1)\le Y`$ give $`\sum_n\Lambda(n)e^{-n/Y}/n\le2\log(1+Y)`$. The principal finite part is $`-\gamma_E`$. Dropping the nonnegative progression sum gives $`c\ge-\gamma_E-2\log(1+q^4)-(q-2)e(q)>-8\log q-3`$. Indeed $`q e(q)<1`$ at 1000 and both terms decrease thereafter. [Fiorilli and Martin, Proposition 3.10](https://arxiv.org/pdf/0912.4908#page=31)

The Euler product gives

```math
 d=h\sum_{k\ge1}\frac{\Lambda(kq+1)}{(kq+1)^2}+\frac{\log q}{q^2-1}
 \le\frac{2\log(2q)+2}{q}+\frac{\log q}{q^2-1}<1.
```

Here $`\zeta(2)<2`$ and $`\sum_{k\ge1}(\log k)/k^2<2`$ by comparison with $`\int_1^\infty(1+\log t)t^{-2}dt`$. The final upper bound decreases from $`q=1000`$. Thus $`F_1(0)>q/2-8\log q-16/3>0`$, an increasing lower bound for $`q\ge1000`$. The mean in (2) is at most $`-4/3`$, since the contribution of each central zero is $`-4/3`$ per multiplicity. Recurrence gives both signs. Nonconstancy then puts the infimum strictly below the mean. Theorem 1 covers the smaller primes from 11. Platt provides the required real-zero exclusion through 400,000.

For the other assertions up to 400,000 it remains to show that in the cancellation case $`F_a`$ is nonconstant. Suppose it were constant. Uniqueness of the Bohr coefficients in (2) implies zero residue of $`D_a`$ at every noncentral critical-line zero. Central nonvanishing and cancellation then remove all nontrivial poles. Consider $`M_a(x)=\sum_{n\le x}d_a(n)(x-n)`$ from §1. Shift its contour further to $`\Re s=-N-1/2`$. Only the elementary residues at $`1,0,-1`$ and the possible trivial-zero residues at negative integers remain. At $`-k`$, $`k\ge2`$, the latter have the form $`b_k x^{1-k}/[k(k-1)]`$ with $`|b_k|\le h`$. The functional equations, reflection for the digamma factors and the absolutely convergent logarithmic derivative at $`1-s`$ give $`D_a(s)=O_q(\log(N+|t|+2))`$ on these half-integer lines. The horizontal shifts can be taken at the separated heights used in §1 for each fixed $`N`$. The left integral tends to zero as $`N\to\infty`$ for each $`x>1`$. The resulting series in $`1/x`$ converges locally uniformly to a real analytic function of $`x>1`$, together with the elementary terms. But $`M_a'`$ has a positive jump of $`h\log p`$ at every prime $`p\equiv a\bmod q`$. This contradiction proves nonconstancy. A nonconstant continuous almost periodic function takes values strictly on both sides of its mean because a strict one-sided value recurs on intervals of positive lower density. The means from §1 now give Theorem 2.

**Corollary using Alpöge's announced Dirichlet GRH theorem.** Combining Theorem 2 with its right-half-plane nonvanishing conclusion gives both signs for class 1 at **every prime** $`q\ge11`$. In fact $`\liminf E_{q,1}<-4/3`$ and, for $`q\ge1000`$, $`\limsup E_{q,1}>q/2-8\log q-16/3`$. Strictness at the lower end follows from nonconstancy and the mean bound. The combined proof also gives positive lower logarithmic densities for the two excursion sets in Theorem 1. The nonconstancy argument above, together with Platt's central nonvanishing (Theorem 7.2), gives both signs for **every quadratic nonresidue** and a lower limit below $`-4/3`$ for **every square** at primes $`11\le q\le2\thinspace{}000\thinspace{}000`$.

The exact upstream declaration is `LFunction_ne_zero_of_half_lt_re` in `Main.lean`. In its statement take a real $`s`$ with $`1/2<s<1`$. The required disjunction holds since $`s\ne1`$. The declaration `LFunction_eq_zero_re` puts all nontrivial Dirichlet zeros in the open strip on the critical line. The zeta factor is covered by `riemannHypothesis`. Sutherland's audit of the source release reports a successful module-by-module replay, full export acceptance by two independent kernels, and a match of all five headline statements against the challenge. Its 20 November 2026, 22:05 UTC snapshot lists two additional runs still in progress. This paper uses that external verification for the combined corollaries. Theorem 1 and the range through 400,000 in Theorem 2 have their separate proofs above. [Exact declarations](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4-L12) [Definitions](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L6-L16) [Sutherland's verification record](https://math.mit.edu/~drew/grh/)

**Inverses of small prime powers.** Under the same Dirichlet GRH hypothesis the integral has positive excursions at arbitrarily large inputs, with $`\limsup E_{q,a}>0`$, for $`a=-1\bmod q`$ for every prime $`q\ge11`$, and $`a=b^{-1}\bmod q`$ whenever $`q\ge1000`$ and $`2\le b\le q/(40\log q)`$ is a prime power. In particular $`a=2^{-1}\bmod q`$ has positive excursions for every prime $`q\ge11`$. In these classes central nonvanishing is sufficient for both signs, since their mean is then either zero or $`-4/3`$. Platt supplies this nonvanishing throughout the range ending at two million. For a fixed prime power the inequality on $`b`$ holds at every sufficiently large prime modulus.

To see this, use the differences of the individual completed logarithmic derivatives in (3), weighted by $`\overline{\chi(b)}`$, with the regularizing factor $`s(s-1)`$ only for zeta. Write $`c_b=\mathrm{FP}_{s=1}D_b(s)`$ and $`d_b=D_b(2)`$. The map $`\rho\mapsto1-\rho`$ interchanges the character with its conjugate, replacing $`b`$ by $`a=b^{-1}`$ in the zero sum. The constant conductor terms disappear on taking the difference. Orthogonality within each parity gives

```math
 F_a(0)+\tfrac23 C_a=\tfrac12+c_b-d_b+G_b,\qquad
 G_b=\begin{cases}h/2,& b=1,\\ h(\log 2-1/2),& b=-1\bmod q,\\ 0,&\text{otherwise}.\end{cases}
```

Indeed, for $`b=-1`$ the gamma difference is $`h[2\psi(1)-\psi(1/2)-\psi(3/2)]/4=h(\log2-1/2)`$. For $`b\ne\pm1`$ the weighted even and odd counts both vanish. These identities allow central zeros with their actual multiplicities. At modulus 11 all ten weighted predictions agree with the separately certified sums over 850 zero brackets to within their proven 0.154 remainder. [Arithmetic check](check_identity.py) · [Verification record](evidence/weighted-identity-128.txt)

For $`2\le b\le q-1`$ and $`q\ge1000`$, repeat the preceding bound for $`c`$ after inserting $`\overline{\chi(b)}`$ in the character sum. Its value on each $`n`$ is now $`h1_{n\equiv b\bmod q}-1_{q\nmid n}`$ after excluding the principal character. Keep the nonnegative $`n=b`$ term. This gives $`c_b>h\Lambda(b)e^{-b/q^4}/b-8\log q-3`$. The series for $`d_b`$ gives $`d_b<h\Lambda(b)/b^2+1`$ by the same bound for the tail $`n=kq+b`$, $`k\ge1`$. Hence

```math
 F_a(0)>G_b-8\log q-5+
 (q-1)\frac{\Lambda(b)}{b}\left(e^{-b/q^4}-\frac1b\right).
```

The last bracket exceeds $`2/5`$ because $`b\ge2`$ and $`e^{-b/q^4}\ge1-q^{-3}`$. At $`b=q-1`$, $`G_b-8\log q-5>0`$ at 1000 and increases thereafter. At a prime power $`b\le q/(40\log q)`$ use $`\Lambda(b)\ge\log2>2/3`$ and $`(q-1)/q\ge99/100`$. The last term exceeds $`(264/25)\log q`$, giving $`F_a(0)>0`$. Strict positive excursions follow by recurrence. For $`b=2`$ the size condition holds at 1000 and $`q/\log q`$ increases beyond it. Theorem 1 supplies the smaller moduli.

## 5. A quantitative criterion involving only heights up to 16

**Theorem 3.** Fix a prime $`q\ge673`$. Suppose all the family's nontrivial zeros with $`|\Im\rho|\le16`$ lie on the critical line, there is no central zero, and no two distinct inducing characters have the same positive ordinate below 16. Suppose also that among the positive ordinates below 16 there is no relation $`u+v=w`$, including $`u=v`$. Then (1) holds for every reduced class. These conditions only concern a bounded window at this particular modulus.

A surviving pole on the right is nonreal by the window assumption, so §1 handles that case. In the cancellation case convolve $`F_a`$ with the probability density $`K(t)=(1-\cos(16t))/(16\pi t^2)`$ (continuously extended at zero) and subtract $`\mu_a`$. The resulting real trigonometric polynomial $`S`$ has mean zero. The multiplier is $`(1-|\gamma|/16)_+`$. Write $`M`$ for Bohr mean and $`V=M(S^2)`$. The absence of triples gives $`M(S^3)=0`$. For $`|\gamma|\le4`$ the squared weight is at least $`(3/4)^2`$, and $`|\rho(\rho+1)|^2\le(65/4)(73/4)`$. Each frequency comes from one character. A zero of multiplicity $`m`$ supplies a variance proportional to $`m^2\ge m`$.

For each of the $`q-2`$ nonprincipal characters, Bennett, Martin, O'Bryant and Rechnitzer's Theorem 1.1 gives at least two zeros counted with multiplicity at $`|\gamma|\le4`$. Explicitly, with $`\ell=\log(6q/(2\pi))`$, its lower bound is at least

```math
 \frac4\pi\log\frac{4q}{2\pi e}+\frac14-0.22737\ell-2\log(1+\ell).
```

At 673 it exceeds one and $`\ell>1.567`$. Its derivative in $`\log q`$ is $`4/\pi-0.22737-2/(1+\ell)>0`$ from there onward. Therefore $`V\ge18(q-2)/(65\cdot73)>(19/12)^2`$. [Bennett, Martin, O'Bryant and Rechnitzer, Theorem 1.1](https://arxiv.org/pdf/2005.02989#page=2)

For $`b=\sup S`$, expand $`M[(b-S)(S+\sqrt V)^2]\ge0`$. The first and third moments vanish, so $`2bV\ge2V\sqrt V`$. Applying the same argument to $`-S`$ proves $`\inf S\le-\sqrt V`$. Convolution with a probability density keeps values between the original extrema. Since $`\mu_a`$ is zero or $`-4/3`$, (1) follows. Neither this triple-exclusion condition nor Theorem 3 is used by the checks in Theorem 1. The positive-polynomial-mean implication used here and the real-axis specialization used in §4 are kernel-checked in Lean 4.33.1. The rest of the analytic argument is given in this paper. [Lean lemmas](Oscillation.lean) · [Kernel replay](evidence/lean-4.33.1.txt)

## 6. Finding a low zero at every sufficiently large prime under GRH

**Theorem 4.** Under GRH for the modulus, every prime $`q\ge8104`$ has a zero of an inducing function with $`|\gamma|<9/20`$. If the family is also nonvanishing at the centre, there is a positive such ordinate. If one such positive ordinate belongs to only one inducing character and its double is not a family ordinate, every reduced class satisfies $`\liminf E_{q,a}<0<\limsup E_{q,a}`$. Along with Theorem 1 this gives both signs for every prime $`q\ge11`$ under GRH and the usual linear independence hypothesis on the family's multiset of nonnegative ordinates. The two local conditions on the chosen positive ordinate and central nonvanishing suffice in place of full linear independence.

For the explicit bound choose $`c_0=9/20`$, $`b=9/4`$ and

```math
 H_0(t)=(c_0^2-t^2)(\sin(bt)/(bt))^4,\qquad
 I=\int_{\mathbb R}H_0(t)dt=\frac\pi b\left(\frac{2c_0^2}3-\frac1{2b^2}\right)>0 .
```

Use $`\widehat H_0(u)=\int_{\mathbb R} H_0(t)e^{-iut}dt`$. Its support lies in $`[-9,9]`$. Sum the Weil explicit formula over the $`h`$ primitive inducing functions. The prime-power terms vanish because the only possible integers $`n\ge2`$ satisfy $`n\le e^9<q`$, where $`\sum_\chi\chi^\ast(n)=0`$. The conductor sum is $`(q-2)\log q`$. Equal numbers of even and odd gamma factors and the digamma duplication formula give, with $`J=\int H_0(t)\Re\psi(1/2+it)dt`$,

```math
 \sum_{\chi,\rho} H_0(\gamma)=2H_0(i/2)+
 \frac{(q-2)\log q\thinspace{}I+h(J-\log(2\pi)I)}{2\pi}. \tag{4}
```

The first term comes from the zeta poles and is positive. The test is entire, even and decays quadratically in each fixed horizontal strip. For the explicit formula and the classical low-lying-zero problem see [Hughes and Rudnick, §§2 and 8](https://arxiv.org/pdf/math/0208230).

Here are details giving an explicit positive right side. Write $`T(u)`$ for the transform of $`(\sin(bt)/(bt))^4`$. Convolution of four interval indicators gives, for $`u\ge0`$,

```math
 T(u)=
 \begin{cases}2\pi/(3b)-\pi u^2/(4b^3)+\pi u^3/(16b^4), & 0\le u\le 2b,\\ \pi(4b-u)^3/(48b^4), &2b\le u\le 4b,\\ 0,&u\ge4b .\end{cases}
```

It is even. Since $`\widehat H_0=c_0^2T+T''`$, $`T(u)\le T(0)`$ and $`T''(u)-T''(0)\le Lu`$ for $`L=3\pi/(8b^4)`$, we have $`\widehat H_0(u)-I\le Lu`$. Use

```math
 \Re\psi(1/2+it)-\psi(1/2)=\int_0^\infty
 \frac{1-\cos(ut)}{2\sinh(u/2)}du .
```

Absolute interchange with $`H_0(t)`$ follows by integrating $`|H_0(t)|(1+\log(2+|t|))`$. The integral of $`u/[2\sinh(u/2)]`$ is $`\pi^2/2`$ by its exponential series. It follows that $`J\ge\psi(1/2)I-L\pi^2/2`$. At $`q=8104`$,

```math
 \left(\frac{q-2}{q-1}\log q-\log(2\pi)+\psi(1/2)\right) I-L\pi^2/2>0.036.
```

This expression increases with $`q`$. Thus (4) is positive. Under GRH every $`\gamma`$ is real and $`H_0(t)\le0`$ for $`|t|\ge c_0`$, proving the existence assertion. Conjugation pairs the signs across the family. Under the additional hypotheses, use the one-ordinate test of §2 with $`d=3`$. Its amplitude is at least $`\sqrt2/\sqrt{(1/4+c_0^2)(9/4+c_0^2)}>1.342>4/3`$, enough for both signs. All numerical thresholds in §§4–6 are checked by [the primary verifier](verify_range.py).

## 7. Scope and prior work

The published question is Daniel R. Johnston's 2024 Problem 23. It asks under GRH which individual progressions eventually give a negative integral. Tianyu Zhao discusses this same integral in equation (35) of a 2025 paper. Multiplication by $`\varphi(q)>0`$ gives our $`A_{q,a}`$. Table 1 lists $1,3,4,5,9$ modulo 11 and $1,3,5,9,15$ modulo 22. Table 1 is stated under GRH. The positive excursions in the modulus-11 proof hold unconditionally, so in particular under GRH, and they contradict those ten entries. For the larger prime moduli our quantitative, unconditional inequalities are stronger information than absence from the table. [Problem 23 (D. R. Johnston) in Hamieh, Kadiri, Martin and Ng](https://arxiv.org/pdf/2407.03530#page=9) [Zhao, equation (35) and Table 1](https://arxiv.org/html/2411.18903v2#S8)

Diamond and Ford–Konyagin explain how finite independence checks can prove oscillations in prime number theory. Bays and Hudson studied averages in class-versus-class prime races. Hughes and Rudnick studied low zeros in these prime-conductor families. The specific contribution proposed here is the application to an individual integrated prime count against its logarithmic-integral benchmark, with uniform signed margins, reproducible finite certificates and the general criteria above. Searches using Johnston's problem, Zhao's equation, smoothed prime races and cyclotomic Euler–Kronecker constants located no earlier proof of the unconditional range in Theorem 1. A literature search cannot certify priority. [Diamond](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1971.Diamond.pdf) · [Ford and Konyagin](https://ford126.web.illinois.edu/wwwpapers/racefk.pdf) · [Bays and Hudson](https://eudml.org/doc/152516) · [Hughes and Rudnick](https://arxiv.org/abs/math/0208230)

**The real-zero obstruction in a proof independent of Dirichlet GRH.** Suppose a primitive real quadratic character has a simple real zero $`\beta>1/2`$ and every other nontrivial zero of the whole inducing family has real part at most $`\beta-\delta`$ for some $`\delta>0`$. The Riesz formula from §1 isolates its contribution. The absolute sum of the other zero terms is $`O_q(x^{1+\beta-\delta})`$, and prime squares contribute $`O_q(x^{3/2})`$. The same partial summation now gives

```math
 A_{q,a}(x)\ \sim\ -\frac{\chi(a)x^{1+\beta}}{\beta(\beta+1)\log x}.
```

This hypothetical configuration would give each class one eventual sign. Alpöge’s announced Dirichlet GRH theorem rules out this scenario. A proof independent of that theorem would have to exclude such dominance at all sufficiently large primes. Even after applying Dirichlet GRH, the all-class conclusion for unbounded prime moduli still requires a new argument. Along the route of §6 the outstanding issues are central nonvanishing, an unshared low ordinate and exclusion of its double. No example of this configuration is asserted here. Ford and Konyagin describe the real-zero issue for conventional prime races. [Ford and Konyagin, §3](https://ford126.web.illinois.edu/wwwpapers/racefk.pdf)
