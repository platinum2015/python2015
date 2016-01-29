def get_braking_distance(v0):
    '''
    Calculates braking distance [m]
    with mu = 0.3 and v0 [km/h]
    '''
    mu = 0.3 #Coefficient of friction
    g = 9.81 # gravitational acceleration
    return 0.5*v0**2 / (mu*g)

velocity = 100 #km/h
print "The braking distance for v0=",velocity,"is",get_braking_distance(velocity),"m"
