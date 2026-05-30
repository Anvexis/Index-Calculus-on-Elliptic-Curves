"""Tests for basic ECC arithmetic and Tonelli-Shanks."""
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from core import sqrt_mod, point_add, point_neg, point_mul, P_TEST, A_TEST

def test_sqrt_mod():
    # Dynamically find a quadratic residue to avoid hardcoded assumptions
    for n in range(1, 50):
        if pow(n, (P_TEST - 1) // 2, P_TEST) == 1:
            root = sqrt_mod(n, P_TEST)
            assert root is not None, f"sqrt_mod failed for quadratic residue {n}"
            assert (root * root) % P_TEST == n, f"Root verification failed: {root}^2 != {n} mod P"
            return
    raise AssertionError("Could not locate a testable quadratic residue")

def test_point_ops():
    G = (1, 33554392)
    assert point_add(G, point_neg(G, P_TEST), P_TEST, A_TEST) is None
    assert point_mul(1, G, P_TEST, A_TEST) == G
    assert point_mul(2, G, P_TEST, A_TEST) == point_add(G, G, P_TEST, A_TEST)
    print("✅ point_ops: PASSED")

if __name__ == "__main__":
    test_sqrt_mod()
    print("✅ sqrt_mod: PASSED")
    test_point_ops()