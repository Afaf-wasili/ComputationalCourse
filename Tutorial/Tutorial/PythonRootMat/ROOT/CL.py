import numpy as np
import matplotlib.pyplot as plt

# Example data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y_true = 2 * np.sin(x)
y = y_true + np.random.normal(0, 0.5, size=x.shape[0])

# Fit a polynomial curve
p = np.polyfit(x, y, 3)
y_fit = np.polyval(p, x)

# Calculate confidence intervals
def polyfit_with_confidence(x, y, degree, alpha=0.05):
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    
    # Get the covariance matrix
    _, cov = np.polyfit(x, y, degree, cov=True)
    
    # Compute the confidence intervals
    n = len(x)
    t = np.abs(np.t.ppf(alpha / 2, n - degree - 1))
    CI = t * np.sqrt(np.diag(cov))
    
    return p, CI

degree = 3
p, CI = polyfit_with_confidence(x, y, degree)

# Plot data and fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Data with noise')
plt.plot(x, y_true, label='True underlying function', color='g', linewidth=2)
plt.plot(x, y_fit, label='Polynomial fit', color='r', linestyle='--', linewidth=2)

# Plot confidence intervals
plt.fill_between(x, y_fit - CI[0], y_fit + CI[0], color='b', alpha=0.2, label='95% Confidence Interval')

plt.title('Polynomial Curve Fitting with Confidence Interval')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
