# This program is writes a file in 
# .dat format
import numpy as np

# example function 
def f(x):
    return (x**2/(1+x))*np.sin(x)

# creates a vector with 100 points 
# equally spaced from 0 to 10 
# using np.linspace
# Reference:
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
x = np.linspace(0,10,100)

# creates the y with those points 
y = f(x)

# The 'np.savetxt' creates the file and 
# the np.columnstack creates a the columns for 
# each x,y array

# Reference 
# savetxt:
# https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html
# column_stack: 
# https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html
np.savetxt("datapy.dat",np.column_stack([x,y]))