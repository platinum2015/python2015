import csv as csv 
import numpy as np
import os #platinum
import time

train = 'titanic3_train.csv'
directory = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(directory,train)

# Open up the CSV file into a Python object 
with open(filename, 'rb') as f:
    csv_file_object = csv.reader(f, delimiter=';') 
    header = csv_file_object.next() #next() skips the first line holding the column headers 
    data=[]
    for row in csv_file_object: #Run through each row in the CSV, add it to the data variable
        data.append(row) # Then convert from a list to an array # (Be aware that each item is currently a string in this format)
    data = np.array(data)

print "---- row 1"
#print data[0:10,(4,5,8)]
print data[0:3:3,4]
x=0
for i in data[0:176:2,4]:
   x=x+1   
   print i,x
