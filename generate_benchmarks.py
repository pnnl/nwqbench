#!/usr/bin/env python3
"""Entrypoint for the NWQBench Docker image: runs one or all of the
NWQ_Bench/<name>/<script>.py generators with a requested qubit/size
parameter and collects the resulting .qasm files.

Usage:
    python generate_benchmarks.py <benchmark|all> <n> [extra_args...]
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
BENCH_ROOT = REPO_ROOT / "NWQ_Bench"

# name -> script path relative to NWQ_Bench/
BENCHMARKS = {
    "adder": "adder/adder.py",
    "binary_welded_tree": "binary_welded_tree/binary_welded_tree.py",
    "boolean_satisfaction": "boolean_satisfaction/boolean_satisfaction.py",
    "bv": "bv/bv.py",
    "cat_state": "cat_state/cat_state.py",
    "cc": "cc/cc.py",
    "ghz_state": "ghz_state/ghz_state.py",
    "grover_search": "grover_search/grover_search.py",
    "hhl": "hhl/hhl.py",
    "ising": "ising/ising.py",
    "multiplier": "multiplier/multiplier.py",
    "n_statevector": "n_statevector/ry_statevector.py",
    "qec_5qubit_x": "qec_5qubit_x/qec_5qubit_x.py",
    "qec_9qubit_xyz": "qec_9qubit_xyz/qec_9qubit_xyz.py",
    "qft": "qft/qft.py",
    "qknn": "qknn/qknn.py",
    "qnn": "qnn/qnn.py",
    "qnn_qf": "qnn_qf/qnn_qf.py",
    "qsvm": "qsvm/qsvm_raw.py",
    "qugan": "qugan/qugan.py",
    "square_root": "square_root/square_root.py",
    "statevector_encoder": "statevector_encoder/state_generator.py",
    "swap_test": "swap_test/swap_test.py",
    "vqc": "vqc/vqc_raw.py",
    "vqe": "vqe/vqe.py",
    "w_state": "w_state/w_state.py",
}

# These generators ignore the qubit-count CLI argument and always emit a
# fixed-size circuit (hardcoded in the script itself).
FIXED_SIZE_BENCHMARKS = {"boolean_satisfaction", "grover_search", "statevector_encoder"}


def run_one(name: str, qubits: int, extra_args: list[str], output_dir: Path) -> bool:
    rel_script = BENCHMARKS[name]
    script_path = BENCH_ROOT / rel_script
    bench_dir = script_path.parent
    cmd = [sys.executable, script_path.name, str(qubits), *extra_args]

    note = " (ignores qubit arg, emits a fixed-size circuit)" if name in FIXED_SIZE_BENCHMARKS else ""
    print(f"\n=== {name}{note} ===")
    print(f"$ {' '.join(cmd)}   (cwd={bench_dir})")

    result = subprocess.run(cmd, cwd=bench_dir, capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode != 0:
        print(f"[{name}] FAILED (exit {result.returncode})", file=sys.stderr)
        if result.stderr.strip():
            print(result.stderr.strip(), file=sys.stderr)
        return False

    qasm_dir = bench_dir / "qasm"
    if qasm_dir.is_dir():
        dest = output_dir / name
        dest.mkdir(parents=True, exist_ok=True)
        copied = []
        for f in qasm_dir.glob("*.qasm"):
            shutil.copy2(f, dest / f.name)
            copied.append(f.name)
        if copied:
            print(f"[{name}] wrote: {', '.join(copied)} -> {dest}")
        else:
            print(f"[{name}] OK, but no .qasm files were found in {qasm_dir}")
    else:
        print(f"[{name}] OK, but no qasm/ directory was produced in {bench_dir}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate NWQBench QASM benchmark circuits.",
    )
    parser.add_argument(
        "benchmark",
        help=f"Benchmark name, or 'all'. Available: {', '.join(sorted(BENCHMARKS))}",
    )
    parser.add_argument("qubits", type=int, help="Qubit/size parameter passed to the generator")
    parser.add_argument(
        "extra_args",
        nargs="*",
        help="Extra positional args for generators needing more than one parameter (e.g. qnn_qf takes n k depth)",
    )
    parser.add_argument(
        "--output-dir",
        default=os.environ.get("OUTPUT_DIR", "/output"),
        help="Where generated .qasm files are collected (default: $OUTPUT_DIR or /output)",
    )
    args = parser.parse_args()

    if args.benchmark == "all":
        names = sorted(BENCHMARKS)
    elif args.benchmark in BENCHMARKS:
        names = [args.benchmark]
    else:
        parser.error(f"unknown benchmark '{args.benchmark}'. Available: {', '.join(sorted(BENCHMARKS))}")
        return

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {name: run_one(name, args.qubits, args.extra_args, output_dir) for name in names}

    print("\n=== Summary ===")
    for name, ok in results.items():
        print(f"{name}: {'OK' if ok else 'FAILED'}")

    if not all(results.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
