import os
import pandas as pd
import matplotlib.pyplot as plt

from model import generate_curve

# -------------------------
# Read estimated parameters
# -------------------------

theta = None
M = None
X = None

with open("../results/parameters.txt", "r") as f:
    for line in f:
        line = line.strip()

        if line.startswith("Theta"):
            theta = float(line.split("=", 1)[1])

        elif line.startswith("M"):
            M = float(line.split("=", 1)[1])

        elif line.startswith("X"):
            X = float(line.split("=", 1)[1])

# -------------------------
# Load dataset
# -------------------------

data = pd.read_csv("../data/xy_data.csv")

# -------------------------
# Generate fitted curve
# -------------------------

pred_x, pred_y = generate_curve(theta, M, X)

# -------------------------
# Plot
# -------------------------

plt.figure(figsize=(8, 8))

plt.scatter(
    data["x"],
    data["y"],
    s=8,
    color="red",
    label="Actual Data"
)

plt.plot(
    pred_x,
    pred_y,
    color="blue",
    linewidth=2,
    label="Predicted Curve"
)

plt.title("Curve Fitting Result")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()

os.makedirs("../results", exist_ok=True)

plt.savefig("../results/fitted_curve.png", dpi=300)

plt.show()

print("Plot saved to results/fitted_curve.png")