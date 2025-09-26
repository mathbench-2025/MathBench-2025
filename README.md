# MathBench-2025

MathBench-2025 is a reproducible benchmark framework for evaluating **mathematical reasoning in large language models (LLMs)**. It provides structured datasets, standardized evaluation metrics, illustrative tasks, and boilerplate code to enable systematic assessment of reasoning depth, step-wise fidelity, and generalization.

---

## Overview

Mathematical reasoning is a core cognitive skill that remains challenging for AI. While recent LLMs have shown promising performance in arithmetic, algebra, calculus, and theorem-style problems, multi-step reasoning, compositionality, and real-world applied tasks remain difficult.

MathBench-2025 addresses these gaps by providing:

- **Structured Dataset:** Multi-step problems across arithmetic, algebra, proofs, and applied reasoning, with annotated intermediate steps.
- **Evaluation Protocol:** Metrics for accuracy, step-wise correctness, generalization, and partial credit.
- **Illustrative Examples:** Sample problems across varying complexity levels (Level 1–5).
- **Reproducible Framework:** Boilerplate code for evaluation and model benchmarking.

---

## Dataset Structure

Each entry in MathBench-2025 includes:

| Field | Description | Example |
|-------|-------------|---------|
| problem_id | Unique problem identifier | MB-ALG-0321 |
| problem_type | Task category | algebra |
| complexity_level | Difficulty rating (1–5) | 3 |
| solution_steps | Step-wise solution trace | Expand → Simplify → Solve |
| topic | Specific mathematical domain | linear equations |
| reference_solution | Ground-truth final answer | x = 5 |

**Complexity Levels:**

1. **Level 1 – Basic Arithmetic**: Single-step computations  
2. **Level 2 – Elementary Algebra**: 2–3 step transformations  
3. **Level 3 – Compositional Reasoning**: Multi-step derivations  
4. **Level 4 – Structured Proofs**: Multi-stage inductive/deductive reasoning  
5. **Level 5 – Applied Multi-Domain**: Real-world problems in physics, finance, or geometry

---

## Evaluation Metrics

The benchmark evaluates models using multiple metrics:

| Metric | Definition | Example |
|--------|------------|---------|
| Accuracy (A) | Fraction of fully correct solutions | 78/100 → 0.78 |
| Step-wise Correctness (S) | Fraction of correct intermediate steps | 430/500 → 0.86 |
| Generalization (G) | Performance on unseen problems | 18/20 → 0.90 |
| Partial Credit (P) | Average credit across steps | Steps [1,1,0.5,1] → 0.875 |

---

## Usage

Clone the repository:

```bash
git clone git@github.com:<anon-username>/MathBench-2025.git
cd MathBench-2025
