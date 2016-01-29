#Import numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt

#Create 2 1-D arrays with normally distributed values

x = np.random.normal(5,2.5,size=40)
y = np.random.normal(5,2.5,size=40)

#Create a scatter-plot

plt.figure()
plt.plot(x,y,'o')
#plot.show()

#Add a title
plt.title('A scatter plot')

#Create a histogram

plt.figure()
plt.hist(x,bins=10)
#plt.show()

#Create a pie plot with count of values above/below mean

plt.figure()
plt.pie([np.sum(x>5),len(x)-np.sum(x>5)],
        labels=['above','below'],
        autopct='%1.1f%%',
        colors=['rosybrown','sandybrown']) # http://matplotlib.org/examples/color/named_colors.html
plt.show()
