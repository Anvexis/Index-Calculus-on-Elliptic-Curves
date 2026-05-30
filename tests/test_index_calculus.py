"""Full pipeline test for Index Calculus on a test curve."""
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from core import run_index_calculus

def test_full_pipeline():
    print("Running Index Calculus pipeline (p ≈ 2^25)...")
    # Uses adaptive limits to guarantee success
    k_found, secret, success = run_index_calculus()
    assert success, f"Index Calculus failed. found={k_found}, secret={secret}"
    print(f"✅ Index Calculus: PASSED (recovered k ≡ {secret} mod ord(G))")

if __name__ == "__main__":
    test_full_pipeline()