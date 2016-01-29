# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 10:56:36 2014

@author: stdm
"""

def loop_power(a, n):
    '''Raises a to the power of n using a simple loop
       Returns the result as well as the number of multiplications'''
    power = 1    
    for i in range(n):
        power *= a
    return power, n
    
def recursion_power(a, n):
    '''Raises a to the power of n using recursion.
       Idea: a^n = a^(n/2)*a^(n/2)   (if n is even)
             a^n = a^(n/2)*a^(n/2)*a (if n is uneven)
       This is very fast because of less multiplications!
       Returns the result as well as the number of multiplications'''
    if n == 0:
        return 1, 0
    else:
        if n%2 != 0:
            x, mc = recursion_power(a, n-1)
            return a * x, mc+1
        else:
            half_power, mc = recursion_power(a, n/2)
            return half_power * half_power, mc+1
    
print "Iterative version: "    
print loop_power(2, 1000000)[1]
print "Recursive version: "
print recursion_power(2, 1000000)[1]