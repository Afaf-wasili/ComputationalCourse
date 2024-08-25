import numpy as np
from scipy.special import jv, yv
from scipy.integrate import quad
import matplotlib.pyplot as plt
from numba import jit

# Constants
rho2 = 1
rho1 = 0.8
x13 = 31.4358
km3 = x13
cm1 = -29.7696

# Numerical integration for bm1
@jit
def integrand(x):
    return x * (jv(0.5, km3 * x) + cm1 * yv(0.5, km3 * x))**2

bm1, _ = quad(integrand, rho1, rho2)
am1 = 1 / np.sqrt(np.pi * bm1)

# psi1n function
@jit
def psi1n(rho, phip):
    return am1 * (jv(0.5, km3 * rho) + cm1 * yv(0.5, km3 * rho)) * np.cos(0.5 * phip)

# F1 and F2 functions
@jit
def F1(phi, phip, theta):
    return rho1 * psi1n(rho1, phip) * np.exp(-1j * km3 * rho1 * (np.cos(phi - phip) * np.sin(theta)))

@jit
def F2(phi, phip, theta):
    return rho2 * psi1n(rho2, phip) * np.exp(-1j * km3 * rho2 * (np.cos(phi - phip) * np.sin(theta)))
          
# Ruqayyah function 
@jit      
def Ruqayyah(rho, phi, theta):   
    phip = np.pi - 0.0000001
    return rho * psi1n(rho, phip) * np.exp(-1j * km3 * rho * (np.cos(phi - phip) * np.sin(theta)))
             
# Helper function to integrate complex functions
def complex_quad(func, a, b, **kwargs):
    real_integral = quad(lambda x: np.real(func(x)), a, b, **kwargs)
    imag_integral = quad(lambda x: np.imag(func(x)), a, b, **kwargs)
    return real_integral[0] + 1j * imag_integral[0]

# Function to compute result for a single point 
def compute_result(i, j, theta, phi):
    return np.sin(theta[i, j])**2 * np.abs(
        complex_quad(lambda phip: F1(phi[i, j], phip, theta[i, j]), 0, 2 * np.pi) -
        complex_quad(lambda phip: F2(phi[i, j], phip, theta[i, j]), 0, 2 * np.pi) +
        2 * complex_quad(lambda rho: Ruqayyah(rho, phi[i, j], theta[i, j]), rho1, rho2)   )**2

# Spherical plot
theta = np.linspace(0, np.pi, 250)  # Increased resolution
phi = np.linspace(0, 2 * np.pi, 250)  # Increased resolution
theta, phi = np.meshgrid(theta, phi)

# Compute results
results = np.zeros(theta.shape)
for i in range(theta.shape[0]):
    for j in range(theta.shape[1]):
        results[i, j] = compute_result(i, j, theta, phi)

# Plotting
plt.figure()
plt.contourf(theta, phi, results.real, cmap='viridis')
plt.xlabel('Theta')
plt.ylabel('Phi')
plt.colorbar(label='Result')
plt.savefig("plot2D.png")
plt.show()
