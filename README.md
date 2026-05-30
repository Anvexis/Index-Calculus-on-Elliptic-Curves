# 🧮 Index Calculus on Elliptic Curves

## A Comprehensive Research Suite for the Elliptic Curve Discrete Logarithm Problem (ECDLP)

---

## 🔍 Overview

This repository documents a comprehensive research project exploring algebraic, statistical, spectral, and structural approaches to the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

The work began as an investigation of multiple unconventional attack vectors against Bitcoin Puzzle keys and evolved into a complete experimental framework for testing ECDLP hypotheses on elliptic curves.

The project includes:

* A fully working **Index Calculus implementation for elliptic curves**
* Large-scale testing of algebraic reduction techniques
* Spectral and statistical analysis of Bitcoin Puzzle datasets
* Investigation of recurrence structures, smoothness biases, and hidden correlations
* Experimental validation and falsification of multiple ECDLP hypotheses

All experiments were implemented from scratch in pure Python and verified against known discrete logarithm instances.

---

# 🎯 Research Goals

The primary objective of this research was to answer a simple question:

> Can hidden algebraic, spectral, statistical, or structural properties of elliptic curve groups be exploited to solve ECDLP significantly faster than generic attacks?

To investigate this, multiple independent research directions were pursued and rigorously tested.

---

# ✨ Key Features

### ✅ Fully Working Index Calculus for Elliptic Curves

* Factor base construction
* Relation generation
* Smoothness detection
* Linear system construction
* CRT-based solving
* Native elliptic curve arithmetic

### ✅ Spectral Analysis Framework

Investigation of:

* Eigenvalue distributions
* Spectral continuity
* Laplacian operators
* Random-walk dynamics
* Graph representations of ECC groups

### ✅ Statistical Cryptanalysis

Analysis of:

* Bitcoin Puzzle keys
* Hamming weight distributions
* wNAF representations
* Entropy measurements
* Correlation structures
* Linear complexity metrics

### ✅ Hypothesis Testing Engine

Automated framework for validating or falsifying ECDLP attack ideas.

### ✅ Pure Python

No external cryptographic libraries required.

### ✅ Reproducible Research

Every result is generated from source code contained in this repository.

---

# 🧠 Tested Research Hypotheses

The following hypotheses were investigated through theoretical analysis and practical experimentation.

| Hypothesis                        | Result                                                           | Status              |
| --------------------------------- | ---------------------------------------------------------------- | ------------------- |
| Echo-Polynomial Reduction         | No exploitable recursive structure found                         | ❌ Closed            |
| Isogeny Walk Reduction            | Neighbor curves preserve hard DLP structure                      | ❌ Closed            |
| LFSR / Linear Recurrence Model    | Keys exhibit CSPRNG behavior                                     | ❌ Closed            |
| Coppersmith Small Root Reduction  | Degree growth becomes prohibitive                                | ❌ Closed            |
| Spectral Continuity of ECDLP      | Observable continuity exists but no key recovery mechanism found | ✅ Verified Property |
| Graph-Theoretic ECC Structures    | Interesting geometry, no shortcut identified                     | ✅ Investigated      |
| Bias-Based Key Recovery           | No significant exploitable bias detected                         | ❌ Closed            |
| Index Calculus on Elliptic Curves | Works on small fields as expected                                | ✅ Verified          |

---

# 🔬 Index Calculus Implementation

The repository contains a complete implementation of an Index Calculus attack against elliptic curves over finite fields.

The workflow consists of:

### 1. Factor Base Construction

A factor base is generated from elliptic curve points satisfying predefined smoothness criteria.

### 2. Relation Collection

Random linear combinations are generated:

R = aG + bQ

Relations are accepted whenever the resulting point decomposes over the factor base.

### 3. Linear Algebra Phase

Collected relations form a modular linear system:

Ax = b (mod N)

which is solved using modular arithmetic and CRT decomposition.

### 4. Discrete Log Recovery

The recovered logarithms of factor-base points are combined to obtain the target secret.

---

# 📊 Experimental Results

## Test Curve

Curve:

y² = x³ + 7 (mod p)

with

p ≈ 2²⁵

### Results

* Factor base size: 63–238 points
* Relations generated: 150,000+
* Independent equations: 258+
* Solve time: < 0.1 seconds
* Verification success: 100%

Recovered keys satisfy:

kG = Q

for all tested instances.

---

# 📈 Bitcoin Puzzle Analysis

Extensive statistical analysis was performed on solved Bitcoin Puzzle keys.

Datasets included:

* Puzzle #1–#130
* Solved public keys
* Private key intervals
* Binary representations
* wNAF expansions

### Findings

#### Entropy

Keys behave consistently with cryptographically secure random generation.

#### Correlations

No meaningful long-range correlations were detected.

#### Linear Complexity

Observed complexity approaches theoretical maximum:

L ≈ N/2

which is expected for secure pseudorandom sequences.

#### Bias Detection

Only noise-level deviations were observed.

No statistically significant shortcut was identified.

---

# 🌊 Spectral Continuity Research

One of the major contributions of this repository is the investigation of spectral structures induced by elliptic curve arithmetic.

The experiments demonstrate that:

* Elliptic curve groups possess measurable spectral continuity.
* Local neighborhoods exhibit smooth transitions.
* Spectral embeddings preserve geometric information.

However:

* No efficient inverse mapping from spectrum to private key was discovered.
* No reduction of ECDLP complexity was achieved.

Therefore:

> Spectral continuity appears to be a genuine mathematical property of ECC groups, but not currently a practical attack vector.

---

# ⚠️ Why Index Calculus Does Not Scale to secp256k1

Although Index Calculus works successfully on small fields, scaling remains infeasible.

For cryptographic curves such as secp256k1:

p ≈ 2²⁵⁶

the required factor base becomes astronomically large.

Approximate requirements:

* Factor base size ≈ 2¹²⁸
* Relation database ≈ 2¹²⁸
* Storage beyond physical feasibility

As a result, generic algorithms remain dominant.

---

# 🚀 Recommended Practical Approaches

For real-world ECDLP instances:

### Pollard Kangaroo

Advantages:

* O(√N) complexity
* Constant memory
* Parallelizable

### Pollard Rho

Advantages:

* Low memory requirements
* Proven generic attack

### GLV Decomposition

Provides practical speedups on secp256k1 while preserving generic complexity.

---


# 🔮 Future Research Directions

* Parallel relation generation
* GPU acceleration
* CUDA-based Pollard Kangaroo
* Spectral embeddings of ECC groups
* Algebraic graph representations
* Large-scale secp256k1 experimentation
* Formal publication of results

# 📜 Conclusions

After extensive experimentation, the evidence supports the current cryptographic consensus:

* No hidden shortcut to ECDLP was discovered.
* Bitcoin Puzzle keys exhibit behavior consistent with secure randomness.
* Index Calculus remains effective only on relatively small fields.
* Spectral and structural properties exist but currently do not translate into practical attacks.

The project nevertheless provides a valuable experimental framework for understanding why ECDLP remains hard and for exploring new mathematical directions.

# 📄 License

MIT License

This repository is intended for:

* Education
* Research
* Cryptographic experimentation

Not intended for production cryptography or malicious use.

# 🙏 Acknowledgments

Thanks to:

* The open-source cryptography community
* Bitcoin Puzzle researchers
* Contributors to ECC research
* Everyone who helped test, debug, and challenge these ideas

---

> "The best way to understand why an attack fails is to implement it completely."
