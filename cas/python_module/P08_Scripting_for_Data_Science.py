# -*- coding: utf-8 -*-
"""
spec:
    Write a Python script that predicts from the data in the 
    training set titan-ic3_train.csv for any individual 
    if he or she has survived or not 

    Examples for ideas to explore are:
        * Things you want to engross (e.g., functions, loops, certain data structures)
        * Things you to newly explore (e.g., list comprehension, lambda expressions)
        * Use different libraries (e.g., Pandas)


test_set:
    titanic3_test.csv

output:
    CSV file separated by a semicolon (not surrounded by whitespaces!)
        header row “key;value”        
        id,predicted value (0 or 1)
        
            Example:
                key;value 
                100001;0 
                100002;1 
                100003;0

    Name :<nickname><_nn>
          platinum_01

    submit adress:
        http://srv-lab-t-864/submission/Titanic/
        
    leaderboard:
        http://srv-lab-t-864/leaderboard/Titanic/
        
links:
--> SOL     https://www.kaggle.com/c/titanic-gettingStarted/details/getting-started-with-python
    https://www.kaggle.com/c/titanic-gettingStarted/details/getting-started-with-python-ii
    https://www.kaggle.com/c/titanic-gettingStarted/details/getting-started-with-random-forests
    http://nbviewer.ipython.org/github/agconti/kaggle-titanic/blob/master/Titanic.ipynb
    http://triangleinequality.wordpress.com/2013/09/05/a-complete-guide-to-getting-0-79903-in-kaggles-titanic-competition-with-python/

learned:
    [0::,2]

"""

###############################################################################
# 4.1 Reading in the training data
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
    print data

print "---- row 1"
print data[0]
print "---- row 1:4"
print data[0:3]
###############################################################################
#4.2 Play with the training data
print "---- column"
print "gender"
print data[0::,5]
number_passengers = np.size(data[0::,2].astype(np.float))
number_survived = np.sum(data[0::,2].astype(np.float))
proportion_survivors = number_survived / number_passengers
print "proportion_survivors"
print proportion_survivors


# This finds where all the elements in the gender column equal “female” 
women_only_stats = data[0::,5] == "female" 
# This finds where all the elements do not equal female (i.e. male) 
men_only_stats = data[0::,5] != "female"

# Using the index from above we select the females and males separately 
women_onboard = data[women_only_stats,2].astype(np.float) 
men_onboard = data[men_only_stats,2].astype(np.float)
# Then we finds the proportions of them that survived 
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard) 
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard) # and then print it out 
print 'Proportion of women who survived is %s' % proportion_women_survived 
print 'Proportion of men who survived is %s' % proportion_men_survived
###############################################################################
#4.3 The first submission using the test data

# Open up the CSV file in to a Python object 
test = 'titanic3_test.csv'
prediction = 'platinum_01_gender.csv'
directory = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(directory,test)
prediction_file =  os.path.join(directory,prediction)

# Open up the CSV file into a Python object 
with open(filename, 'rb') as f:#platinum
    test_file_object = csv.reader(f, delimiter=';') 
    header = test_file_object.next() #next() skips the first line holding the column headers 

    prediction_file = open(prediction_file, "wb") 
    prediction_file_object = csv.writer(prediction_file, delimiter=';')

    prediction_file_object.writerow(["key", "value"])
    for row in test_file_object:
        if row[4] == 'female':
            prediction_file_object.writerow([row[0],'1']) # predict 1
        else: #it is male 
            prediction_file_object.writerow([row[0],'0']) # predict 0 
    prediction_file.close()
############################################################################### 
# 4.4 Submission two (optional)
#fill up empty fare values with the mean of the corresponding pclass 
#1. calculate mean fare of each pclass 
fare_mean_per_pclass = []
for i in range(len(np.unique(data[0::,1]))): #loop over all possible pclass's (i == pclass-1) 
    fare_mean_per_pclass.append(0) #initialize ith pclass     fare mean 
    cnt = 0 #number of tickets with a value in pclass i 
    for j in range(len(data[0::,10])):
        if data[j, 1].astype(np.int) == i+1:
            try: #try to cast the jth fare value as float 
                fare_mean_per_pclass[i] += data[j, 10].astype(np.float) 
                cnt += 1 
            except: #if it can't be casted to float: ignore it 
                fare_mean_per_pclass[i] += 0 #just ignore empty values 
    if cnt > 0:fare_mean_per_pclass[i] /= float(cnt) #calculate mean 
print "Mean fare per pclass: ", fare_mean_per_pclass

for i in range(len(data[0::,10])): #2. replace the empty values with the pclass mean
    try: 
        #print "beg" ,i,data[i, 3],data[i, 1].astype(np.int) 
        #print fare_mean_per_pclass[data[i, 1].astype(np.int)]       
        test = float(data[i, 10]) #if this works, all is well with row i 
        #print "end"
    except ValueError:
        data[i, 10] = fare_mean_per_pclass[data[i, 1].astype(np.int)-1] #index: current pclass-1
        #platinum
# So we add a ceiling 
fare_ceiling = 40
# then modify the data in the Fare column to =39, if it is greater or equal to the ceiling 
data[ data[0::,10].astype(np.float) >= fare_ceiling, 10 ] = fare_ceiling - 1.0 
fare_bracket_size = 10 
number_of_price_brackets = fare_ceiling / fare_bracket_size 
# I know there were 1st, 2nd and 3rd classes on board 
number_of_classes = 3 
# But it's better practice to calculate this from the data directly 
# Take the length of an array of unique values in column index 1 
number_of_classes = len(np.unique(data[0::,1])) 
#Initialize the survival table with all zeros 
survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))


#print survival_table
'''
[
	[#female
         [class 1  
            0.  #bracket 10
            0.  #bracket 10-20
            0.  #bracket 20-30
            0.  #bracket 30-40
        ]
         [ 0.  0.  0.  0.]#bracket (10-20-30-40) class 2
         [ 0.  0.  0.  0.]#bracket (10-20-30-40) class 3
  ]

 	[#male
		[ 0.  0.  0.  0.]#bracket (10-20-30-40) class 1
         	[ 0.  0.  0.  0.]#bracket (10-20-30-40) class 2
  	      [ 0.  0.  0.  0.]#bracket (10-20-30-40) class 3
  ]
]
'''
for i in xrange(number_of_classes): #loop through each class 
    for j in xrange(number_of_price_brackets): #loop through each price bin 
        #Which element is a female, and was ith class, was greater than this bin, 
        #and less than the next bin -> give the the 3rd col (survived) 
        women_only_stats = data[ \
        (data[0::,5] == "female") \
        &(data[0::,1].astype(np.float) == i+1) \
        &(data[0:,10].astype(np.float) >= j*fare_bracket_size) \
        &(data[0:,10].astype(np.float) < (j+1)*fare_bracket_size) \
        , 2]
        #Which element is a male, and was ith class, was greater than this bin, 
        #and less than the next bin 
        men_only_stats = data[ \
        (data[0::,5] != "female")  
        &(data[0::,1].astype(np.float) == i+1) \
        &(data[0:,10].astype(np.float) >= j*fare_bracket_size) \
        &(data[0:,10].astype(np.float) < (j+1)*fare_bracket_size) \
        , 2]
        #platinum
        w = women_only_stats.astype(np.float)        
        m = men_only_stats.astype(np.float)
        if len(w)  == 0:
            wm = 0
        else:
            wm = np.mean(w)

        if len(m)  == 0:
            mm = 0
        else:
            mm = np.mean(m)
        survival_table[ survival_table != survival_table ] = 0. #platinum
        survival_table[0,i,j] = wm
        survival_table[1,i,j] = mm + 0.2
     
        
print "----survival_table  percentage %"        
print survival_table       
survival_table[ survival_table < 0.5 ] = 0 
survival_table[ survival_table >= 0.5 ] = 1        
print "----survival_table  0 not survive - 1 survive" 
print survival_table       



#open the test set and a new submission file 
test = 'titanic3_test.csv'
prediction = 'platinum_02_genderclassbased_fix_1.csv'
directory = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(directory,test)
prediction_file =  os.path.join(directory,prediction)

test_file = open(filename, 'rb') 
test_file_object = csv.reader(test_file , delimiter=';') 
header = test_file_object.next() 
predictions_file = open(prediction_file, "wb") 
p = csv.writer(predictions_file, delimiter=';') 
p.writerow(["key", "value"])


# We are going to loop through each passenger in the test set 
for row in test_file_object: 
    # For each passenger we loop throu each price bin 
    for j in xrange(number_of_price_brackets): 
        try: # Some passengers have no fare data so try to make… 
            row[9] = float(row[9]) # a float
        except: # If fails: no data, so… 
            bin_fare = 3 - float(row[1]) # bin the fare according to pclass 
            break 
        if row[9] > fare_ceiling:# If there is data see if it is greater than fare ceiling 
            bin_fare = number_of_price_brackets-1  # If so set to highest bin 
            break 
        # If passed these tests then loop through each bin 
        if row[9] >= j * fare_bracket_size \
            and row[9] < (j+1) * fare_bracket_size:
                bin_fare = j # If passed these tests then assign index 
                break 
        if row[4] == 'female': #If the passenger is female 
            p.writerow([row[0], "%d" % int(survival_table[0, float(row[1])-1, bin_fare])]) 
        else: #passenger is male 
            p.writerow([row[0], "%d" % int(survival_table[1, float(row[1])-1, bin_fare])]) 
            # Close out the files. 
test_file.close() 
predictions_file.close()        


###############################################################################
#4.5
###############################################################################
#4.6
###############################################################################
#4.7 Submission three
import csv as csv 
import numpy as np 
from scipy import stats 
from sklearn.ensemble import RandomForestClassifier


train = 'titanic3_train.csv'
directory = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(directory,train)
# Open up the CSV file into a Python object 
with open(filename, 'rb') as f: # Load the training file 
    csv_file_object = csv.reader(f, delimiter=';') 
    csv_file_object.next() # next() skips the first line holding the column headers 
    orig_train_data = [] 
    for row in csv_file_object: # Run through each row in the csv, add it to the data variable 
        orig_train_data.append(row) 
# Then convert from a list to an array 
# (Be aware that each item is currently a string in this format) 
orig_train_data = np.array(orig_train_data)
#print orig_train_data 
"""
# COLUMN CONTENT ORIG.INDEX 
# id 0 
# pclass 1 
# survived 2 
# name 3
# surname 4 
# sex 5 
# age 6 
# sibsp 7 
# parch 8 
# ticket 9 
# fare 10 
# cabin 11 
# embarked 12 
# boat 13 
# body 14 
# home.dest 15



# Prepare the data structure used for training 
#         ORIG.IDX TRAIN.IDX 
# survived     2     0 
# pclass       1     1 
# sibsp        7     2 
# parch        8     3 
# sex          5     4 
# age          6     5 
# fare         10    6 
# embarked     12    7

"""

rows = len(orig_train_data[0::, 0]) # Number of rows in the training data 
cols = 8 # Number of columns in the training data 
train_data = np.zeros((rows, cols)) # Array to store the data used for training

# SURVIVED: Store data 'survived' in train_data 
train_data[0::, 0] = orig_train_data[0::, 2].astype(np.float)
# PCLASS: Store data 'pclass' in train_data 
train_data[0::, 1] = orig_train_data[0::, 1].astype(np.float) 
# SIBSP: Store data 'sibsp' in train_data t
train_data[0::, 2] = orig_train_data[0::, 7].astype(np.float) 
# PARCH: Store data 'parch' in train_data 
train_data[0::, 3] = orig_train_data[0::, 8].astype(np.float)


# SEX: Prepare data 'sex' and store it in train_data 
# First: get the most frequent gender 
gender_data = orig_train_data[0::, 5] 
num_female = sum(gender_data == 'female') 
num_male = sum(gender_data == 'male') 
# Set the most frequent gender (female = 0, male = 1) 
most_freq_gender = 0 if num_female >= num_male else 1 
# Second: store gender data in train_data 
for i, sex in enumerate(gender_data): 
    if sex == '':
        train_data[i, 4] = most_freq_gender # Most freq. gender is used     if 'sex' is undefined 
    if sex == 'female':
        train_data[i, 4] = 0 
    if sex == 'male':
        train_data[i, 4] = 1

# AGE: Prepare data 'age' and store it in train_data 
# First: get the median age 
# Convert 'age' to float, empty values to 0 
age_data = [0 if age == '' else float(age) for age in orig_train_data[0::, 6]]
median_age = stats.nanmedian(age_data) 
# Second: store age data in train_data
# Alternative: train_data[0::, 5] = [median_age if age == 0 else age for age in age_data] 
for i, age in enumerate(age_data): 
    if age == 0: 
        train_data[i, 5] = median_age # Most freq. age is used if 'age' is undefined 
    else: 
        train_data[i, 5] = age
        

# FARE: Prepare data 'fare' and store it in train_data
# First: get the 'fare' and 'pclass' data
# Convert 'fare' to float, empty values to 0
fare_data = [0 if fare == '' else float(fare) for fare in orig_train_data[0::, 10]]
fare_data = np.array(fare_data) # Convert from a list to an array
pclass_data = train_data[0::, 1] # Get the 'pclass' values from train_data
pclass_data_unique = list(enumerate(np.unique(pclass_data))) # Get the unique 'pclass' values
# Second: replace fares with value 0 with the median fare of the corresponding 'pclass'
for i, unique_pclass in pclass_data_unique:
    # Get array of fares corresponding to the current pclass
    pclass_fare = fare_data[pclass_data == unique_pclass] 
    # Calculate the median of the previously received fares 
    median_fare = stats.nanmedian(pclass_fare) 
    pclass_fare[pclass_fare == 0] = median_fare # Replace

# Third: store fare data in train_data 
train_data[0::, 6] = fare_data[0::]  

# EMBARKED: Prepare data 'embarked' and store it in train_data 
# First: get the most common 'embarked' value 
embarked_data = list(orig_train_data[0::, 12])        

mc_embarked = max(set(embarked_data), key=embarked_data.count) 
# Second: replace empty entries with the most common 'embarked' value 
embarked_data = [mc_embarked if embarked == '' else embarked for embarked in embarked_data] 
embarked_data = np.array(embarked_data) 
# Third: convert all 'embarked' values to int 
# Get the unique 'embarked' values 
embarked_data_unique = list(enumerate(np.unique(embarked_data))) 
for i, unique_embarked in embarked_data_unique:
    embarked_data[embarked_data == unique_embarked] = i 
# Fourth: store embarked data in train_data 
train_data[0::, 7] = embarked_data[0::].astype(np.float)

# Open up the CSV file into a Python object 
test = 'titanic3_test.csv'
directory = os.path.dirname(os.path.realpath(__file__))
prediction = 'platinum_03_gender.csv'
filename = os.path.join(directory,test)
prediction_file =  os.path.join(directory,prediction)

# Open up the CSV file into a Python object 
with open(filename, 'rb') as f: # Load the test file 
    csv_file_object = csv.reader(f, delimiter=';') 
    csv_file_object.next() # next() skips the first line holding the column headers 
    orig_test_data = [] 
    for row in csv_file_object: # Run through each row in the csv, add it to the data variable 
        orig_test_data.append(row) 
# Then convert from a list to an array 
# (Be aware that each item is currently a string in this format) 
orig_test_data = np.array(orig_test_data)


rows = len(orig_test_data[0::, 0]) # Number of rows in the test data 
cols = 7 # Number of columns in the test data 
test_data = np.zeros((rows, cols)) # Array to store the data used for testing

# PCLASS: Store data 'pclass' in test_data 
test_data[0::, 0] = orig_test_data[0::, 1].astype(np.float)
# SIBSP: Store data 'sibsp' in test_data 
test_data[0::, 1] = orig_test_data[0::, 6].astype(np.float)
# PARCH: Store data 'parch' in test_data 
test_data[0::, 2] = orig_test_data[0::, 7].astype(np.float)
# SEX: Prepare data 'sex' and store it in test_data 
# First: get the most frequent gender 
gender_data = orig_test_data[0::, 4] 
num_female = sum(gender_data == 'female') 
num_male = sum(gender_data == 'male') 
# Set the most frequent gender (female = 0, male = 1) 
most_freq_gender = 0 if num_female >= num_male else 1 
# Second: store gender data in test_data 
for i, sex in enumerate(gender_data):
    if sex == '':
        test_data[i, 3] = most_freq_gender # Most freq. gender is used if 'sex' is undefined 
    if sex == 'female': 
        test_data[i, 3] = 0
    if sex == 'male':
        test_data[i, 3] = 1
        
# AGE: Prepare data 'age' and store it in test_data 
# First: get the median age 
# Convert 'age' to float, empty values to 0 
age_data = [0 if age == '' else float(age) for age in orig_test_data[0::, 5]] 
median_age = stats.nanmedian(age_data) 
# Second: store age data in test_data 
# Alternative: test_data[0::, 5] = [median_age if age == 0 else age for age in age_data] 
for i, age in enumerate(age_data):
    if age == 0:
         test_data[i, 4] = median_age 
    # Most freq. age is used if 'age' is undefined 
    else:
        test_data[i, 4] = age
        
# FARE: Prepare data 'fare' and store it in test_data 
# First: get the 'fare' and 'pclass' data 
# Convert 'fare' to float, empty values to 0 
fare_data = [0 if fare == '' else float(fare) for fare in orig_test_data[0::, 9]] 
fare_data = np.array(fare_data) 
# Convert from a list to an array 
pclass_data = test_data[0::, 0] 
# Get the 'pclass' values from test_data 
pclass_data_unique = list(enumerate(np.unique(pclass_data))) 
# Get the unique 'pclass' values
# Second: replace fares with value 0 with the median fare of the corresponding 'pclass' 
for i, unique_pclass in pclass_data_unique: 
# Get array of fares corresponding to the current pclass 
    pclass_fare = fare_data[pclass_data == unique_pclass] 
    median_fare = stats.nanmedian(pclass_fare) 
    pclass_fare[pclass_fare == 0] = median_fare 
# Replace fares with value 0 with median fare fare_data[pclass_data == unique_pclass] = pclass_fare 
# Third: store fare data in test_data 
test_data[0::, 5] = fare_data[0::]


# EMBARKED: Prepare data 'embarked' and store it in test_data 
# First: get the most common 'embarked' value 
embarked_data = list(orig_test_data[0::, 11]) 
mc_embarked = max(set(embarked_data), key=embarked_data.count) 

# Second: replace empty entries with the most common 'embarked' value 
embarked_data = [mc_embarked if embarked == '' else embarked for embarked in embarked_data] 
embarked_data = np.array(embarked_data) 

# Third: convert all 'embarked' values to int 
# Get the unique 'embarked' values 
embarked_data_unique = list(enumerate(np.unique(embarked_data))) 
for i, unique_embarked in embarked_data_unique:
    embarked_data[embarked_data == unique_embarked] = i 

# Fourth: store embarked data in test_data 
test_data[0::, 6] = embarked_data[0::].astype(np.float)

test_ids = orig_test_data[0::, 0]

forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(train_data[0::, 1::], train_data[0::, 0])
#http://scikit-learn.org/dev/modules/generated/sklearn.ensemble.RandomForestClassifier.html
output = forest.predict(test_data).astype(np.float)

# Write the data into a file 
directory = os.path.dirname(os.path.realpath(__file__))
prediction = 'platinum_03__randomforest_bb.csv'
filename =  os.path.join(directory,prediction)

boats = orig_train_data[(data[0::,12] <> "") ] 
for idx,rw in  enumerate(orig_test_data):
    print rw[12],"/",rw[13],"--"
    raw_input(">>>>")
    if rw[12] <> "":
        output[idx]=1.0
    elif rw[13] <> "":
        output[idx]=0.0

predictions_file = open(filename, 'wb') 
open_file_object = csv.writer(predictions_file, delimiter=';') 
open_file_object.writerow(['key', 'value']) 
open_file_object.writerows(zip(test_ids, output)) 
predictions_file.close()