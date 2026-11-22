# Integrated prime-counting errors in progressions

The [original modulus-11 study](README.md) and [extension across prime moduli](range/PROOF.md) are maintained together. The extension has its own [paper through 10,007](range/paper.pdf), [certificate data](range/ordinates.tsv) and [replay instructions](README.md#reproduce-the-results).

| Result | Source revision | Publication | Reviews |
| --- | --- | --- | --- |
| [Integrated prime-counting errors for prime moduli](README.md) | [630ca6965f](https://github.com/leecrossley/integrated-prime-errors-mod-11/tree/630ca6965f98063a7d7fed6d8009223f7201bf33) | [Releases](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases) · [DOI](https://doi.org/10.5281/zenodo.24410803) | [Issues](https://github.com/leecrossley/integrated-prime-errors-mod-11/issues) · [PRs](https://github.com/leecrossley/integrated-prime-errors-mod-11/pulls) |

The finite certificate now includes prime 10,009. The [prime profiles and combined-prime tests](results/prime-profiles/) also give a positive proportion of sign-changing classes at every prime modulus under Dirichlet GRH, and, under the same hypothesis, an exact twelve-term test modulo 10,009. [Release and verification](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.2)

## Checking the collection

When a collection file changes, stage new paths with Git, then run `python3 tools/collection_manifest.py --write` to refresh `COLLECTION.sha256`.

Run `sh verify-collection.sh` from the repository root to check the collection files and the manifests for every result directory. The root manifest covers `range/`. The numerical CI job replays the modulus-11 checks and both range calculations through 10,009. Each result’s README gives its mathematical replay and environment requirements. [Contribution and publication guidance](AGENTS.md)

## Review discussions at import

GitHub shows the current status and subsequent replies at each original link. Review notes posted from the author’s account record checks made by or for the author. They are not independent referee reports.

- [integrated-prime-errors-mod-11 issue 4](https://github.com/leecrossley/integrated-prime-errors-mod-11/issues/4) — v2.0.0: state the status of Alpöge's GRH result, and make the Lean check enforce its axioms

## Edition DOIs

Each DOI identifies a fixed release. The final column identifies the archive with the proof files in this revision. A shared release can contain several papers. The collection as archived on 21 November 2026 is available at [10.5281/zenodo.24426575](https://doi.org/10.5281/zenodo.24426575).

| Result | Published release | Version DOI | Current proof files |
| --- | --- | --- | --- |
| [Integrated prime-counting errors for prime moduli](https://github.com/leecrossley/integrated-prime-errors-mod-11/blob/42e0a7ad31025f65f6def66bd4bcd9a446166d10/README.md) | [v2.0.0-archive](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.0.0-archive) | [10.5281/zenodo.24440125](https://doi.org/10.5281/zenodo.24440125) | [v2.0.0 proof files](https://github.com/leecrossley/integrated-prime-errors-mod-11/tree/42e0a7ad31025f65f6def66bd4bcd9a446166d10) |
| [Integrated prime-counting errors modulo 11 and 22](https://github.com/leecrossley/integrated-prime-errors-mod-11/blob/69ef7e85f5107f5b0a5283af2f87a914abda5356/README.md) | [v1.0.0-archive](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v1.0.0-archive) | [10.5281/zenodo.24440124](https://doi.org/10.5281/zenodo.24440124) | [v1.0.0 proof files](https://github.com/leecrossley/integrated-prime-errors-mod-11/tree/69ef7e85f5107f5b0a5283af2f87a914abda5356) ([Readable proof](https://github.com/leecrossley/integrated-prime-errors-mod-11/blob/42e0a7ad31025f65f6def66bd4bcd9a446166d10/PROOF.md)) |
| [Integrated prime-counting errors for prime moduli](README.md) | [v2.1.2](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.2) | [10.5281/zenodo.24442719](https://doi.org/10.5281/zenodo.24442719) | Same edition |
| [Sign changes in many residue classes](results/prime-profiles/README.md) | [v2.1.2](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.2) | [10.5281/zenodo.24442719](https://doi.org/10.5281/zenodo.24442719) | Same edition |
| [Integrated prime-counting errors for prime moduli](https://github.com/leecrossley/integrated-prime-errors-mod-11/blob/v2.1.1/README.md) | [v2.1.1](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.1) | [10.5281/zenodo.24425209](https://doi.org/10.5281/zenodo.24425209) | [10.5281/zenodo.24442719](https://doi.org/10.5281/zenodo.24442719) |
| [Sign changes in many residue classes](https://github.com/leecrossley/integrated-prime-errors-mod-11/blob/v2.1.1/results/prime-profiles/README.md) | [v2.1.1](https://github.com/leecrossley/integrated-prime-errors-mod-11/releases/tag/v2.1.1) | [10.5281/zenodo.24425209](https://doi.org/10.5281/zenodo.24425209) | [10.5281/zenodo.24442719](https://doi.org/10.5281/zenodo.24442719) |
