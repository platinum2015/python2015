def find_closest_point(all_points,p):
    '''
    Finds the 2D point in a the list all_points that is closest to p
    returns closest point and the distance
    '''
    import math
    xp, yp = p #unpacking tuple
    min_dist = 1e10 # something large
    for xi, yi in all_points: #unnacking tuple
        dist = math.sqrt((xp-xi)**2 + (yp-yi)**2)
        if dist < min_dist:
            min_dist = dist
            min_p = (xi,yi) #packing tuple
    return min_p, min_dist

# Main starts here
some_points = [(2,3),(0,1),(5,3),(3,-2)]
desired_point = (0,0)

p_close, p_dist = find_closest_point(some_points,desired_point) #unpacking tuple

print "Out of these points"
for x, y in some_points:
    print "(",x,",",y,")"
print "the point (",p_close[0],",",p_close[1],")"
print "is closest to (",desired_point[0],",",desired_point[1],")"
print "at a distance of",p_dist
