# This program will generate a file 
# Importing the package 
using DelimitedFiles

# with the same function as the python program 
function f(x)
    return sin(x)*(x^2)/(x+1)
end

# Creating the vector with 100 dots 
# from 0 to 10
x = [LinRange(0.0,10.0,100);]
y = f.(x)

open("datajl.dat","w") do file
    # writing the columns in the file  
    # transposing the vectors 
    # x = line 
    # x.T = column 
    writedlm(file,[x y])
end 