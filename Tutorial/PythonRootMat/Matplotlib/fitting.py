import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.optimize import curve_fit

# Generate example signal data
np.random.seed(0)
signal = np.random.normal(loc=5, scale=1, size=10000)

# Fit Gaussian to signal data
(mu, sigma) = norm.fit(signal)

# Define a Gaussian function
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) ** 2) / (2 * stddev ** 2))

# Bin signal data for histogram
counts, bins, _ = plt.hist(signal, bins=50, density=True, alpha=0.6, color='b', label='Signal')

# Fit the Gaussian model to the data
popt, _ = curve_fit(gaussian, bins[:-1], counts, p0=[1, mu, sigma])

# Plot fitted Gaussian curve
#Generate 100 evenly spaced points between the first and last bin edge
x_fit = np.linspace(bins[0], bins[-1], 100)
plt.plot(x_fit, gaussian(x_fit, *popt), color='r', label='Gaussian Fit')

# Add legend with fit parameters
plt.legend()
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Signal Distribution with Gaussian Fit')

# Display fit parameters
plt.text(0.95, 0.85, f'$\mu={popt[1]:.2f}$\n$\sigma={np.abs(popt[2]):.2f}$', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.grid(True)
plt.tight_layout()
plt.show()
