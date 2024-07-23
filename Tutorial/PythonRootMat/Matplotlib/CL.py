import numpy as np
import matplotlib.pyplot as plt
import uproot

# Load the ROOT file
file_path = "Plots/histo.root"
file = uproot.open(file_path)

# Access the "data" histogram
data_hist = file["data"]

# Extract data
data_edges = data_hist.axis().edges()
data_values = data_hist.values()
data_centers = (data_edges[:-1] + data_edges[1:]) / 2

# Calculate mean, standard deviation, and SEM of histogram values
mean_y = np.mean(data_values)
std_y = np.std(data_values)
n = len(data_values)
sem_y = std_y / np.sqrt(n)

# Choose confidence level and calculate z-score for 95% confidence
confidence_level = 0.95
z_score = 1.96

# Calculate confidence interval
margin_of_error = z_score * sem_y
lower_bound = mean_y - margin_of_error
upper_bound = mean_y + margin_of_error

# Plot histogram
plt.figure(figsize=(10, 7))
plt.hist(data_centers, bins=len(data_centers), weights=data_values, density=True, alpha=0.6, color='b', label='Data')

# Plot confidence interval band
plt.fill_between(data_centers, lower_bound, upper_bound, color='blue', alpha=0.2, label=f'{int(confidence_level*100)}% CI')

# Add labels and legend
plt.xlabel('X axis')
plt.ylabel('Frequency')
plt.title('Data Histogram with Confidence Interval')
plt.legend()

# Display confidence interval values
plt.text(0.95, 0.85, f'CI: {int(confidence_level*100)}% \nLower Bound: {lower_bound:.2f} \nUpper Bound: {upper_bound:.2f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.grid(True)
plt.tight_layout()
plt.show()
