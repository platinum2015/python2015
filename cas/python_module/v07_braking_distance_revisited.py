def get_braking_distance(v0,mu):
    '''
    Calculates braking distance [m]
    with mu and v0 [km/h]
    '''
    g = 9.81 # gravitational acceleration
    return 0.5*v0**2 / (mu*g)

velocity = 100 #km/h
friction = 0.2
print "The braking distance for v0=",velocity,
print "and friction mu=",friction,
print "is",get_braking_distance(velocity,friction),"m"
