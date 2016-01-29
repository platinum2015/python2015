def function(a):
    if a:
        return
    else:
        return (a, not a)

x = function(True)
y = function(False)
z1, z2 = function(False)
print "x: ", x, type(x)
print "y: ", y, type(y)
print "z1, z2: ", z1, type(z1), z2, type(z2)


