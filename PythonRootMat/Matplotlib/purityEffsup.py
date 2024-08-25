import matplotlib.pyplot as plt
import numpy as np

# Generate example signal and background data
np.random.seed(0)
signal = np.random.normal(loc=5, scale=1, size=10000)
background = np.random.normal(loc=0, scale=1, size=100000)

# Define a function to calculate efficiency, purity, and efficiency * purity
def calculate_metrics(signal, background, threshold, suppression):
    signal_count = np.sum(signal > threshold)
    background_count = np.sum(background > threshold)
    background_count_suppressed = np.sum(background[suppression * background > threshold])
    
    efficiency = signal_count / len(signal)
    purity = signal_count / (signal_count + background_count_suppressed)
    efficiency_purity = efficiency * purity
    
    # Calculate suppression efficiency
    suppression_efficiency = 1 - (background_count_suppressed / background_count)
    
    return efficiency, purity, efficiency_purity, suppression_efficiency

# Define thresholds to evaluate
thresholds = np.linspace(0, 10, 100)
efficiencies = []
purities = []
efficiency_purities = []
suppression_efficiencies = []

# Define suppression factor
suppression = 0.1  # Example suppression factor

# Calculate metrics for each threshold
for threshold in thresholds:
    efficiency, purity, efficiency_purity, suppression_efficiency = calculate_metrics(signal, background, threshold, suppression)
    efficiencies.append(efficiency)
    purities.append(purity)
    efficiency_purities.append(efficiency_purity)
    suppression_efficiencies.append(suppression_efficiency)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot signal and background
ax1.hist(signal, bins=50, color='b', alpha=0.5, label='Signal')
ax1.hist(background, bins=50, color='g', alpha=0.5, label='Background')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.set_title('Signal and Background Distribution')
ax1.legend(loc='upper right')  # Adjust legend position

# Plot metrics and suppression efficiency
ax2.plot(thresholds, efficiencies, label='Efficiency', color='tab:blue')
ax2.plot(thresholds, purities, label='Purity', color='tab:orange')
ax2.plot(thresholds, efficiency_purities, label='Efficiency * Purity', color='tab:green')
ax2.set_xlabel('Threshold')
ax2.set_ylabel('Metric Value')

# Create a secondary y-axis for suppression efficiency
ax2_secondary = ax2.twinx()
ax2_secondary.plot(thresholds, suppression_efficiencies, label='Suppression Efficiency', color='tab:red', linestyle='--')
ax2_secondary.set_ylabel('Suppression Efficiency')

# Adjustments
ax2.grid(True)
ax2.set_title('Metrics and Suppression Efficiency vs. Threshold')
ax2.legend(loc='upper left')  # Adjust legend position
ax2_secondary.legend(loc='upper right')  # Adjust legend position

plt.tight_layout()
plt.show()
