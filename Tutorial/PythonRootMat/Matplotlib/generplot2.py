import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
plt.plot(x, y, marker='*', linestyle='--', color='g', label='Slope')

# Customize plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.grid()  # Add grid
plt.legend()    # Add legend

# Display plot
plt.show()
#plt.savefig("plot1.eps")
