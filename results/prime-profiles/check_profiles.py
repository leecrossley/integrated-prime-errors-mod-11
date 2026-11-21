"""Replay the prime-side witnesses and check the two continuous-scan certificates."""
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


STUDY = Path(__file__).resolve().parent
DATA = STUDY / "data"
LIMITS = (2_000_000, 200_000_000, 10_000_000_000, 100_000_000_000, 1_000_000_000_000)


def run(program, *args):
    subprocess.run([sys.executable, "-B", str(STUDY / program), *map(str, args)], check=True)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_scan_chain(bits, temp, full):
    source = DATA / "prime-10009-128.json"
    initial = json.loads(source.read_bytes())["scan"]
    remaining = set(initial["missing_positive"])
    require(len(remaining) == 227, "unexpected initial set")
    classes_by_stage = []
    count = 0
    for limit in LIMITS:
        suffix = "-160" if bits == 160 else ""
        recorded = DATA / f"continuous-{limit}{suffix}.json"
        stage = json.loads(recorded.read_bytes())
        require(stage["bits"] == bits and stage["prime"] == 10009 and stage["limit"] == limit,
                f"wrong parameters at {limit}")
        require(stage["input_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest(),
                f"wrong input at {limit}")
        positive = {int(a): (v["direction"], v["numerator"], v["denominator"])
                    for a, v in stage["positive"].items()}
        negative = set(stage["negative_throughout"])
        require(stage["classes_tested"] == len(remaining)
                and len(negative) == len(stage["negative_throughout"])
                and positive.keys().isdisjoint(negative)
                and set(positive) | negative == remaining, f"incomplete classes at {limit}")
        if full:
            generated = temp / f"continuous-{limit}-{bits}.json"
            run("combined_primes.py", source, generated, "--limit", limit, "--bits", bits)
            require(generated.read_bytes() == recorded.read_bytes(), f"scan mismatch at {limit}")
        classes_by_stage.append((positive, negative))
        count += stage["intervals_checked"]
        remaining = negative
        source = recorded
    require(remaining == {148, 9100} and count == 18_578_682, "unexpected final coverage")
    return classes_by_stage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true", help="recompute every continuous interval")
    args = parser.parse_args()
    if not __debug__:
        parser.error("run without -O so the numerical checks are active")
    run("check_uniform_bounds.py")
    run("check_multi_examples.py")
    brackets = STUDY.parents[1] / "zero-brackets.json"
    saved_grid = json.loads((DATA / "prime-10009-128.json").read_bytes())
    with tempfile.TemporaryDirectory() as temporary:
        temp = Path(temporary)
        for bits in (128, 160):
            grid = temp / f"grid-{bits}.json"
            run("verify_prime_side.py", "--brackets", brackets, "--bits", bits, "--output", grid)
            require(json.loads(grid.read_bytes()) == dict(saved_grid, bits=bits),
                    f"grid mismatch at {bits} bits")
        lower = check_scan_chain(128, temp, args.full)
        higher = check_scan_chain(160, temp, args.full)
        require(lower == higher, "dyadic witnesses or remaining classes disagree")
    print("All five stages agree on every dyadic witness. Final classes: 148 and 9100.")
    print("18,578,682 intervals per precision.")
    if args.full:
        print("Every scan was regenerated and matched its recorded output byte for byte.")


if __name__ == "__main__":
    main()
