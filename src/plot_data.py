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
print(data.columns)

print("\nMissing Values:")
print(data.isnull().sum())

# Plot the points
plt.figure(figsize=(8, 8))
plt.scatter(data["x"], data["y"], s=10)
plt.title("Input Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Save the figure
plt.savefig("../results/input_curve.png", dpi=300)

# Show the figure
plt.show()