# 🧮 ECDLP Research Suite

## Index Calculus, Spectral Analysis, and Structural Cryptanalysis of Elliptic Curves

---

# 🔍 Overview

This repository contains a comprehensive research framework for studying the **Elliptic Curve Discrete Logarithm Problem (ECDLP)** through algebraic, spectral, statistical, and structural approaches.

The project began as an exploration of unconventional attack vectors against Bitcoin Puzzle instances and evolved into a large-scale experimental environment for validating and falsifying ECDLP hypotheses.

The repository includes:

* A complete Index Calculus implementation for elliptic curves
* Spectral analysis of elliptic curve groups
* Statistical cryptanalysis of Bitcoin Puzzle datasets
* Structural investigations of key distributions
* Automated hypothesis testing framework
* Experimental benchmarks and reproducible research results

All components were implemented from scratch in pure Python.

---

# 🎯 Research Objectives

The primary goal of this project is to investigate whether hidden algebraic or geometric structures inside elliptic curve groups can provide shortcuts for solving ECDLP.

Research questions explored include:

* Can ECDLP be transformed into a simpler algebraic problem?
* Do Bitcoin Puzzle keys exhibit detectable structure?
* Can spectral methods reveal hidden information about scalar multiplication?
* Are there exploitable biases in public-key distributions?
* Can Index Calculus be adapted to elliptic curves in a practical way?

---

# ✨ Features

## ✅ Complete Index Calculus Framework

Implemented entirely in Python:

* Factor base construction
* Relation generation
* Smoothness testing
* Modular linear algebra
* CRT decomposition
* Discrete logarithm recovery

## ✅ Spectral Analysis Toolkit

Research modules for:

* Spectral continuity
* Eigenvalue distributions
* Graph Laplacians
* Random walk dynamics
* Spectral embeddings

## ✅ Statistical Cryptanalysis

Analysis of:

* Bitcoin Puzzle datasets
* Hamming-weight distributions
* wNAF representations
* Entropy measurements
* Correlation structures
* Linear complexity

## ✅ Hypothesis Validation Framework

Automated testing environment for evaluating potential ECDLP attack strategies.

## ✅ Pure Python Implementation

No external cryptographic libraries required.

## ✅ Fully Reproducible Research

All published results can be regenerated from repository code.

---

# 🧠 Investigated Hypotheses

The following hypotheses were studied experimentally.

| Hypothesis                     | Result                                      | Status         |
| ------------------------------ | ------------------------------------------- | -------------- |
| Echo-Polynomial Reduction      | No exploitable recursive structure detected | ❌ Falsified    |
| Isogeny Walk Reduction         | Neighbor curves preserve DLP hardness       | ❌ Falsified    |
| LFSR / Linear Recurrence Model | Keys exhibit CSPRNG characteristics         | ❌ Falsified    |
| Coppersmith-Based Reduction    | Polynomial growth becomes impractical       | ❌ Falsified    |
| Bias-Based Key Recovery        | No statistically significant bias found     | ❌ Falsified    |
| Spectral Continuity            | Observable and reproducible phenomenon      | ✅ Verified     |
| Graph-Theoretic ECC Structure  | Interesting geometry observed               | ✅ Investigated |
| Index Calculus on ECC          | Successfully implemented on small fields    | ✅ Verified     |

---

# 🔬 Index Calculus Implementation

A complete experimental Index Calculus implementation is included.

Pipeline:

## 1. Factor Base Construction

A factor base is generated from selected elliptic curve points satisfying smoothness criteria.

## 2. Relation Collection

Random combinations are generated:

R = aG + bQ

Relations are accepted whenever R decomposes over the factor base.

## 3. Linear Algebra

Relations produce a modular linear system:

Ax = b (mod N)

which is solved using CRT decomposition and modular elimination.

## 4. Logarithm Recovery

Recovered factor-base logarithms are combined to derive the target discrete logarithm.

---

# 📊 Experimental Results

## Test Curve

Curve:

y² = x³ + 7 (mod p)

where:

p ≈ 2²⁵

### Benchmark Results

| Metric                | Value    |
| --------------------- | -------- |
| Factor Base Size      | 63–238   |
| Relations Generated   | 150,000+ |
| Independent Equations | 258+     |
| Solve Time            | < 0.1 s  |
| Verification Success  | 100%     |

Verification:

kG = Q

for all tested instances.

---

# 📈 Bitcoin Puzzle Analysis

Datasets analyzed:

* Puzzle #1–#130
* Solved private keys
* Public keys
* Binary encodings
* wNAF expansions

## Findings

### Entropy

Observed entropy is consistent with cryptographically secure random generation.

### Correlations

No meaningful long-range correlations were detected.

### Linear Complexity

Measured complexity approaches:

L ≈ N/2

which is expected for secure pseudorandom sequences.

### Bias Detection

Only noise-level deviations were observed.

No statistically significant shortcut was identified.

---

# 🌊 Spectral Continuity Research

One of the most interesting outcomes of this research is the observation of spectral continuity within elliptic curve groups.

Experimental results indicate:

* Smooth spectral transitions between neighboring scalar multiples
* Stable spectral embeddings
* Reproducible geometric structure
* Consistent behavior across multiple curve sizes

However:

* No efficient inversion procedure was discovered
* No reduction in ECDLP complexity was achieved
* No practical key-recovery mechanism emerged

Current conclusion:

> Spectral continuity appears to be a genuine mathematical property of elliptic curve groups, but not currently a practical attack vector.

---

# ⚠️ Why Index Calculus Does Not Scale to secp256k1

Although successful on small fields, Index Calculus remains impractical for cryptographic curves.

For secp256k1:

p ≈ 2²⁵⁶

Approximate requirements:

* Factor base ≈ 2¹²⁸ elements
* Relation database ≈ 2¹²⁸ relations
* Astronomical storage requirements

Consequently:

> Generic attacks remain significantly more practical than Index Calculus on standard elliptic curves.

---

# 🚀 Quick Start

## Requirements

* Python 3.8+
* No external dependencies
* ~2 GB RAM recommended

## Clone Repository

```bash
git clone https://github.com/Anvexis/Index-Calculus-on-Elliptic-Curves.git
cd Index-Calculus-on-Elliptic-Curves
```

## Run Full Test Suite

```bash
python run_all_tests.py
```

## Run Individual Components

```bash
python test_ecc_core.py
python test_index_calculus.py
python test_hypotheses.py
python test_puzzle_analysis.py
```

---

# 📊 Test Modules

| Module                  | Purpose                      | Runtime |
| ----------------------- | ---------------------------- | ------- |
| test_ecc_core.py        | ECC arithmetic validation    | <1 s    |
| test_index_calculus.py  | Full Index Calculus pipeline | ~45 s   |
| test_hypotheses.py      | Hypothesis validation        | <1 s    |
| test_puzzle_analysis.py | Bitcoin Puzzle statistics    | <1 s    |

---

# ⚙️ Troubleshooting

### Index Calculus Occasionally Fails

Relation collection is probabilistic.

If a run fails:

```bash
python test_index_calculus.py
```

again.

Default success rate exceeds 95%.

### Slow Execution

The implementation prioritizes transparency and educational value over performance.

---

# 🚀 Practical ECDLP Algorithms

For real-world cryptographic curves:

## Pollard Kangaroo

* O(√N)
* Constant memory
* Highly parallelizable

## Pollard Rho

* Proven generic attack
* Low memory footprint

## GLV Decomposition

Provides practical speedups on secp256k1 while preserving generic complexity.

---

# 🔮 Future Work

* Parallel relation generation
* GPU acceleration
* CUDA-based Kangaroo implementation
* Spectral embeddings of secp256k1
* Advanced graph-theoretic analysis
* Formal academic publication
* Large-scale benchmark datasets

---

# 📜 Conclusions

The experimental evidence collected throughout this project supports the current cryptographic consensus:

* No practical shortcut to ECDLP was discovered.
* Bitcoin Puzzle keys behave consistently with secure randomness.
* Index Calculus remains effective only on relatively small fields.
* Spectral structures exist but currently provide no practical attack.

Nevertheless, the project offers a valuable research framework for exploring the mathematics underlying elliptic curve cryptography.

---

# 📄 License

MIT License

This repository is intended for:

* Education
* Research
* Cryptographic experimentation

Not intended for production cryptography or malicious use.

---

# 🙏 Acknowledgments

Special thanks to:

* Open-source cryptography researchers
* Bitcoin Puzzle community
* ECC researchers worldwide
* Everyone who contributed ideas, testing, and critical review

---

> "The best way to understand why an attack fails is to implement it completely."
