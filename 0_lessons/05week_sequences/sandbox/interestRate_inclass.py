#!/usr/bin/env python3
# interest of money in bank calculater

# functions

def calcInterest(x0, p, N):
    """ function to calculate interest and return a list"""
    print("\t calcInterest()")
    x_list = []
    x_list.append(x0) # add the first amount of money to the list
    for i in range(N):
        lastElement = x_list[len(x_list)-1] # last recorded element
        x = lastElement + (p/100) * lastElement
        x_list.append(x)
    return x_list
#define the variables for the interest calculation


def plotter(x_list):
    """plotting function"""
    import matplotlib.pyplot as plt
    plt.plot(x_list, 'ro')
    plt.show()


x0 = 100000 # first payment
p = 3.92 # interest rate
N = 6 # number of years


# start of my program
x_list = calcInterest(x0, p, N)
print("My returned x_list is: ",x_list)
plotter(x_list)
