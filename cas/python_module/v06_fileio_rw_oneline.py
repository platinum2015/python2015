# A test program for writing to files
# the file we want to write to
a_filename = 'test.txt'

# Write a string to file
f = open(a_filename,'w')
f.write("This is a test\n")
f.close()

# Read the string back
f = open(a_filename, 'r')
line = f.readline()
print line,
f.close()

