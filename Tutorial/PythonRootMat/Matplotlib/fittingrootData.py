import numpy as np
import matplotlib.pyplot as plt
import uproot
from scipy.optimize import curve_fit

# Define the Gaussian function
def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))

file_path = "Plots/histo.root"

# Open the ROOT file
file = uproot.open(file_path)

# Access the "data" histogram
data_hist = file["data"]

# Extract data
data_edges = data_hist.axis().edges()
data_values = data_hist.values()
data_centers = (data_edges[:-1] + data_edges[1:]) / 2

# Initial parameter estimates
initial_amplitude = max(data_values)
initial_mu = data_centers[np.argmax(data_values)]
initial_sigma = np.std(data_centers)

# Fit the Gaussian to the data
popt, pcov = curve_fit(gaussian, data_centers, data_values, p0=[initial_amplitude, initial_mu, initial_sigma])

# Extract errors for mean and sigma from covariance matrix
mu_error = np.sqrt(pcov[1][1])
sigma_error = np.sqrt(pcov[2][2])

# Generate x_fit using the specified range
x_fit = np.linspace(data_edges[0], data_edges[-1], 1000)
y_fit = gaussian(x_fit, *popt)

# Plot the data histogram and the Gaussian fit
plt.figure(figsize=(10, 7))
plt.step(data_centers, data_values, where='mid', color='blue', label='Data')
plt.plot(x_fit, y_fit, 'r-', label=f'Fit: $\mu={popt[1]:.2f} \pm {mu_error:.2f}$, $\sigma={popt[2]:.2f} \pm {sigma_error:.2f}$')
plt.xlabel('X axis')
plt.ylabel('Counts')
plt.title('Data Histogram and Gaussian Fit')
plt.legend()
plt.grid(True)
plt.savefig("Plots/Data_GaussianFit.png")
plt.show()
