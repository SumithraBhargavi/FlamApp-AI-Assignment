import os
import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution

from objective import objective

# -------------------------------
# Load CSV
# -------------------------------

data = pd.read_csv("../data/xy_data.csv")

actual_points = data[["x", "y"]].values

# -------------------------------
# Optimization bounds
# -------------------------------

bounds = [
    (0, 50),        # theta
    (-0.05, 0.05),  # M
    (0, 100)        # X
]

print("=" * 50)
print("Starting Optimization...")
print("=" * 50)

# -------------------------------
# Run optimization
# -------------------------------

result = differential_evolution(
    objective,
    bounds,
    args=(actual_points,),
    strategy="best1bin",
    maxiter=100,
    popsize=20,
    tol=1e-6,
    mutation=(0.5, 1.0),
    recombination=0.7,
    seed=42,
    polish=True,
)

theta, M, X = result.x

print("\nOptimization Finished\n")

print(f"Theta : {theta:.6f}")
print(f"M     : {M:.6f}")
print(f"X     : {X:.6f}")
print(f"Error : {result.fun:.6f}")

# -------------------------------
# Save results
# -------------------------------

os.makedirs("../results", exist_ok=True)

with open("../results/parameters.txt", "w") as f:
    f.write("Estimated Parameters\n")
    f.write("=====================\n\n")
    f.write(f"Theta = {theta:.10f}\n")
    f.write(f"M     = {M:.10f}\n")
    f.write(f"X     = {X:.10f}\n")
    f.write(f"\nObjective Error = {result.fun:.10f}\n")

print("\nResults saved to results/parameters.txt")