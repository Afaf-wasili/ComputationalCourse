import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Generate example data (quadratic with noise)
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 0.5 * x**2 + np.random.normal(0, 1, size=len(x))  # Quadratic data with noise

# Define quadratic function (without noise) for fitting
def quadratic_func(x, a, b):
    return a * x**2 + b

# Fit the quadratic function to the data
popt, _ = curve_fit(quadratic_func, x, y)

# Calculate fitted values and ratio
fitted_values = quadratic_func(x, *popt)
ratio = fitted_values / y

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), sharex=True)

# Main plot (top)
ax1.scatter(x, y, label='Data', color='b', alpha=0.7)
ax1.plot(x, fitted_values, color='r', linestyle='--', label='Quadratic Fit')
ax1.set_ylabel('Y axis')
ax1.set_title('Data and Quadratic Fit')
ax1.legend()
ax1.grid(True)

# Ratio plot (bottom)
ax2.plot(x, ratio, color='g')
ax2.axhline(y=1.0, color='gray', linestyle='--')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Ratio')
ax2.grid(True)

# Adjust layout and display plot
plt.tight_layout()
plt.show()
