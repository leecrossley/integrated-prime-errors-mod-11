import Statements

open Polynomial

namespace IntegratedPrimeErrors

/-- Specialize the right-half-plane theorem to real points in the open critical strip. -/
theorem noRealZero (nonvanishing : DirichletLNonvanishingRightOfHalf)
    {N : ℕ} [NeZero N] (χ : DirichletCharacter ℂ N) {s : ℝ}
    (lower : 1 / 2 < s) (upper : s < 1) : χ.LFunction (s : ℂ) ≠ 0 := by
  apply nonvanishing N χ (s : ℂ)
  · simpa using lower
  · right
    intro eq_one
    have h := congrArg Complex.re eq_one
    simp at h
    linarith

/-- A positive polynomial mean of variance r² and vanishing first and third
moments requires the supporting interval to extend at least r on either side. -/
theorem thirdMomentExtrema (mean : ℝ[X] →ₗ[ℝ] ℝ) {l u r : ℝ} (hr : 0 < r)
    (positive : ∀ p : ℝ[X], (∀ t ∈ Set.Icc l u, 0 ≤ p.eval t) → 0 ≤ mean p)
    (h0 : mean 1 = 1) (h1 : mean X = 0)
    (h2 : mean (X ^ 2) = r ^ 2) (h3 : mean (X ^ 3) = 0) :
    l ≤ -r ∧ r ≤ u := by
  let p : ℝ[X] := (u*r^2) • 1 + (2*u*r-r^2) • X + (u-2*r) • (X^2) - X^3
  let q : ℝ[X] := (-l*r^2) • 1 + (2*l*r+r^2) • X + (-l-2*r) • (X^2) + X^3
  have hp : 0 ≤ mean p := positive p (by
    intro t ht
    have eq : p.eval t = (u-t)*(t+r)^2 := by
      simp [p, Polynomial.eval_smul]
      ring
    exact eq ▸ mul_nonneg (sub_nonneg.mpr ht.2) (sq_nonneg _))
  have hq : 0 ≤ mean q := positive q (by
    intro t ht
    have eq : q.eval t = (t-l)*(t-r)^2 := by
      simp [q, Polynomial.eval_smul]
      ring
    exact eq ▸ mul_nonneg (sub_nonneg.mpr ht.1) (sq_nonneg _))
  simp [p, h0, h1, h2, h3] at hp
  simp [q, h0, h1, h2, h3] at hq
  have factor_pos : 0 < 2*r^2 := by positivity
  have upper : 0 ≤ (u-r)*(2*r^2) := by nlinarith only [hp]
  have lower : 0 ≤ (-r-l)*(2*r^2) := by nlinarith only [hq]
  exact ⟨sub_nonneg.mp ((mul_nonneg_iff_of_pos_right factor_pos).mp lower),
         sub_nonneg.mp ((mul_nonneg_iff_of_pos_right factor_pos).mp upper)⟩

end IntegratedPrimeErrors

#print axioms IntegratedPrimeErrors.noRealZero
#print axioms IntegratedPrimeErrors.thirdMomentExtrema
