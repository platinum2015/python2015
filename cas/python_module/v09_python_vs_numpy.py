import time
import numpy

def trad_version():
    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = numpy.arange(10000000)
    Y = numpy.arange(10000000)
    Z = X + Y
    return time.time() - t1
    
print "Adding two large lists/arrays"
print "Traditional ",trad_version(),"seconds"
print "Numpy ",numpy_version(),"seconds"