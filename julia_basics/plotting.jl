# To plot the graph of a function 
# you in julia you will need to use the package 
# Plots 
using Plots 

# then you will have to define the function  
# that you want to plot, for example 
# f(x) = sin(x)/x 

f = x-> x*sin(x) 

# now we simply define the argument that 
# will state the range and the step of the 
# x array we want to evaluate the function 

plot(0:0.1:4,f,
     xlabel = "x",ylabel= "f(x)",
     color = :black, label = "\$x\\sin(x)\$")

# To plot another function on the same graph as 
# the latest one we must use plot!, to write 
# another curve instead of deleting the old one 

plot!(0.0001:0.1:4,x-> sin(x)/x,
      label = "\$\\frac{sin(x)}{x}\$")
