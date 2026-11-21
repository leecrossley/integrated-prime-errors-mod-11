"""Run inside 'lake env' for Mathlib v4.33.1, with the upstream source directory."""
import argparse
import hashlib
import os
import re
from pathlib import Path
import subprocess
import tempfile

STATEMENTS_SHA256 = "79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf"


MATHLIB_COMMIT = "0df444a360eaa60ab8c11dca51a86af692955474"
LEAN_COMMIT = "819816b2e0a3bf405af45ae5c7af2491d8f5bee6"
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
THEOREMS = ("IntegratedPrimeErrors.noRealZero", "IntegratedPrimeErrors.thirdMomentExtrema")


def check_axioms(output):
    for theorem in THEOREMS:
        reports = re.findall(r"'" + re.escape(theorem) + r"' depends on axioms:\s*\[([^\]]*)\]", output)
        if len(reports) != 1 or {name.strip() for name in reports[0].split(",")} != AXIOMS:
            raise ValueError(f"Unexpected axiom report for {theorem}:\n{output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("upstream", type=Path, help="directory containing the pinned Statements.lean")
    args = parser.parse_args()
    interface = args.upstream.resolve() / "Statements.lean"
    if hashlib.sha256(interface.read_bytes()).hexdigest() != STATEMENTS_SHA256:
        raise ValueError("upstream statement file does not match the published source")
    version = subprocess.check_output(["lean", "--version"], text=True)
    if LEAN_COMMIT not in version:
        raise ValueError("expected Lean 4.33.1")
    if not Path("Mathlib.lean").is_file():
        raise ValueError("run from the pinned Mathlib checkout using lake env")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    if revision != MATHLIB_COMMIT:
        raise ValueError(f"Unexpected Mathlib revision: {revision}")
    print("Lean 4.33.1", flush=True)
    print("Mathlib commit: " + revision, flush=True)
    print("Statements.lean SHA-256: " + STATEMENTS_SHA256, flush=True)
    local = Path(__file__).resolve().with_name("Oscillation.lean")
    with tempfile.TemporaryDirectory() as directory:
        build = Path(directory)
        env = os.environ.copy()
        paths = [str(Path(entry).resolve()) for entry in env.get("LEAN_PATH", "").split(os.pathsep) if entry]
        env["LEAN_PATH"] = os.pathsep.join([directory, *paths])
        for source in (interface, local):
            compiled = subprocess.run(["lean", "-DautoImplicit=false", "-DwarningAsError=true",
                                       "-R", str(source.parent), "-o", str(build / (source.stem + ".olean")),
                                       str(source)], cwd=source.parent, env=env, check=True,
                                      stdout=subprocess.PIPE, text=True)
            print(compiled.stdout, end="", flush=True)
            if source == local:
                check_axioms(compiled.stdout)
        subprocess.run(["leanchecker", "-v", "Statements", "Oscillation"],
                       cwd=build, env=env, check=True)
    print("Both modules passed kernel replay.")


if __name__ == "__main__":
    main()
