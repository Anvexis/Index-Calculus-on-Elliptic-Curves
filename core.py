"""
core.py
Mathematical core: ECC arithmetic, Index Calculus pipeline, hypothesis testing, puzzle analysis.
Pure Python 3.8+, zero external dependencies.
"""
import math
import random
from typing import List, Tuple, Optional, Dict

# ============================================================
# CURVE PARAMETERS
# ============================================================
P_TEST = 33554393
A_TEST = 0
B_TEST = 7
N_TEST = P_TEST + 1  # Group order for p ≡ 2 (mod 3)

# ============================================================
# BASIC ECC ARITHMETIC
# ============================================================
def mod_inv(a: int, m: int) -> int:
    return pow(a, m - 2, m)

def sqrt_mod(n: int, p: int) -> Optional[int]:
    """Tonelli-Shanks with integer-square fallback and index safety."""
    if n == 0: return 0
    if pow(n, (p - 1) // 2, p) != 1: return None
    
    int_root = int(n**0.5)
    if int_root * int_root == n:
        return int_root % p
        
    if p % 4 == 3: return pow(n, (p + 1) // 4, p)
    
    q, s = p - 1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1: z += 1
    
    m_val, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        i, temp = 0, t
        while temp != 1:
            temp = (temp * temp) % p
            i += 1
            if i == m_val: return None
        b = pow(c, 1 << (m_val - i - 1), p)
        m_val, c, t, r = i, (b * b) % p, (t * c) % p, (r * b) % p
    return r

def point_add(P1: Optional[Tuple[int,int]], P2: Optional[Tuple[int,int]], 
              p: int = P_TEST, a: int = A_TEST) -> Optional[Tuple[int,int]]:
    if P1 is None: return P2
    if P2 is None: return P1
    x1, y1 = P1; x2, y2 = P2
    if x1 == x2:
        if (y1 + y2) % p == 0: return None
        lam = (3 * x1 * x1 + a) * mod_inv(2 * y1, p) % p
    else:
        lam = (y2 - y1) * mod_inv(x2 - x1, p) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def point_neg(Pt: Optional[Tuple[int,int]], p: int = P_TEST) -> Optional[Tuple[int,int]]:
    return (Pt[0], (-Pt[1]) % p) if Pt else None

def point_mul(k: int, Pt: Optional[Tuple[int,int]], 
              p: int = P_TEST, a: int = A_TEST) -> Optional[Tuple[int,int]]:
    if k == 0: return None
    if k < 0: Pt, k = point_neg(Pt, p), -k
    R, Q = None, Pt
    while k > 0:
        if k & 1: R = point_add(R, Q, p, a)
        Q = point_add(Q, Q, p, a); k >>= 1
    return R

# ============================================================
# INDEX CALCULUS PIPELINE
# ============================================================
def build_factor_base(max_x: int, p: int = P_TEST, a: int = A_TEST, b: int = B_TEST) -> List[Tuple[int,int]]:
    base = []
    for x in range(max_x):
        y = sqrt_mod((x**3 + a*x + b) % p, p)
        if y is not None: base.append((x, y))
    return base

def build_sum_table(base: List[Tuple[int,int]], p: int = P_TEST, a: int = A_TEST) -> Dict[int, List[Tuple[int,int,int]]]:
    table = {}
    n = len(base)
    for i in range(n):
        for j in range(i, n):
            S = point_add(base[i], base[j], p, a)
            if S: table.setdefault(S[0], []).append((i, j, 1))
            if i != j:
                Sd = point_add(base[i], point_neg(base[j], p), p, a)
                if Sd: table.setdefault(Sd[0], []).append((i, j, -1))
    return table

def solve_system_crt(matrix: List[List[int]], rhs: List[int], modulus: int) -> Optional[int]:
    """Solves A*x = b (mod modulus) via Chinese Remainder Theorem. Returns k or None."""
    factors = []
    d, temp = 2, modulus
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            while temp % d == 0: temp //= d
        d += 1
    if temp > 1: factors.append(temp)
    
    residues, moduli_list = [], []
    for prime in factors:
        rows, cols = len(matrix), len(matrix[0])
        aug = [matrix[i][:] + [rhs[i]] for i in range(rows)]
        pivot = 0
        for col in range(cols):
            if pivot >= rows: break
            piv_row = next((r for r in range(pivot, rows) if aug[r][col] % prime != 0), -1)
            if piv_row == -1: continue
            aug[pivot], aug[piv_row] = aug[piv_row], aug[pivot]
            try:
                inv = pow(aug[pivot][col], -1, prime)
            except ValueError:
                continue
            for j in range(col, cols + 1): aug[pivot][j] = (aug[pivot][j] * inv) % prime
            for r in range(rows):
                if r != pivot and aug[r][col] != 0:
                    f = aug[r][col]
                    for j in range(col, cols + 1): aug[r][j] = (aug[r][j] - f * aug[pivot][j]) % prime
            pivot += 1
        
        sol = [0] * cols
        for r in range(pivot):
            lead = next((c for c in range(cols) if aug[r][c] == 1), -1)
            if lead != -1: sol[lead] = aug[r][cols]
        residues.append(sol[-1])
        moduli_list.append(prime)
    
    if not residues: return None
    x, m = residues[0], moduli_list[0]
    for i in range(1, len(residues)):
        r, n = residues[i], moduli_list[i]
        a_, b_ = m, n
        x1, x2 = 1, 0
        while b_:
            q = a_ // b_; a_, b_ = b_, a_ % b_
            x1, x2 = x2, x1 - q * x2
        x = (x + m * x1 * (r - x)) % (m * n)
        m = m * n
    return x

def run_index_calculus(p: int = P_TEST, a: int = A_TEST, b: int = B_TEST, 
                       max_x: int = 800, target_relations: int = None) -> Tuple[int, int, bool]:
    """Returns (found_k, secret_k, success)"""
    N = p + 1
    fb = build_factor_base(max_x, p, a, b)
    if not fb: return 0, 0, False
    
    st = build_sum_table(fb, p, a)
    if target_relations is None:
        target_relations = len(fb) + 15  # Overdetermined system
        
    G = None
    for x in range(p):
        y = sqrt_mod((x**3 + a*x + b) % p, p)
        if y is not None and point_mul(1000, (x, y), p, a) is not None:
            G = (x, y); break
    if G is None: return 0, 0, False
    
    secret = random.randint(1, N-1)
    Q = point_mul(secret, G, p, a)
    
    # Adaptive attempt limit based on table coverage probability
    coverage = len(st) / p
    expected_per_rel = int(1.0 / max(coverage, 1e-6)) + 50
    max_att = max(400_000, int(target_relations * expected_per_rel * 1.5))
    
    eqs, att = [], 0
    while len(eqs) < target_relations and att < max_att:
        att += 1
        av, bv = random.randint(1, N-1), random.randint(1, N-1)
        R = point_add(point_mul(av, G, p, a), point_mul(bv, Q, p, a), p, a)
        if R and R[0] in st:
            for i, j, s in st[R[0]]:
                Pi, Pj = fb[i], fb[j]
                if point_add(Pi, Pj if s==1 else point_neg(Pj, p), p, a) == R:
                    eqs.append({'i': i, 'j': j, 'a': av, 'b': bv}); break
    
    if len(eqs) < target_relations:
        return 0, secret, False
    
    nv = len(fb) + 1
    mat = [[0]*nv for _ in eqs]
    rhs = []
    for idx, e in enumerate(eqs):
        mat[idx][e['i']] = (mat[idx][e['i']] + 1) % N
        mat[idx][e['j']] = (mat[idx][e['j']] + 1) % N
        mat[idx][-1] = (-e['b']) % N
        rhs.append(e['a'])
    
    k_found = solve_system_crt(mat, rhs, N)
    if k_found is None: return 0, secret, False
    success = point_mul(k_found, G, p, a) == Q
    return k_found, secret, success

# ============================================================
# HYPOTHESIS ANALYSIS
# ============================================================
def echo_score(blocks: List[int], alpha: int) -> int:
    return sum(1 for i in range(len(blocks)-1) if blocks[i+1] == (alpha * blocks[i]) % 32)

def berlekamp_massey_gf2(bits: List[int]) -> int:
    """Computes linear complexity of a binary sequence using Berlekamp-Massey."""
    n = len(bits)
    C, B = [1], [1]
    L, m = 0, 1
    for i in range(n):
        while len(C) < L + 1: C.append(0)
        d = bits[i]
        for j in range(1, L + 1):
            if i - j >= 0: d ^= C[j] & bits[i - j]
        if d:
            T = C[:]
            while len(C) < len(B) + m: C.append(0)
            for j in range(len(B)): C[j + m] ^= B[j]
            if 2 * L <= i:
                L = i + 1 - L; B = T[:]; m = 1
            else: m += 1
    return L

def hex_to_blocks(hex_key: str, bits_per_block: int = 5) -> List[int]:
    k = int(hex_key, 16)
    return [(k >> (i * bits_per_block)) & ((1 << bits_per_block) - 1) for i in range(k.bit_length() // bits_per_block + 1)]