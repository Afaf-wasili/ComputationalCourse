import matplotlib.pyplot as plt
import numpy as np

# Generate example signal and background data
np.random.seed(0)
signal = np.random.normal(loc=5, scale=1, size=10000)
background = np.random.normal(loc=0, scale=1, size=100000)

# Define a function to calculate efficiency, purity, and efficiency * purity
def calculate_metrics(signal, background, threshold):
    signal_count = np.sum(signal > threshold)
    background_count = np.sum(background > threshold)
    
    efficiency = signal_count / len(signal)
    purity = signal_count / (signal_count + background_count)
    efficiency_purity = efficiency * purity
    
    return efficiency, purity, efficiency_purity

# Define thresholds to evaluate
thresholds = np.linspace(0, 10, 100)
efficiencies = []
purities = []
efficiency_purities = []

# Calculate metrics for each threshold
for threshold in thresholds:
    efficiency, purity, efficiency_purity = calculate_metrics(signal, background, threshold)
    efficiencies.append(efficiency)
    purities.append(purity)
    efficiency_purities.append(efficiency_purity)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plot signal and background
ax1.hist(signal, bins=50, color='b', alpha=0.5, label='Signal')
ax1.hist(background, bins=50, color='g', alpha=0.5, label='Background')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.set_title('Signal and Background Distribution')
ax1.legend()

# Plot metrics
ax2.plot(thresholds, efficiencies, label='Efficiency')
ax2.plot(thresholds, purities, label='Purity')
ax2.plot(thresholds, efficiency_purities, label='Efficiency * Purity')
ax2.set_xlabel('Threshold')
ax2.set_ylabel('Metric Value')
ax2.set_title('Efficiency, Purity, and Efficiency * Purity vs. Threshold')
ax2.legend()

# General adjustments
plt.tight_layout()
plt.show()
