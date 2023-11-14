import numpy as np 
import matplotlib.pyplot as plt 

# defining the path to the file 
path_to_file = "../file_generation/datapy.dat"
# reads the ".dat" file and put each column 
# in a different array x and y
x,y = np.loadtxt(path_to_file,unpack=True)

# plots x and y, with a label
plt.plot(x,y,label='y = f(x)')
# set the title
plt.title("Figure Title")
# set the xlabel and ylabel
plt.xlabel("x")
plt.ylabel("y")
# activate the legend 
plt.legend()
# shows the figure
plt.show()
