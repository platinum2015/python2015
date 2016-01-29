# A test program for reading all lines of a file
# the file we want to read from
a_filename = 'test.txt'

# Read all lines in file and print to screen
with open(a_filename, 'r') as f:
    for line in f:
        print line, #mind the comma at the end
