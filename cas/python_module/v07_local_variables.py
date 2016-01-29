a, b = 'one', 'two'
print "outer a,b=", a, b

def fcn():
    #a, b = 1, 2
    a = 1
    print "inner a,b=", a, b
    c = 3

fcn()
print "outer a,b=", a,b
print "c=", c
