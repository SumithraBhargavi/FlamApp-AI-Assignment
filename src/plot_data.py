import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv("../data/xy_data.csv")

# Display basic information
print("First 5 rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns.tolist())

print("\nMissing Values:")
print(data.isnull().sum())

# Create the figure
plt.figure(figsize=(8, 8))

# Draw the curve in the order of the CSV rows
plt.plot(
    data["x"],
    data["y"],
    linewidth=1,
    color="blue",
    label="Curve"
)

# Draw the points
plt.scatter(
    data["x"],
    data["y"],
    s=10,
    color="red",
    label="Data Points"
)

plt.title("Input Curve (CSV Order)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()

# Save the figure
plt.savefig("../results/input_curve_ordered.png", dpi=300)

# Show the figure
plt.show()