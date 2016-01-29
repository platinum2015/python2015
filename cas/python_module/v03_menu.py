while True:
    s = raw_input("Please enter a number between 1 and 5: ")
    if s in ['1', '2', '3', '4', '5']:
        i = int(s)
        break
print "You chose number", i
