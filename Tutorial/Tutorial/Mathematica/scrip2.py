import numpy as np
from scipy.special import jn, yn
from scipy.integrate import quad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
rho1 = 0.8
rho2 = 1
km3 = 31.4358
a = rho1 / rho2
pi = np.pi

# Numerical derivative of Bessel functions
def numerical_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

# Derivative of Bessel J function
def d_bessel_j1_2(x):
    return numerical_derivative(lambda t: jn(0.5, t), x)

# Derivative of Bessel Y function
def d_bessel_y1_2(x):
    return numerical_derivative(lambda t: yn(0.5, t), x)

def cm1(x):
    return (-d_bessel_j1_2(x) / d_bessel_y1_2(x)) - (2 * pi * np.cos(x) / x) - (2 * pi * np.sin(x) / x)

def integrand(x, km3, cm1):
    return x * (jn(0.5, km3 * x) + cm1 * yn(0.5, km3 * x))**2

# Compute bm1 using numerical integration
def bm1_integrand(x):
    cm1_value = cm1(x)
    return integrand(x, km3, cm1_value)

bm1, _ = quad(bm1_integrand, rho1, rho2)
am1 = 1 / np.sqrt(bm1)

def psi1n(rho, phip):
    return am1 * (jn(0.5, km3 * rho) + cm1(rho) * yn(0.5, km3 * rho)) * np.cos(0.5 * phip)

def F1(phi, theta, phip):
    return rho1 * psi1n(rho1, phip) * np.exp(-1j * km3 * rho1 * (np.cos(phi - phip) * np.sin(theta)))

def F2(phi, theta, phip):
    return rho2 * psi1n(rho2, phip) * np.exp(-1j * km3 * rho2 * (np.cos(phi - phip) * np.sin(theta)))

def psi1np(phip):
    return psi1n(rho1, np.pi - 0.0000001)

def Ruqayyah(rho, phi, theta):
    return rho * psi1np(np.pi - 0.0000001) * np.exp(-1j * km3 * rho * (np.cos(phi - np.pi + 0.0000001) * np.sin(theta)))

# Create a grid for plotting
theta = np.linspace(0, pi, 100)
phi = np.linspace(0, 2*pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Define the function to integrate
def integrand_F1(theta, phi, phip):
    return np.abs(F1(phi, theta, phip))**2

def integrand_F2(theta, phi, phip):
    return np.abs(F2(phi, theta, phip))**2

def integrand_Ruqayyah(theta, phi, rho):
    return np.abs(Ruqayyah(rho, phi, theta))**2

def integral_F1(theta, phi):
    return np.trapz([integrand_F1(t, p, phi) for t, p in zip(theta, phi)], phi[0])

def integral_F2(theta, phi):
    return np.trapz([integrand_F2(t, p, phi) for t, p in zip(theta, phi)], phi[0])

def integral_Ruqayyah(rho, theta, phi):
    return np.trapz([integrand_Ruqayyah(t, p, rho) for t, p in zip(theta, phi)], rho)

# Calculate the integrals
int_F1 = np.array([integral_F1(t, p) for t, p in zip(theta, phi)])
int_F2 = np.array([integral_F2(t, p) for t, p in zip(theta, phi)])
int_Ruqayyah = np.array([integral_Ruqayyah(rho1, t, p) for t, p in zip(theta, phi)])

# Define the function for plotting
def plot_function(theta, phi):
    return np.sin(theta)**2 * np.abs(int_F1 - int_F2 + 2 * int_Ruqayyah)**2

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(phi, theta)
Z = plot_function(theta, phi)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Phi')
ax.set_ylabel('Theta')
ax.set_zlabel('Value')
plt.show()
