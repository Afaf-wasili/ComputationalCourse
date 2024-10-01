import matplotlib.pyplot as plt
import numpy as np

# generate data points
x1 = np.linspace(1, 10) #
#x11 = [1,2,3,4,5,6,7,8,9,10]

y1 = np.log(x1)
y2 = np.cos(x1)
y3 = np.sin(x1)

#Styling
#plt.style.use('seaborn')
#plt.style.use('ggplot') 
#plt.style.use('Solarize_Light2') 
# plotting
fig, ax = plt.subplots()

ax.plot(x1, y1, label="", color="Black")
ax.plot(x1, y2, label="cos", color="GREEN")
#ax.plot(x1, y3, label="sin", color= "BLUE")
#Axes Labels 
ax.set_xlabel("X values") 
ax.set_ylabel("Y values")
#Legend
ax.legend()
#Title
ax.set_title("A figure with multiple lines")
#Grid
ax.grid()
plt.show()
#plt.savefig("Plots/moreplots.png")



