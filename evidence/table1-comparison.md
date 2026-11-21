# Zhao’s Table 1

Under GRH, a calculation retaining the prime-square coefficient from Zhao’s equation (33) reproduces all 63 pairs printed in Table 1. For moduli 2 through 120 it gives one further pair, $(6,1)$. Equation (35) has a different prime-square coefficient. For moduli 11 and 22, the difference decides which side of the test the five printed classes fall on. The public notebooks implement Theorems 3 and 4. The program used for Table 1 would establish how Zhao obtained the entries. [Equations (33) and (35)](https://arxiv.org/html/2411.18903v2#S7) [Table 1](https://arxiv.org/html/2411.18903v2#S8.T1) [Published notebooks](https://github.com/skyfishzhao/RH-and-Mertens-Theorems/tree/b040d47f1d1c0541701c089d0de76fdbd2604102)

## Prime squares

Let $C(q,a)$ count the square roots of the reduced class $a$ modulo $q$. After multiplying the prime count by the totient, the integral of its prime-square contribution has leading term $-C(q,a)\int_2^X\sqrt t/\log t\thinspace dt$. Its coefficient after multiplication by $\log X/X^{3/2}$ is $-2C(q,a)/3$. Section 7 uses the magnitude $2C(q,a)$ for a different integral.

For a nontrivial zero $\rho=1/2+i\gamma$ of a primitive factor inducing a character modulo $q$, the absolute coefficient of the oscillating term in equation (35), in the same normalisation, is $1/|\rho(\rho+1)|$. Write $S(q)$ for the sum of these coefficients, counting every zero of each factor with multiplicity. The triangle inequality proves eventual negativity if $S(q)<2C(q,a)/3$. Failure of this sufficient test leaves the sign open. For 11 and 22 the separate signed witnesses in the proof establish positive excursions at arbitrarily late inputs. [Signed witnesses](../PROOF.md#class-one-witness)

## Zero sum

Let $H$ be the product of the completed primitive factors, using the entire Riemann xi function for the principal character. Pairing zeros in the Hadamard product about $1/2$ gives, for $x>0$ under GRH,

~~~math
K_q(x)=\frac{H'(1/2+x)}{xH(1/2+x)}
      =\sum_{\chi\bmod q}\sum_{\gamma_\chi}\frac{1}{x^2+\gamma_\chi^2}.
~~~

The product includes the primitive factor associated with each character modulo $q$. A central zero contributes its multiplicity divided by $x^2$. To evaluate the full absolute sum, put $x(\theta)^2=1/4+2\sin^2\theta$. Substituting $u=\tan\theta$ in the integral for each ordinate gives

~~~math
\frac{2}{\pi}\int_0^{\pi/2}\frac{d\theta}{x(\theta)^2+\gamma^2}
=\frac{1}{\sqrt{(\gamma^2+1/4)(\gamma^2+9/4)}}.
~~~

All summands are positive, so the same integral of $K_q$ gives $S(q)$. Its integrand decreases on the interval. Left and right endpoint sums on equal subdivisions enclose the answer. The program uses interval arithmetic for the logarithmic derivatives and refines the subdivision until both comparisons are strict. [Completed product](../PROOF.md) [Replay script](table1_threshold.py)

## Comparison

Both 11 and 22 give $3.77<S(q)<3.78$. Their square classes have two roots each, so the earlier threshold is $4$ and the threshold for the prime integral is $4/3$. The square classes are 1, 3, 4, 5 and 9 modulo 11 and 1, 3, 5, 9 and 15 modulo 22.

Running the earlier-threshold comparison for every reduced class through modulus 120 gives precisely the printed square classes at all 27 listed moduli, plus $(6,1)$. Primes in class 1 modulo 3 are exactly those in class 1 modulo 6, and the two totients agree. With the coefficient from the prime integral, the absolute bound succeeds at the square classes of moduli 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24 and 30 in that range.

From the repository root, install the version of python-flint in the requirements file and run the following command. [Requirements](../requirements.txt)

~~~sh
python evidence/table1_threshold.py
~~~
