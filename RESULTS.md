# Integrated prime-counting errors in progressions

The [original modulus-11 study](README.md) and [extension across prime moduli](range/PROOF.md) are maintained together. The extension has its own [paper through 10,007](range/paper.pdf), [certificate data](range/ordinates.tsv) and [replay instructions](README.md#reproduce-the-results).

| Result | Source revision | Publication | Reviews |
| --- | --- | --- | --- |
| [Integrated prime-counting errors for prime moduli](README.md) | [630ca6965f](https://github.com/leecrossley/integrated-prime-errors-mod-11/tree/630ca6965f98063a7d7fed6d8009223f7201bf33) | [Releases](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases) · [DOI](https://doi.org/10.5281/zenodo.24410803) | [Issues](https://github.com/leecrossley/integrated-prime-errors-mod-11/issues) · [PRs](https://github.com/leecrossley/integrated-prime-errors-mod-11/pulls) |

The finite certificate now includes prime 10,009. The [prime profiles and combined-prime tests](results/prime-profiles/) also give a positive proportion of sign-changing classes at every prime modulus under Dirichlet GRH, and, under the same hypothesis, an exact twelve-term test modulo 10,009. [Release and verification](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.1)

## Checking the collection

Run `sh verify-collection.sh` from the repository root to check the result manifests. Each result’s README gives its mathematical replay and environment requirements. [Contribution and publication guidance](AGENTS.md)

## Review discussions at import

GitHub shows the current status and subsequent replies at each original link. Review notes posted from the author’s account record checks made by or for the author. They are not independent referee reports.

- [integrated-prime-errors-mod-11 issue 4](https://github.com/leecrossley/integrated-prime-errors-mod-11/issues/4) — v2.0.0: state the status of Alpöge's GRH result, and make the Lean check enforce its axioms

## Edition DOIs

Each DOI identifies a fixed release. The final column identifies the archive with the proof files in this revision. A shared release can contain several papers. The collection as archived on 21 November 2026 is available at [10.5281/zenodo.24426575](https://doi.org/10.5281/zenodo.24426575).

| Result | Published release | Version DOI | Current proof files |
| --- | --- | --- | --- |
| [Integrated prime-counting errors for prime moduli](README.md) | [v2.1.1](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.1) | [10.5281/zenodo.24425209](https://doi.org/10.5281/zenodo.24425209) | Same edition |
| [Sign changes in many residue classes](results/prime-profiles/README.md) | [v2.1.1](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.1) | [10.5281/zenodo.24425209](https://doi.org/10.5281/zenodo.24425209) | [10.5281/zenodo.24426575](https://doi.org/10.5281/zenodo.24426575) |
