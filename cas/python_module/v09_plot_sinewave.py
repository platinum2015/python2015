# 1. Import
import matplotlib.pyplot as plt
import numpy as np

# 2. Get the data
x = np.linspace(0,360,90) # angle from 0 to 360 every 4 degrees
y = np.sin(x*np.pi/180) # need to convert from deg to radian

# 3 Create Figure
plt.figure()

# 3.1 Plot data
plt.plot(x,y)

# 3.2 Set title, x and y label
plt.title('A sine wave')
plt.xlabel('Angle [deg]')
plt.ylabel('sin(x)')

# 3.2 Other formating
plt.grid(True)

# 4 Make plot visible
plt.show()
