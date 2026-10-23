# Cryptography and Hashing Fundamentals Report

## 1. Cryptographic Hashing Functions
Unlike encryption, hashing is a structural one-way function. It maps an arbitrary size input string into a fixed-length hexadecimal digest output. Once hashed, the original data cannot be mathematically reverse-engineered.

### Key Characteristics:
- **Deterministic:** The same input will always generate the exact same hash signature.
- **Collision Resistant:** It is computationally unfeasible for two distinct inputs to yield an identical hash digest.
- **Avalanche Effect:** A tiny mutation in the source input string completely alters the output hash digest.

## 2. Practical Applications
- **Password Storage:** Systems store hashed inputs instead of plaintext, preserving authentication safety during database leaks.
- **Data Integrity Verification:** Comparing software download hash signatures against original vendor values to verify data corruption or tempering.
