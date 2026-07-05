# FlamApp AI – Research & Development Assignment

## Overview

This project estimates the unknown parameters **θ (Theta), M, and X** of the given parametric curve using the provided dataset (`xy_data.csv`).

The solution uses numerical optimization and nearest-neighbor matching to fit the generated curve to the given point cloud.

---

## Problem Statement

Estimate the unknown parameters of the following parametric equations:

$$
x = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
$$

$$
y = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
$$

Subject to:

- \(0^\circ < \theta < 50^\circ\)
- \(-0.05 < M < 0.05\)
- \(0 < X < 100\)
- \(6 < t < 60\)

# Project Structure

```
FlamApp-AI-Assignment/
│
├── data/
│   └── xy_data.csv
│
├── results/
│   ├── input_curve.png
│   ├── input_curve_ordered.png
│   ├── fitted_curve.png
│   └── parameters.txt
│
├── src/
│   ├── plot_data.py
│   ├── model.py
│   ├── objective.py
│   ├── optimize.py
│   └── visualize.py
│
├── README.md
├── requirements.txt
└── result.txt
```

---

# Methodology

## 1. Data Exploration

- Loaded the provided dataset.
- Verified dataset dimensions.
- Checked for missing values.
- Visualized the input curve.

## 2. Dataset Analysis

The dataset was inspected by plotting consecutive points.

The visualization showed that the CSV points are **unordered**, making direct row-by-row comparison unsuitable.

## 3. Mathematical Model

The given parametric equations were implemented exactly as provided.

The parameter **t** was uniformly sampled between **6 and 60**.

## 4. Optimization

The unknown parameters were estimated using:

- Differential Evolution (SciPy)
- KDTree-based nearest-neighbor matching
- Bounded optimization according to assignment constraints

The objective function minimizes the total nearest-neighbor distance between the generated curve and the observed dataset.

## 5. Visualization

The optimized curve was plotted together with the original dataset to visually validate the fitting.

---

# Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib

---

# Estimated Parameters

| Parameter | Value |
|-----------|-------|
| Theta | **29.999475** |
| M | **0.030000** |
| X | **54.999137** |

Objective Error:

```
31.854430
```

---

# Output Files

The project generates:

- `results/input_curve.png`
- `results/input_curve_ordered.png`
- `results/fitted_curve.png`
- `results/parameters.txt`
- `result.txt`

---

# How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run optimization

```bash
cd src
python optimize.py
```

Generate visualization

```bash
python visualize.py
```

---
## Final Estimated Parametric Equation

```latex
\left(
t*\cos(0.52359)
-
e^{0.03\left|t\right|}
\cdot
\sin(0.3t)\sin(0.52359)
+
54.999137,
42
+
t*\sin(0.52359)
+
e^{0.03\left|t\right|}
\cdot
\sin(0.3t)\cos(0.52359)
\right)
```

# Assumptions

- Parameter **t** is uniformly sampled in the interval **[6, 60]**.
- Since the dataset points are unordered, nearest-neighbor matching was used instead of row-wise comparison.
- Differential Evolution was selected because it performs well for nonlinear optimization problems.

---

# Future Improvements

- One-to-one point matching using the Hungarian Algorithm.
- Local optimization refinement after global optimization.
- Faster convergence using hybrid optimization techniques.
- Automatic uncertainty estimation of parameters.

---

# Author

**M. Sumithra Bhargavi**

Amrita Vishwa Vidyapeetham

FlamApp AI – Research & Development Assignment
