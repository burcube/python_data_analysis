import pandas as pd  # version 1.3.0
import numpy as np  # version 1.21.0
import matplotlib.pyplot as plt  # version 3.4.0

# Generate or load a sample dataset
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 10, 67, 38]
}
df = pd.DataFrame(data)

# Basic Data Analysis
print("Summary Statistics:")
print(df.describe())

# Plotting the data
plt.figure(figsize=(8, 5))
plt.bar(df['Category'], df['Values'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Values by Category')
plt.show()

# Additional Analysis: Mean and Standard Deviation
mean_value = np.mean(df['Values'])
std_dev = np.std(df['Values'])
print(f"\nMean of Values: {mean_value}")
print(f"Standard Deviation of Values: {std_dev}")

# Scatter Plot with Random Data (for demonstration)
# Generate random data points for a scatter plot
np.random.seed(42)  # for reproducibility
x = np.random.rand(50) * 100
y = np.random.rand(50) * 100
plt.figure(figsize=(8, 5))
plt.scatter(x, y, c='purple', alpha=0.6, edgecolors='w', s=80)
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.title('Random Scatter Plot')
plt.show()
