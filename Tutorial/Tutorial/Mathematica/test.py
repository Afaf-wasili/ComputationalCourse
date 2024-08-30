import numpy as np
import matplotlib.pyplot as plt
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl

# Start a Wolfram Language session
with WolframLanguageSession() as session:
    
    # Define the integral in Mathematica
    integral_result = session.evaluate(wl.Integrate(wl.Sin(wl.x)**2, (wl.x, 0, wl.Pi)))
    
    # Print the result from Mathematica
    print("The integral of sin^2(x) from 0 to Pi is:", integral_result)

# Use the result in a Python function
def f(x, integral_result):
    return np.sin(x) ** 2 + float(integral_result)  # Add the integral result as a constant

# Generate x values
x = np.linspace(0, 2 * np.pi, 400)

# Compute y values using the function
y = f(x, integral_result)

# Plot the function
plt.plot(x, y, label=f'sin^2(x) + {integral_result}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = sin^2(x) + Integral Result')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
