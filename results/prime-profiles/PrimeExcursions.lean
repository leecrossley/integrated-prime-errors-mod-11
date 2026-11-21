import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace PrimeExcursions

/-- Exact threshold for one weighted prime to exceed the Riesz main term. -/
theorem single_prime_threshold {p w : ℝ} (hp : 0 < p) :
    (∃ y : ℝ, p ≤ y ∧ y ^ 2 / 2 < w * (y - p)) ↔ 2 * p < w := by
  constructor
  · rintro ⟨y, hy, hw⟩
    by_contra! h
    nlinarith [mul_le_mul_of_nonneg_right h (sub_nonneg.mpr hy), sq_nonneg (y - 2*p)]
  · intro h
    refine ⟨2*p, by linarith, ?_⟩
    nlinarith [mul_lt_mul_of_pos_right h hp]

private theorem four_dvd_of_dvd_pow_two {d m : ℕ} (hd : 2 < d) (h : d ∣ 2^m) :
    4 ∣ d := by
  obtain ⟨j, _, rfl⟩ := (Nat.dvd_prime_pow Nat.prime_two).1 h
  match j with
  | 0 => norm_num at hd
  | 1 => norm_num at hd
  | j + 2 => exact ⟨2^j, by ring⟩

private theorem nine_pow_mod_eight (j : ℕ) : 9^j % 8 = 1 := by
  induction j with
  | zero => decide
  | succ j ih => rw [pow_succ, Nat.mul_mod, ih]

/-- The two later progression terms cannot simultaneously be prime powers
of the required bases in the class-two case. -/
theorem no_paired_powers {q m k : ℕ} (hq : 11 ≤ q)
    (h2 : q + 1 = 2^m) (h3 : q + 2 = 3^k) : False := by
  have hm : 3 ≤ m := by
    match m with
    | 0 | 1 | 2 =>
      norm_num at h2
      omega
    | _ + 3 => omega
  obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le hm
  have hpow : 2^m = 8 * 2^r := by rw [hr, pow_add]; norm_num
  have hmod : 3^k % 8 = 1 := by omega
  let j := k / 2
  have hk : k = j*2 := by
    have hcases : k = j*2 ∨ k = 2*j+1 := by dsimp [j]; omega
    rcases hcases with even | odd
    · exact even
    · have hodd : 3^k % 8 = 3 := by
        rw [odd, pow_succ, pow_mul, Nat.mul_mod]
        norm_num only [Nat.reducePow]
        rw [nine_pow_mod_eight]
      omega
  let z := 3^j
  have hs : 3^k = z*z := by rw [hk, pow_mul, pow_two]
  have hz : 4 ≤ z := by
    by_contra! small
    have hle : z ≤ 3 := by omega
    have := Nat.mul_le_mul hle hle
    omega
  obtain ⟨u, hu⟩ := Nat.exists_eq_add_of_le hz
  have hprod : (u+3)*(u+5) = 2^m := by rw [hu] at hs; nlinarith
  have left : u+3 ∣ 2^m := by rw [← hprod]; exact dvd_mul_right _ _
  have right : u+5 ∣ 2^m := by rw [← hprod]; exact dvd_mul_left _ _
  have hleft := four_dvd_of_dvd_pow_two (by omega) left
  have hright := four_dvd_of_dvd_pow_two (by omega) right
  omega

/-- For a higher power of two in an odd prime progression, the term at 2q+a
is twice an odd integer greater than one. -/
theorem later_term_not_power_two {q j m : ℕ} (hq : 11 ≤ q)
    (odd : q % 2 = 1) (hj : 2 ≤ j) : 2*q + 2^j ≠ 2^m := by
  intro h
  obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le hj
  have ha : 2^j = 4*2^r := by rw [hr, pow_add]; norm_num
  have hd : 2*q + 2^j ∣ 2^m := by rw [h]
  have hfour := four_dvd_of_dvd_pow_two (by omega) hd
  omega

#print axioms single_prime_threshold
#print axioms no_paired_powers
#print axioms later_term_not_power_two

end PrimeExcursions
