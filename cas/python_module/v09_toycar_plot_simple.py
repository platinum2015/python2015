#
# A spring-loaded toy car accelerating is recorded with a camera.
# From this video, the distance of the car was measured on screen with
# a ruler and saved to an Excel file along with the frame number
#
# This program loads this distance data, calculates velocity and acceleration 
# and plots the resulting curves in x-y plots.
#
# Ideas: Calculate average velocity, acceleration
#        Fit curves to data (numpy.polyfit)
#
# References
# Web: http://serc.carleton.edu/dmvideos/activities/example10.html
# Video: http://d32ogoqmya1dw8.cloudfront.net/files/sp/library/direct_measurement_video/examples/direct_measurment_video_toy.mov

import numpy as np
import matplotlib.pyplot as plt
import xlrd

# Conversion constants
screen_to_real_ratio = 20.0/50.0 #20cm on screen are 50cm in real life (depends on screen size!)
frames_per_second = 240 # used to convert frame number to seconds



# Read frame number and screen distance from Excel sheet
wb = xlrd.open_workbook('v09_toycar.xls')
sheet = wb.sheet_by_index(0)

frames = np.zeros(sheet.nrows-1) #notice the -1, we leave out the header
screen_distance_mm =np.zeros(sheet.nrows-1)
for i in range(1,sheet.nrows):
    frames[i-1] = float(sheet.cell(i,0).value)
    screen_distance_mm[i-1]=float(sheet.cell(i,1).value)

# Convert frame number to seconds  
# (note the vectorized computation here and below: the result is a NumPy array!)
times = frames / frames_per_second
# Convert screen distance to actual distance in meters
actual_distance_m = screen_distance_mm/(screen_to_real_ratio*1000)

# Calculate velocity and acceleration from position using finite differences.
delta_t = times[1]-times[0]
velocity_m_per_s = np.diff(actual_distance_m)/delta_t
acceleration_m_per_s2 = np.diff(actual_distance_m,2)/(delta_t*delta_t)

# Calculate average velocity and acceleration
mean_velocity = np.mean(velocity_m_per_s)
mean_acceleration = np.mean(acceleration_m_per_s2)


# Plot position, velocity and acceleration
# Distance vs Time
plt.figure()

plt.plot(times,actual_distance_m,marker='*')

plt.title('Distance vs time')
plt.xlabel('time [s]')
plt.ylabel('distance [m]')
plt.grid(True)

# Velocity vs Time
plt.figure()

plt.plot(times[1:],velocity_m_per_s,marker='*')

plt.title('Velocity vs time, mean= '+str(round(mean_velocity,2))+' m/s')
plt.xlabel('time [s]')
plt.ylabel('velocity [m/s]')
plt.ylim(ymin=0)
plt.grid(True)

# Acceleration vs Time
plt.figure()

plt.plot(times[2:],acceleration_m_per_s2,marker='*')

plt.title('Acceleration vs time, mean= '+str(round(mean_acceleration,2))+' m/s^2')
plt.xlabel('time [s]')
plt.ylabel('acceleration [m/s^2]')
plt.ylim(ymin=0)
plt.grid(True)


plt.show()
