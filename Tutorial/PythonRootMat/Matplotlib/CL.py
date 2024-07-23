import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
x = np.linspace(0, 10, 100)
slope = 2.0
intercept = 1.0
noise = np.random.normal(0, 1, size=len(x))
y = slope * x + intercept + noise  # Linear relationship with noise

# Calculate mean, standard deviation, and SEM
mean_y = np.mean(y)
std_y = np.std(y)
n = len(y)
sem_y = std_y / np.sqrt(n)

# Choose confidence level and calculate z-score for 60% confidence
confidence_level = 0.95 # 0.60  # 60% confidence interval
z_score = 1.96 #0.84  # z-score for 60% confidence level

# Calculate confidence interval
margin_of_error = z_score * sem_y
lower_bound = mean_y - margin_of_error
upper_bound = mean_y + margin_of_error

# Plot data
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Data', color='b', alpha=0.7)

# Plot confidence interval band
plt.fill_between(x, lower_bound, upper_bound, color='blue', alpha=0.2, label=f'{int(confidence_level*100)}% CI')

# Add true line (slope * x + intercept)
plt.plot(x, slope * x + intercept, color='r', linestyle='--', label='True Line')

# Add labels and legend
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Random Data with 60% Confidence Interval')
plt.legend()

# Display plot
plt.grid(True)
plt.show()
