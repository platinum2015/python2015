#Create a 1-D array of 10 normally distributed random numbers
#with mean = 5 and standard deviation = 2.5

import numpy as np
x = np.random.normal(5,2.5,size=10)
print x

#Calculate the mean (should be close to 5)

print x.mean() 

#Calculate the standard deviation (should be close to 2.5)

print x.std()

#Find the index of the maximum value

idx = x.argmax()
print idx, x[idx]

# Copy 1-D array and reshape into 5x2 matrix

y = x.copy().reshape(5,2)
print y

#Double the values and add 5

y = 2 * y + 5
print y

#Calculate mean for each column

print y.mean(axis=0)

#Calculate mean for each row

print y.mean(axis=1)
