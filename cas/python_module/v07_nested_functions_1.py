import math

def df(f, x, h):
    return (f(x+h) - f(x-h)) / (2.0*h)

print df(math.sin, 0.0, 0.000001) #sin'(x) = cos(x) ==> result should be 1.0
