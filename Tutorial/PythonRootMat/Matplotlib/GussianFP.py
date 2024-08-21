import numpy as np
import matplotlib.pyplot as plt

# Define the Gaussian (Normal) distribution function
def gaussian(x, mu, sigma):
    """
    Compute the Gaussian distribution (Normal distribution) PDF.
    
    Parameters:
    - x: array-like, values at which to compute the PDF
    - mu: mean of the distribution
    - sigma: standard deviation of the distribution
    
    Returns:
    - PDF values for the input array
    """
    return (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu)**2 / sigma**2))

# Parameters for the Gaussian distribution
mu = 0       # Mean
sigma = 1    # Standard deviation

# Generate a range of x values
x = np.linspace(-5, 5, 1000)

# Compute the Gaussian PDF
pdf = gaussian(x, mu, sigma)

# Plot the Gaussian distribution
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label=f'Gaussian Distribution\n$\mu={mu}$, $\sigma={sigma}$', color='b')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Gaussian (Normal) Distribution')
plt.grid(True)
plt.legend()
plt.show()
