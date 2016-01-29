# A test program to handle IOExceptions


# A file name, file does not exist
a_filename = "does_not_exist.txt"

# Use try to see if the file can be opened
try:
    f = open(a_filename, 'r')
except IOError, detail:
    print "Cannot open file "+a_filename, detail
else:
    with f:
        
        print "** Reading the file content with a for loop, found:"
        
        for line in f:
            print line, #notice the comma, if ommited, there is an empty line
        print "** done."
