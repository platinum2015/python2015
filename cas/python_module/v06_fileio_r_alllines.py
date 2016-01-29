# A test program for reading all lines of a file
# the file we want to write to
a_filename = 'test.txt'

# Read all lines in file and print to screen
f = open(a_filename, 'r')
for line in f:
    print line, #mind the comma at the end
f.close()
