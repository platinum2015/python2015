# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 10:20:38 2014

@author: stdm
"""

def celsius_2_fahrenheit(celsius):
    '''Converts degrees Celsius to degrees Fahrenheit.
       Receives and returnes a float.
    '''
    return 1.8 * celsius + 32

celsius = float(input("Please enter temperature in degrees Celsius: "))
fahrenheit = celsius_2_fahrenheit(celsius)
print str(celsius) + " degrees Celsius are " + str(fahrenheit) + " degrees Fahrenheit."