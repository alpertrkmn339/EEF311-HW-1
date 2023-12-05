import numpy as np 
import matplotlib.pyplot as plt 
## I assigned the gravitational accelaration constant globally to use in both functions as 9.8 m/s^2
gravitational_acc = 9.8
def height_equation(t,h_init): ## Function for finding the h(t)
    return h_init - ((gravitational_acc*np.power(t,2))/2) ## height equation function returns the height at a given time with the provided initial height
## h(t,ho) = h0 - 1/2*g*t^2
def bisection_method_for_falling_object(err_tolerance,h_init): 
    ## The function iterates till the error is smaller than the error tolerance
    a = 0.0 ## Chose a and b as the guessed interval boundaries 
    b = 2 * (h_init / gravitational_acc) ## Interval's closing bound
    u = height_equation(a,h_init) ## u = h(a,h0) 
    v = height_equation(b,h_init) ## v = h(b,h0)

    if u*v >= 0: ## Bisection methods first rule to be satisfied if this is not satisfied im executing the program   
        exit(1) ## Code exists if there is no possible real zeros in given interval 
    intermed_val = (a + b)/2 ## Defining a midpoint
    w = height_equation(intermed_val) ## Assigning a new w variable to indicate the intervals new starting bound
    while(abs(w)>err_tolerance):  ## Iterating till the errors absolute value is smaller than err_tolerance which is taken from the user
        
        if u*w < 0: ## Checking if there are any zeros in the new interval 
            b = intermed_val ## Assigning the new closing boundary as the midpoint
            v = w ## Assigning the v as w
            intermed_val = (a+b)/2 ## Updating the midpoint
            w = height_equation(intermed_val,h_init) ## Updating the function output of the new midpoint 
        elif u*w > 0: ## Checking if there are any zeros between the other half of two intervals which we produced
            a = intermed_val ## Assigning the new midpoint
            u = w ## Assigning the u as w
            intermed_val = (a+b)/2 ## Updating the midpoint
            w = height_equation(intermed_val,h_init) ## Updating the function output of the new midpoint 
             
    return intermed_val # I am returning the midpoint which denotes the time value which is closer to root


def plot_the_motion_graph(h_init): ## Function for plotting the motion of a free falling object depending on the initial height
    x_start = 0 ## Defining an interval start
    x_stop = 60 / gravitational_acc  ## Closing the interval, 60 chosen randomly
    increment = 0.1 ## Choosing increment as 0.1 to get more smooth curve 
    x = np.arange(x_start, x_stop, increment) ## Defining x as an interval
    y = list(map(lambda x: height_equation(x,h_init),x)) ## Mapping the x values in a function and getting the y values. We have to typecast the map output because we need an array-like object
    plt.plot(x, y) ## We are plotting the graph
    plt.grid() ## We are generating the grid lines 
    plt.xlabel('Time') ## Labelling x axis
    plt.ylabel('Height') ## Labelling y axis 
    plt.show() ## Showing the graph