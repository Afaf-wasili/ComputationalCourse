import matplotlib.pyplot as plt
import numpy as np

# generate data points
x1 = np.linspace(1, 10)
y1, y2, y3 = np.log(x1), np.cos(x1), np.sin(x1)
#Styling
#plt.style.use('seaborn')
#plt.style.use('ggplot') 
#plt.style.use('Solarize_Light2') 
plt.style.use('dark_background')
# plotting
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x1, y2)
ax.plot(x1, y3)
#Axes Labels 
ax.set_xlabel("X values")
ax.set_ylabel("Y values")
#Legend
ax.plot(x1, y1, label="log")
ax.plot(x1, y2, label="cos")
ax.plot(x1, y3, label="sin")
ax.legend()
#Title
ax.set_title("A figure with multiple lines")
#Grid
ax.grid()
plt.show()
#plt.savefig("")
