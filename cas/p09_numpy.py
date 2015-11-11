# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:34:49 2015

@author: programming
"""

import numpy as np
x = np.random.normal(5, 2.5, size=10)
print x
print "Calculate the mean (should be close to 5)"
print x.mean()
print " Calculate the standard deviation (should be close to 2.5)"
print x.std()
print "Find the index of the maximum value"
idx = x.argmax()
print idx, x[idx]
print "Copy 1-D array and reshape into 5x2 matrix"
y = x.copy().reshape(5, 2)
print y
print "Double the values and add 5"
y = 2*y + 5
print  y
print "Calculate mean for each column"
print y.mean(axis=0)
print "Calculate mean for each row"
print y.mean(axis=1)