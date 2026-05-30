#!/usr/bin/env python3
"""Main test runner for GitHub CI/CD."""
import os, time, subprocess, sys

TESTS = [
    "test_ecc_core.py",
    "test_index_calculus.py",
    "test_hypotheses.py",
    "test_puzzle_analysis.py"
]

def main():
    print("="*70)
    print(" ECDLP Research | Full Test Suite")
    print("="*70)
    passed = failed = 0
    t0 = time.time()
    
    test_dir = os.path.dirname(os.path.abspath(__file__))
    
    for test_file in TESTS:
        print(f"\n🔍 Running {test_file}...")
        proc = subprocess.run([sys.executable, test_file], capture_output=True, text=True, cwd=test_dir)
        print(proc.stdout.strip())
        if proc.returncode != 0:
            print(f"❌ {test_file}: FAILED")
            if proc.stderr: print(proc.stderr.strip()[-200:])
            failed += 1
        else:
            passed += 1
            
    print("\n" + "="*70)
    print(f"📊 Summary: {passed} passed, {failed} failed | Time: {time.time()-t0:.1f}s")
    print("="*70)
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())