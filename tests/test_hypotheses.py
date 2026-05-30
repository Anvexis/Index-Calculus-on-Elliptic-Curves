"""Tests for closed hypotheses: Echo patterns, LFSR complexity, block structure."""
import sys, os, random
sys.path.insert(0, os.path.abspath('..'))
from core import echo_score, berlekamp_massey_gf2, hex_to_blocks

def test_echo_randomness():
    random.seed(42)
    blocks = [random.randint(0, 31) for _ in range(30)]
    scores = [echo_score(blocks, a) for a in range(1, 32, 2)]
    assert max(scores) <= 4, f"Random blocks showed anomalous Echo score: {max(scores)}"
    print("✅ echo_randomness: PASSED")

def test_lfsr_complexity():
    random.seed(42)
    bits = [random.randint(0, 1) for _ in range(60)]
    L = berlekamp_massey_gf2(bits)
    assert L >= 25, f"LFSR complexity too low for random bits: {L}"
    print("✅ lfsr_complexity: PASSED")

def test_block_structure():
    blocks = hex_to_blocks("0x0000000000000000000000000000000000000000000000000000000000000001", 5)
    assert blocks[0] == 1 and all(b == 0 for b in blocks[1:10]), "Block conversion failed"
    print("✅ block_structure: PASSED")

if __name__ == "__main__":
    test_echo_randomness()
    test_lfsr_complexity()
    test_block_structure()