import numpy as np
import matplotlib.pyplot as plt

# Function to generate random Dalitz plot data for illustration
def generate_dalitz_data(n_points):
    # Generate random invariant masses squared (m12^2 and m23^2)
    m12_squared = np.random.uniform(0, 1, n_points)
    m23_squared = np.random.uniform(0, 1, n_points)
    # Generate random efficiency values for each point
    efficiency = np.random.uniform(0, 1, n_points)
    return m12_squared, m23_squared, efficiency

# Number of points to generate
n_points = 1000

# Generate data
m12_squared, m23_squared, efficiency = generate_dalitz_data(n_points)

# Set up plot style to mimic CMS
plt.style.use('seaborn-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Helvetica']
plt.rcParams['text.usetex'] = False  # Use True if you have LaTeX installed

# Plotting the Dalitz plot with efficiency as color scale
fig, ax = plt.subplots(figsize=(8, 6))
sc = ax.scatter(m12_squared, m23_squared, c=efficiency, s=10, alpha=0.6, cmap='coolwarm', marker='o')

# Set plot labels and title
ax.set_xlabel(r'$m_{12}^2$ (GeV$^2$)', fontsize=16)
ax.set_ylabel(r'$m_{23}^2$ (GeV$^2$)', fontsize=16)
ax.set_title('Dalitz Plot with Efficiency Scale', fontsize=18)

# Set plot limits for better visualization
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add color bar to indicate efficiency scale
cbar = plt.colorbar(sc)
cbar.set_label('Efficiency', fontsize=14)

# Add CMS label
#ax.text(0.1, 1.05, 'CMS Preliminary', fontsize=18, fontweight='bold', transform=ax.transAxes)

# Show grid
ax.grid(True)

# Show plot
plt.show()
