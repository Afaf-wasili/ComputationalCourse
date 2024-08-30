import numpy as np
import matplotlib.pyplot as plt
import math

# Define the Poisson distribution PMF function
def poisson_pmf(k, lam):


    """
    Compute the Poisson distribution PMF (Probability Mass Function).
    
    Parameters:
    - k: array-like, number of events (non-negative integers)
    - lam: rate parameter (average number of events)
    
    Returns:
    - PMF values for the input array
    """
    return (lam**k * np.exp(-lam)) / np.array([math.factorial(i) for i in k])

# Parameters for the Poisson distribution
lam = 5  # Average rate (mean number of events)

# Generate a range of k values
k = np.arange(0, 15)

# Compute the Poisson PMF
pmf = poisson_pmf(k, lam)

# Plot with fill style using bar plot
plt.figure(figsize=(12, 6))
'''
# Bar plot with fill style
plt.subplot(1, 2, 1)
plt.bar(k, pmf, color='b', alpha=0.7, label=f'Poisson Distribution\n$\lambda={lam}$')
plt.xlabel('Number of Events (k)')
plt.ylabel('Probability')
plt.title('Poisson Distribution (Bar Plot)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
'''
# Line plot with fill style
#plt.subplot(1, 2, 2)
plt.plot(k, pmf, marker='o', color='b', label=f'Poisson Distribution\n$\lambda={lam}$')
plt.fill_between(k, pmf, color='b', alpha=0.3)  # Filling the area under the curve
plt.xlabel('Number of Events (k)')
plt.ylabel('Probability')
plt.title('Poisson Distribution (Line Plot)')
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
#plt.show()
plt.savefig("Plots/Poission.png")
# Print calculated Poisson PMF values
for i, prob in zip(k, pmf):
    print(f"P(X = {i}) = {prob:.4f}")
