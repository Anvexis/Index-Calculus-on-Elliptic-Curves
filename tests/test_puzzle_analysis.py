"""Statistical analysis of known Bitcoin Puzzle keys."""
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from core import hex_to_blocks, echo_score, berlekamp_massey_gf2

KNOWN_KEYS = [
    "0000000000000000000000000000000000b10f22572c497a836ea187f2e1fc23",
    "000000000000000000000000000000001c533b6bb7f0804e09960225e44877ac",
    "000000000000000000000000000000033e7665705359f04f28b88cf897c603c9",
]

def test_puzzle_echo_scores():
    for hx in KNOWN_KEYS:
        blocks = hex_to_blocks(hx, 5)
        scores = [echo_score(blocks, a) for a in range(1, 32, 2)]
        assert max(scores) <= 4, f"Puzzle {hx[-6:]} showed suspicious Echo score: {max(scores)}"
    print("✅ puzzle_echo_scores: PASSED")

def test_puzzle_lfsr():
    for hx in KNOWN_KEYS:
        bits = [(int(hx, 16) >> i) & 1 for i in range(int(hx, 16).bit_length())]
        L = berlekamp_massey_gf2(bits)
        expected = len(bits) // 2
        assert L >= expected * 0.7, f"LFSR complexity for {hx[-6:]} too low: {L} < {expected*0.7}"
    print("✅ puzzle_lfsr: PASSED")

if __name__ == "__main__":
    test_puzzle_echo_scores()
    test_puzzle_lfsr()