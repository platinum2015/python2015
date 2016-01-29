# Compute the distance it takes to stop a car
#
# A car driver, driving at velocity v0, suddenly puts on the brake. What 
# braking distance d is needed to stop the car? One can derive, from basic 
# physics, that
#   d=0.5*v_0^2 / mu * g
#
# Develop a program for computing d using the above formula when the initial 
# car velocity v0 and the friction coefficient mu are provided via the 
# raw_input function.
#
# Run the program for two cases: v0 = 120 and v0 = 50 km/h, both with mu = 0.3
# (mu is dimensionless).
#
# Hint: Remember to convert the velocity from km/h to m/s before inserting the 
# value in the formula!

g = 9.81 # Assigns g value

# Inputs become floats
v0_in_kmh = float(raw_input("Please enter the initial velocity(v0) in km/h "))
mu = float(raw_input("Please, enter the friction coefficient (mu) "))

# Conversion from km/h to m/s
v0 = (v0_in_kmh*1000.)/3600. 

# Computes braking distance
distance = (0.5*v0**2)/(mu*g) 

# Prints the result
print "The braking distance of a car traveling at %.2f km/h is %.2f m" % (v0_in_kmh, distance) 
