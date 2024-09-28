import matplotlib.pyplot as plt

# Generation Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
plt.plot(x,y)
#plt.plot(x, y, marker='*', linestyle='--', color='green', label='Slope')   
# Customize plot

plt.xlabel('X-axis') #adding name to x-axis
plt.ylabel('Y-axis') #adding name to y-axis
plt.title('slope') #dding name as title for the plot
plt.grid()  # Add grid
#plt.legend()    # Add legend to the plot
#plt.legend(x, y, label="Slope")
# Display plot
plt.show()
# save plot
#plt.savefig("/Users/afafwasili/ComputationalMC/Tutorial/PythonROOTMat/Matplotlib/Plots/XY.png")

