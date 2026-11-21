"""Run inside 'lake env' for Mathlib v4.33.1, with the upstream source directory."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile

STATEMENTS_SHA256 = "79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("upstream", type=Path, help="directory containing the pinned Statements.lean")
    args = parser.parse_args()
    interface = args.upstream.resolve() / "Statements.lean"
    if hashlib.sha256(interface.read_bytes()).hexdigest() != STATEMENTS_SHA256:
        raise ValueError("upstream statement file does not match the published source")
    version = subprocess.check_output(["lean", "--version"], text=True)
    if "version 4.33.1," not in version:
        raise ValueError("expected Lean 4.33.1")
    print("Lean 4.33.1", flush=True)
    print("Statements.lean SHA-256: " + STATEMENTS_SHA256, flush=True)
    local = Path(__file__).resolve().with_name("Oscillation.lean")
    with tempfile.TemporaryDirectory() as directory:
        build = Path(directory)
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join([directory, env.get("LEAN_PATH", "")])
        for source in (interface, local):
            subprocess.run(["lean", "-DautoImplicit=false", "-R", str(source.parent),
                            "-o", str(build / (source.stem + ".olean")), str(source)],
                           cwd=source.parent, env=env, check=True)
        subprocess.run(["leanchecker", "-v", "Statements", "Oscillation"],
                       cwd=build, env=env, check=True)
    print("Both modules passed kernel replay.")


if __name__ == "__main__":
    main()
