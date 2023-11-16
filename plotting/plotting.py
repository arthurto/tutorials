import numpy as np 
import matplotlib.pyplot as plt 

# defining the path to the file 
path_to_file = "../file_generation/datapy.dat"
# plt.rcParams['figure.facecolor'] = 'black'
# plt.rcParams['figure.facecolor'] = 'black'
ax=plt.axes()
# reads the ".dat" file and put each column 
# in a different array x and y
x,y = np.loadtxt(path_to_file,unpack=True)

# plots x and y, with a label
plt.scatter(x,y,label='y = f(x)',marker='s')
# set the title
plt.title("Figure Title")
# set the xlabel and ylabel
plt.xlabel("$GeV^2$",fontsize=24)
plt.ylabel("y",fontsize=24)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
# plt.figure(facecolor='red') 
# ax.set_facecolor('pink')

# plt.set_facecolor('black')
# activate the legend 
plt.legend(bbox_to_anchor = (1,0),fontsize=20)
# shows the figure
plt.show()
