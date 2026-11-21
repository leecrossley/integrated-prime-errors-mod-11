# Integrated prime-counting errors modulo 11 and 22

Lee Crossley · 21 November 2026

Let $\pi(x;q,a)$ count primes $p\le x$ with $p\equiv a\bmod q$. For a reduced class $a$, put

$$
A_{q,a}(x)=\int_2^x \bigl(\varphi(q)\pi(t;q,a)-\mathrm{li}(t)\bigr)\thinspace dt,\qquad
E_{q,a}(x)=\frac{\log x}{x^{3/2}}A_{q,a}(x).
$$

**Theorem (unconditional).** For $q=11$ or $22$ and every reduced class $a\bmod q$,

$$
\liminf_{x\to\infty} E_{q,a}(x)<-\frac32,\qquad
\limsup_{x\to\infty} E_{q,a}(x)>\frac14.
$$

If GRH holds for the Riemann zeta function and the nine primitive nonprincipal Dirichlet $L$-functions of conductor 11, there is a further conclusion. The sets where $E_{q,a}<-3/2$ and where $E_{q,a}>1/4$ each have positive lower logarithmic density. The assertions are for each class separately. The argument permits repeated zeros, shared ordinates and rational relations among ordinates.

## 1. Two possibilities for an individual residue class

Fix $q=11$. Write $\chi^\ast$ for the primitive character inducing $\chi\bmod 11$, taking $L(s,\chi^\ast)=\zeta(s)$ for the principal character. Let $C_a$ count the reduced solutions of $r^2\equiv a\bmod 11$. It equals two for $a\in\lbrace1,3,4,5,9\rbrace$ and zero otherwise. Define a function on all real $u$ by

$$
F_a(u)=-\frac23 C_a-
\sum_{\chi\bmod 11}\overline{\chi(a)}
\sum_{\rho_\chi}\frac{e^{iu\gamma_\chi}}{\rho_\chi(\rho_\chi+1)},
\qquad \rho_\chi=\tfrac12+i\gamma_\chi .
\tag{1}
$$

In (1) sum only over nontrivial zeros **on the critical line**, with multiplicity. The standard zero count $N_\chi(T)=O((T+2)\log(T+2))$ gives absolute and uniform convergence. Pairing a zero of $\chi^\ast$ with its conjugate for $\overline{\chi^\ast}$ makes (1) real.

To determine when this profile describes the error, form

$$
D_a(s)=\sum_{\chi\bmod 11}\overline{\chi(a)}\frac{-L'}{L}(s,\chi^\ast)
      =\sum_{n\ge1} d_a(n)n^{-s},\qquad \Re s>1.
$$

At a nontrivial zero $\rho$, write $m_\chi(\rho)$ for its multiplicity in $L(s,\chi^\ast)$, using zero when it is absent. The residue of $D_a$ there is $-\sum_\chi\overline{\chi(a)}m_\chi(\rho)$. For each individual $\chi^\ast$ its functional equation and conjugation give $m_\chi(\rho)=m_\chi(1-\overline{\rho})$. Thus if all such residues vanish to the right of the critical line, they vanish to the left as well. Call this the cancellation case. It includes GRH. In the other case $D_a$ has a pole with real part greater than $1/2$. Section 4 proves that this forces larger excursions in both directions.

In the cancellation case we claim $E_{11,a}(x)=F_a(\log x)+o(1)$. By character orthogonality, $d_a(n)=10\thinspace1_{n\equiv a\bmod 11}\Lambda(n)+1_{n=11^j,\ j\ge1}\log 11$, where $\Lambda$ is the von Mangoldt function. The extra term comes from using the primitive zeta function. The first Riesz mean
$M_a(x)=\sum_{n\le x}d_a(n)(x-n)$ has Mellin integral $D_a(s)x^{s+1}/[s(s+1)]$ on any line $\Re s>1$, with factor $1/(2\pi i)$.

Move the line to $\Re s=-1/2$. The pole at $s=1$ contributes $x^2/2$. Off-line terms cancel by the defining condition of this case. The residue calculation may be grouped by ordinate and real part, since the zero sums before grouping are absolutely convergent for each fixed $x$. Each critical-line zero contributes $-\overline{\chi(a)}x^{\rho_\chi+1}/[\rho_\chi(\rho_\chi+1)]$ per multiplicity. The possible pole at zero has order at most two and contributes $O(x\log(2x))$. On the left line the functional equation and the absolutely convergent logarithmic derivative at $1-s$ give $D_a(s)=O(\log(|\Im s|+2))$. The integral there is $O(x^{1/2})$. The shift may be made along heights tending to infinity and separated by $\gg1/\log T$ from all nearby ordinates, by the local zero count $O(\log T)$ for this fixed finite family. The standard partial fraction expansion then gives $O(\log^2 T)$ for the logarithmic derivatives along those horizontal segments. Their integrals tend to zero. This proves the expansion for $M_a$.

To replace prime powers by primes, the $11^j$ terms cost $O(x\log x)$. Powers $p^k\le x$ with $k\ge3$ cost $O(x^{4/3}\log^2(2x))$, by counting bases up to $x^{1/3}$ and exponents up to $\log_2 x$. The square contribution is

$$
10\int_2^x\sum_{r^2\equiv a\bmod 11}\theta(\sqrt t;11,r)\thinspace dt
   =\frac23 C_a x^{3/2}+o(x^{3/2}),
$$

by the prime number theorem in each fixed reduced progression. Here $\theta(y;11,r)$ sums $\log p$ over the primes in that class up to $y$. Thus
$T(x)=\int_2^x(10\theta(t;11,a)-t)\thinspace dt$ satisfies $T(x)=x^{3/2}F_a(\log x)+o(x^{3/2})$ and $T(x)=O(x^{3/2})$.

For the final change of weights let $B(t)=10\theta(t;11,a)-t$. Partial summation gives
$10\pi(t;11,a)-\mathrm{li}(t)=B(t)/\log t+\int_2^t B(v)/(v\log^2 v)\thinspace dv+O(1)$, with constant depending only on the convention for $\mathrm{li}$. Integrating the first term gives $T(x)/\log x+O(x^{3/2}/\log^2 x)$ by integration by parts. The double integral is
$\int_2^x (x-v)T'(v)/(v\log^2 v)\thinspace dv$. Integrating by parts once more and using $T(2)=0$ bounds it by $O(x\int_2^x v^{-1/2}/\log^2 v\thinspace dv)=O(x^{3/2}/\log^2 x)$. This proves the claim. Changing Johnston's lower endpoint from zero to two adds a fixed constant. Changing the additive convention for $\mathrm{li}$ costs $O(x)$. Both disappear in the normalized limit.

## 2. Certifying the contribution of the zeros

The data give 850 disjoint positive-ordinate brackets, disjoint within each character. Each bracket has the form $[n/d,(n+1)/d]$ with $d=402653184$. Character labels are Conrey labels $1,\ldots,10$. Equivalently, for $l=2^k\bmod 11$ define $\chi_l(2^j)=\exp(2\pi i k j/10)$. For the principal label the zeros are those of $\zeta$. Both programs check every bracket from its endpoints. The input need only contain a subset of the zeros. For example, the quadratic character (label 10) has certified Hardy sign changes in $(106.69829648,106.69829649)$ and $(106.99570265,106.99570266)$, both disjoint from the selected brackets. The mass bound covers these zeros along with the rest of the omitted contribution. [Endpoint check](crosscheck.py)

Put $s=1/2+it$, let $f$ be the primitive conductor and let $\kappa$ be the parity. By the functional equation the completed value $(f/\pi)^{(s+\kappa)/2}\Gamma((s+\kappa)/2)L(s,\chi^\ast)$ lies on a fixed line through the origin as $t$ varies. Rotating it by the conjugate of a nonzero central value puts it on the real axis up to a positive factor. Opposite strict signs at the endpoints therefore certify at least one zero. Select one zero per bracket and include its conjugate in the conjugate character. The disjointness within each character and the signs of the ordinates prevent double counting.

For a retained positive ordinate $\gamma$ for $\chi^\ast$, the conjugate-pair contribution to (1) is

$$
-2\Re\frac{\overline{\chi(a)}e^{iu\gamma}}
                 {(1/2+i\gamma)(3/2+i\gamma)}.
\tag{2}
$$

Every operation in the numerical inequalities uses outward-rounded Arb balls, including evaluation over the entire bracket. Here is the unconditional upper bound that makes the cancellation case sufficient. Put
$H(s)=s(s-1)\prod_\chi (f_\chi/\pi)^{(s+\kappa_\chi)/2}\Gamma((s+\kappa_\chi)/2)L(s,\chi^\ast)$.
This entire function has order one and its zeros are precisely the nontrivial zeros with multiplicity. Its functional equation is symmetric up to sign about $1/2$. In $z=s-1/2$, pair zeros $w=\rho-1/2$ and $-w$ in its Hadamard product to obtain factors $1-z^2/w^2$, plus a power of $z$ for central zeros. The possible exponential $e^{bz}$ has $b=0$ by the symmetry. Taking the real logarithmic derivative at a real $\sigma\ge1$ gives

$$
\frac{H'(\sigma)}{H(\sigma)}
  =\sum_{\chi,\rho}\Re\frac{1}{\sigma-\rho}
  \ \ge\sum_{\chi,\ \Re\rho=1/2}
       \frac{\sigma-1/2}{(\sigma-1/2)^2+\gamma^2}.
\tag{3}
$$

Here the left sum includes **all** zeros. Each real part is positive since every nontrivial zero has real part less than one. These real parts are absolutely summable by the zero count, and $H$ is nonzero at one after pole removal. This argument bounds the critical-line terms even if there are off-line zeros.

At $\sigma=1$ write $V=2H'(1)/H(1)$. The zeta contribution is $2+\gamma_E-\log(4\pi)$, by the logarithmic derivative of the completed zeta function at one. For each of the nine nonprincipal characters the contribution is

$$
\log(11/\pi)-\gamma_E-(1+\chi(-1))\log2
      +2\Re\bigl(L'(1,\chi)/L(1,\chi)\bigr).
$$

Under GRH this recovers the zero-mass identity in Lemma 3.5 of Fiorilli and Martin. Formula (3) supplies the upper bound required here without GRH. Because $|\rho+1|\ge|\rho|$, the error in (1) after the selected pairs is at most $V-2\sum_{\rm sele{}cted}(1/4+\gamma^2)^{-1}$. This bounds every remaining term of the critical-line profile, including unselected multiplicities and skipped ordinates at any height. The first computation gives a remainder less than $0.154$. It evaluates the logarithmic derivatives with Taylor coefficients at one. [Fiorilli and Martin, Lemma 3.5](https://arxiv.org/pdf/0912.4908#page=27)

Each row below gives a certified upper bound at the first time and a certified lower bound at the second. These are values of the limiting profile $F_a(u)$, including the entire remainder. In particular, $u=0$ is a legitimate argument of the profile. Section 3 explains why it gives information about arbitrarily large $x$.

| $a$ | $u_-$ | $F_a(u_-)<$ | $u_+$ | $F_a(u_+)>$ |
|---:|---:|---:|---:|---:|
| 1 | 1609 | −3.202 | 0 | 1.342 |
| 2 | 668.75 | −1.684 | 2248 | 1.700 |
| 3 | 275 | −3.006 | 1742.5 | 0.275 |
| 4 | 835.5 | −3.060 | 1123.5 | 0.324 |
| 5 | 500.5 | −3.004 | 2457.5 | 0.327 |
| 6 | 747.75 | −1.700 | 2123.5 | 1.731 |
| 7 | 588.25 | −1.666 | 401.5 | 1.656 |
| 8 | 2594.5 | −1.732 | 183.25 | 1.607 |
| 9 | $\log31$ | −2.181 | $\log21000$ | 0.346 |
| 10 | 2632.25 | −1.711 | 2425.75 | 1.570 |

## 3. From one witness to arbitrarily large inputs

Fix $a$ and $\epsilon>0$. Truncate (1) with uniform error below $\epsilon/4$. For the resulting finite set of ordinates $\gamma_j$, the closure of $u\mapsto (e^{iu\gamma_j})_j$ is a compact subgroup of a torus. Visits to a sufficiently small neighbourhood of the identity have bounded gaps. Indeed, finitely many translates of the neighbourhood by orbit points cover the closure. For every time $t$, some $t-t_j$ is a return, with the $t_j$ in a fixed bounded set. At these returns $\tau$, the finite sum changes by less than $\epsilon/2$ uniformly in $u$. Hence $\sup_u|F_a(u+\tau)-F_a(u)|<\epsilon$.

At either witness in the table, uniform continuity gives a small interval with a strict margin over the claimed threshold in the appropriate direction. Choose $\epsilon$ less than half that margin. Translations by the returns above reproduce such intervals, with a fixed positive length and bounded gaps. The $o(1)$ in section 1 absorbs the remaining margin at sufficiently large $u$. In the cancellation case this proves both strict bounds on the limiting extrema (retain a smaller positive margin), and a positive lower proportion of time on each side in the $u$ coordinate. Since $du=dx/x$, this proportion is positive lower logarithmic density in $x$. Explicitly, for either excursion set $S$ the assertion is $\liminf_{X\to\infty}(\log X)^{-1}\int_{S\cap[2,X]}dx/x>0$.

## 4. A surviving off-line pole forces both signs

We first exclude all real zeros in $(1/2,1)$ for this family. For $\zeta(s)$ this follows from the positive alternating eta series and $1-2^{1-s}<0$. For each nonprincipal $\chi\bmod 11$, the sums $S(t)=\sum_{n\le t}\chi(n)$ have modulus at most 10 by periodicity. Integration by parts gives $L(s,\chi)=s\int_1^\infty S(t)t^{-s-1}\thinspace dt$ for real $s>0$. Differentiating under the integral gives $|L'(s,\chi)|\le20/s\le40$ on $[1/2,1]$. Truncating the Dirichlet series at $N=11000$, a multiple of 11, gives error at most $10/\sqrt{N}$ there since $S(N)=0$.

Use the 64 midpoints $s_j=1/2+(2j+1)/256$ for $0\le j<64$. Direct interval evaluation of the finite sums gives for each of the nine characters and each midpoint

$$
\Re\sum_{n\le N}\chi(n)n^{-s_j}
      -10/\sqrt N-40/256>1/20 .
$$

Every point of $[1/2,1]$ is within $1/256$ of a midpoint. Hence $\Re L(s,\chi)>1/20$ on this entire closed interval. The checker uses cosines of rational multiples of $2\pi$ for the real parts of the character values. This finite assertion also follows, as far as nonvanishing is concerned, from Platt's verified low-height zero count. [Finite-sum check](real_axis.py) · [Platt, Theorem 7.1](https://arxiv.org/abs/1305.3087)

Now suppose $D_a$ has a pole $\rho$ with $\beta=\Re\rho>1/2$. It is nonreal by the preceding paragraph. Fix a real $r$ with $1/2<r<\beta$. We show there are arbitrarily large $x$ with $A_{11,a}(x)>x^{1+r}$ and arbitrarily large $x$ with $A_{11,a}(x)<-x^{1+r}$.

For $\Re s>1$, define $P_a(s)=10\sum_{p\equiv a\bmod 11}p^{-s}$, $J(s)=\int_2^\infty t^{-s}/\log t\thinspace dt$ and $G_a(s)=s(s+1)\int_2^\infty A_{11,a}(x)x^{-s-2}\thinspace dx$. Integrating the prime count and the logarithmic integral separately gives

$$
G_a(s)=P_a(s)-J(s)-\mathrm{li}(2)2^{-s}.
$$

Euler products give $\sum_\chi\overline{\chi(a)}\log L(s,\chi^\ast)=P_a(s)+B_a(s)$ where $B_a$ extends holomorphically to $\Re s>1/2$. Its terms are the single correction $11^{-s}$ and the absolutely locally uniformly convergent prime powers of degree at least two. Since $J'(s)=-2^{1-s}/(s-1)$, a meromorphic continuation of the derivative is

$$
G_a'(s)=-D_a(s)-B_a'(s)+\frac{2^{1-s}}{s-1}
             +(\log2)\mathrm{li}(2)2^{-s}.
\tag{4}
$$

The residue $+1$ of $D_a$ at one cancels in (4). At every other real point $s>1/2$ the derivative is regular by the real zero exclusion and the Euler products. The original branch of $G_a$, and hence the Mellin transform of the integral error, therefore continues holomorphically along the whole real interval $(1/2,\infty)$. At the nonreal point $\rho$ the right side of (4) has a nonzero residue.

If either $A_{11,a}(x)\le x^{1+r}$ or $A_{11,a}(x)\ge-x^{1+r}$ eventually, choose the sign so that $h(x)=x^{1+r}\mp A_{11,a}(x)$ is nonnegative for $x$ beyond a fixed $X$. Its Mellin transform $\int_X^\infty h(x)x^{-s-2}\thinspace dx$ converges for $\Re s>1$. It continues along the real interval $(r,\infty)$ by the preceding identity, since the transform of $x^{1+r}$ has its only pole at $r$, and changing a finite lower limit adds an entire function. Landau's theorem for nonnegative Mellin transforms implies an abscissa of convergence at most $r$. Indeed a finite abscissa must be a singularity on the real axis. The elementary reason is that the Taylor expansion about a point to its right, evaluated to the left, has nonnegative moment terms and can be integrated term by term by monotone convergence.

The transform of $h$ is thus holomorphic on $\Re s>r$. Combining it with the elementary power transform, with the corresponding sign, and adding back the bounded-interval contribution would make $G_a$ single-valued and holomorphic on that half-plane. Its derivative cannot then have the pole exhibited in (4), a contradiction. This proves both asserted excursions. In this case $\limsup E_{11,a}=+\infty$ and $\liminf E_{11,a}=-\infty$. The argument makes no density assertion in this case.

The two cases exhaust every residue class. For $b$ reduced modulo $22$, let $a\equiv b\bmod 11$. Their lists of odd primes coincide. The only possible discrepancy is the prime two, present in the class $a=2$ modulo 11. As $\varphi(22)=\varphi(11)=10$,
$A_{22,b}(x)=A_{11,a}(x)-10\thinspace1_{a=2}(x-2)$ for $x\ge2$. The difference of the normalized errors tends to zero. The strict margins transfer the bounds to modulus 22 in both cases, and the density conclusion whenever it holds in the cancellation case.

## 5. A second bound using primes

The second program constructs each character from the generator 2 and evaluates its $L$-function at bracket endpoints as

$$
L(s,\chi)=11^{-s}\sum_{r=1}^{10}\chi(r)\zeta(s,r/11)
$$

for nonprincipal $\chi$. It uses the real part of the product of one completed endpoint and the conjugate of the other to test their signs on the fixed line. It evaluates (2) by real sines and cosines, and bounds the remainder by a different positive series.

Put $\eta=\sqrt{3}/2$, $\sigma=1/2+\eta$. For real $t$,
$(t^2+\eta^2)^2\le(t^2+1/4)(t^2+9/4)$. Thus $\sum_{\rm omitted}(\eta^2+\gamma^2)^{-1}$ also bounds the missing terms. Applying (3) with this $\sigma$ gives

$$
\sum_{\chi,\ \Re\rho=1/2}\frac{1}{\eta^2+\gamma^2}
     \le \frac{H'(\sigma)}{\eta H(\sigma)} .
$$

There are five even and five odd factors. Write $\psi_0=\Gamma'/\Gamma$. Orthogonality at $a=1$ and the Euler products at $\sigma>1$ give

$$
\frac{H'(\sigma)}{H(\sigma)}
=\frac1\sigma+\frac1{\sigma-1}
+\frac{9\log11-10\log\pi+5\psi_0(\sigma/2)+5\psi_0((\sigma+1)/2)}2
-\frac{\log11}{11^\sigma-1}
-10\sum_{n\equiv1\bmod 11}\frac{\Lambda(n)}{n^\sigma}.
$$

Omitting the terms $n>2{,}000{,}000$ gives an upper bound. After subtracting the selected-pair mass the bound is below $0.170$. All twenty inequalities pass again. Both implementations use FLINT's ball arithmetic. They differ in the representation of the characters, the endpoint tests, the trigonometric computation, and the analytic bound for all missing zeros.

## 6. A prime-side check for class 9

In the cancellation case for class 9, including under GRH, there is also an exact check of two values of $F_9$ that uses no zero ordinates. Take $a=9$ and $b=5$, so $ab=1\bmod11$. Since $a\ne\pm1\bmod11$, the weighted sums of the even characters and of the odd characters vanish separately. Applying the primitive functional equations in $D_a$ therefore cancels both digamma terms. The weighted log-conductor sum is $-\log11$. This gives $D_a(s)+D_b(1-s)=-\log11$ as meromorphic functions. Put $c_b=\lim_{z\to1}(D_b(z)-1/(z-1))$.

At $s=0$ we have $D_a(s)=1/s-\log11-c_b+O(s)$. The zero residue of the Mellin integrand for $M_a(v)$ is consequently $v(\log v-1-\log11-c_b)$. On the left line insert $D_a(s)=-\log11-D_b(1-s)$, where the series for the dual logarithmic derivative converges absolutely. For $z>1$ the Mellin integral of $z^s/[s(s+1)]$ on $\Re s=-1/2$ equals $-1/z$, by closing to the left. The left-line contribution to $M_a(v)$ is therefore $\log11+D_b(2)$. Combining the residues with (1) gives, for $v>1$,

$$
F_9(\log v)=
\frac{M_9(v)-v^2/2-v(\log v-1-\log11-c_5)-\log11-D_5(2)}
     {v^{3/2}}-\frac43 .
$$

Here $M_9(v)$ is just a finite prime-power sum. The constants are computed at one and two. In particular $c_5=-\gamma_E-\sum_{\chi\ne1}\overline{\chi(5)}L'(1,\chi)/L(1,\chi)$. Evaluation gives $-2.353<F_9(\log31)<-2.352$ and $0.4974<F_9(\log21000)<0.4976$. Both results also lie inside the enclosures obtained from the zeros.

### Class-one witness

Under GRH let $H$ be the product of $\xi$ and the nine entire completed primitive Dirichlet functions for the nonprincipal characters modulo 11. Write $h=H'/H$. The nontrivial zeros of $H$, counted with multiplicity, are invariant under $\rho\mapsto1-\rho$. The difference of the Hadamard logarithmic derivatives gives $h(1)-h(2)=\sum_\rho [(1-\rho)^{-1}-(2-\rho)^{-1}]=\sum_\rho 1/[\rho(\rho+1)]$. The differences converge absolutely, since each summand is $O(|\rho|^{-2})$. For class 1 all character weights are one and there are two square roots of 1. Its square term is therefore $-(2/3)2=-4/3$. The limiting profile at time zero is $F_1(0)=-4/3-h(1)+h(2)$, strictly between 1.65147046110676 and 1.65147046110677. This calculation uses no tabulated ordinates. Uniform almost periodicity gives arbitrarily late returns as close to this value as desired. [Arithmetic witness](crosscheck.py)

The normalised prime integral at a finite input can have a different sign from its limiting profile. At $x=21000$ one has $-0.264084655513<E_{11,9}(x)<-0.264084655512$, while $F_9(\log x)$ is about $0.49748568637794$. The verifier evaluates the integral of the prime count as $10\sum_{p<x,\,p\equiv9\bmod11}(x-p)$ and subtracts the change in $t\,\mathrm{li}(t)-\mathrm{li}(t^2)$ from 2 to $x$. [Verification output](evidence/hurwitz-160.txt)

## 7. Relation to earlier work

Daniel R. Johnston posed the all-moduli eventual-negativity classification at the 2024 Comparative Prime Number Theory Symposium. His earlier theorem concerns the ordinary prime-counting function. For the progression problem the stated hypothesis is GRH. [Problem 23, p. 9](https://arxiv.org/pdf/2407.03530#page=9) · [Johnston's original paper](https://doi.org/10.4153/S0008439522000212)

Tianyu Zhao's 2025 paper gives a table for equation (35) in the concluding section. Its integral equals $A_{q,a}/\varphi(q)$. The row for 11 lists $1,3,4,5,9$ and the row for 22 lists $1,3,5,9,15$ as eventually negative. Zhao's table is stated under GRH. The positive excursions above hold unconditionally, so in particular under GRH, and they contradict those two rows. This comparison addresses equation (35) and those specific entries. [Published paper, §8](https://doi.org/10.1007/s40993-025-00640-y) · [Equation (35) and Table 1](https://arxiv.org/html/2411.18903v2#S8)

Hudson and Bays used finite averages of the difference between two residue classes in 1977 (equations 2.1 and 2.2). Bays and Hudson examined finite-range averages of prime counts and relative orderings modulo 11. Hudson also studied averaged races between quadratic nonresidues and residues. Benli, Martin and Péringuey treat joint densities for the unintegrated Chebyshev function modulo 11. These are relevant precedents for smoothing or for the modulus. The present statements concern each individual integrated prime count against $\mathrm{li}/\varphi$ at unbounded inputs. The explicit formula, almost periodicity and zero-mass identity are established tools. The unconditional quantitative bounds for 11 and its odd lifts, and the positive lower logarithmic densities under GRH, are the contributions proposed here. [Hudson and Bays (1977)](https://eudml.org/doc/151935) · [Bays and Hudson (1983)](https://eudml.org/doc/152516) · [Hudson (1985)](https://doi.org/10.1090/S0025-5718-1985-0777286-7) · [Benli, Martin and Péringuey (2025)](https://arxiv.org/abs/2510.05427)

The checks recorded here are reproducible numerical certificates used in a written analytic proof. The work has not been peer reviewed. Searches by problem number, paper title, integrated and averaged prime-counting errors, and modulus found no earlier proof of the stated quantitative result. Priority remains open to further references.
