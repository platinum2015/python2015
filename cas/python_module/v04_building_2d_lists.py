#Reference
#http://www.kosbie.net/cmu/fall-11/15-112/handouts/notes-2d-lists.html



# Try, and FAIL, to create a variable-sized 2d list
rows = 3
cols = 2

x = [ [0] * cols ] * rows # Error: creates shallow copy
                          # Creates one unique row, the rest are aliases!
 
print "Using * to create empty list (uses shallow copy):"
print "   x =", x

x[0][0] = 42
print "But see what happens after x[0][0]=42"
print "   x =", x

print




# Create a variable-sized 2d list - append
rows = 3
cols = 2

x=[]
for row in xrange(rows): x += [[0]*cols] #Note, we use xrange, an iterable, the space saving cousin of range

print "Using for and += to append rows (works):"
print "   x =", x

x[0][0] = 42
print "And now see what happens after x[0][0]=42"
print "   x =", x
print

# Create a variable-sized 2d list - list comprehension
rows = 3
cols = 2
x = [ ([0] * cols) for row in xrange(rows) ]
print "Using list comprehension:"
print "   x =", x

x[0][0] = 42
print "And now see what happens after x[0][0]=42"
print "   x =", x
# Create an "arbitrary" 2d List
a = [ [ 2, 3, 5] , [ 1, 4, 7 ] ]
print "Before: a =", a
rows = len(a)
cols = len(a[0])
print "rows =", rows
print "cols =", cols