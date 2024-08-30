import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Generate example data (quadratic)

np.random.seed(0)
#x = np.linspace(0, 10, 100)
x = np.array([1, 2, 3, 4, 5])   
y = 0.5 * x**2 + np.random.normal(0, 1, size=len(x))  # Quadratic

'''
# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 5, 6, 7, 7])
'''
# Define quadratic function
def quadratic_func(x, a, b):
    return a * x**2 + b

# Fit quadratic function to data
popt, _ = curve_fit(quadratic_func, x, y)
fitted_values = quadratic_func(x, *popt)
ratio = fitted_values / y

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), sharex=True)

# Plot data and fit
ax1.scatter(x, y, color='b', alpha=0.7, label='Data')
ax1.plot(x, fitted_values, color='r', linestyle='--', label='Quadratic Fit')
ax1.set_title('Data and Quadratic Fit')
ax1.set_ylabel('Y axis')
ax1.legend()
ax1.grid(True)

# Plot ratio
ax2.plot(x, ratio, color='g')
ax2.axhline(y=1.0, color='gray', linestyle='--')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Ratio')
ax2.grid(True)

plt.tight_layout()
plt.show()
