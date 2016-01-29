def getMinAndMax(values):
    return min(values), max(values) #Tuple packing

temperatures_this_week = [22,20,19,19,18,17,20]

min_and_max = getMinAndMax(temperatures_this_week) 
min_temp, max_temp = min_and_max #Tuple unpacking

print "This week we expect a low of",min_temp,"and a high of",max_temp 
