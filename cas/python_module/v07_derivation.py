import math

def df(f, x , h):
    '''Computes the numerical approximation of the derivative of f at point x:
       f\'(x), using a small increment h around the value x'''
    return (f(x+h) - f(x-h)) / (2.0*h)

f = math.sin
for x in [0.0, 0.5*math.pi, math.pi]: #take some values in [0, pi]
    dx = df(f, x, 0.000001) #compute the numerical derivative of sin(x)
    print "f'(",x,")=", dx, " should be: ", math.cos(x) #check if it's near cos(x)
