'''                                                                                                   
import uproot                                                                                         
import numpy as np                                                                                    
import matplotlib.pyplot as plt                                                                       
'''
# Questions :                                                                                         
# 1. Access and define the Histogram:                                                                 
# 2. Extract Data:                                                                                    
# 3. Customization:                                                                                   
#    - Do the labels, title, and grid add to the visualization.                                       
# 4. Save the Plot:                                                                                   
#    - Modify the script to save the "Data Histogram" plot as a PNG file named "DataHistogram.png".   
'''                                                                                                   
file_path = "Plots/histo.root"                                                                        
                                                                                                      
# Open the ROOT file                                                                                  
file = uproot.open(file_path)                                                                         
                                                                                                      
# Access histograms:                                                                                  
data_hist = file.Get("data")                                                                          
# Extract data:                                                                                       
data_hist.SetTitle("data")                                                                            
                                                                                                      
#Plot histograms for Data:                                                                            
plt.figure(figsize=(10, 7))                                                                           
plt.step(data_edges[:-1], data_values, color='blue', label='Data')  # Plot Datahistogram              
plt.Draw()                                                                                            
#Customization:                                                                                       
Canvas.SavaAs(" Q3S2.png")                                                                            
'''
import uproot
import numpy as np
import matplotlib.pyplot as plt


file_path = "/Users/ndawyalmhzry/Master_project/ComputationalCourse/Tutorial/C++ROOT/histo.root"


file = uproot.open(file_path)


hist_data = "data" 

if hist_data in file:
    data_hist = file[hist_data]
else:
    raise ValueError(f"Histogram '{hist_data}' not found in the ROOT file. Available keys: {file.keys()}")

data_values = data_hist.values() 
data_edges = data_hist.axis().edges() 


plt.figure(figsize=(10, 7))
plt.step(data_edges[:-1], data_values, color='blue', label='Data')  # Plot histogram


plt.xlabel("X-axis Label") 
plt.ylabel("Y-axis Label") 
plt.title("Data Histogram") 
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()


output_file = "DataHistogram.png"
plt.savefig(output_file, dpi=300)


plt.show()

print(f"Plot saved as {output_file}")
