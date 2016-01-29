# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:04:53 2015

@author: MG
"""

import csv as csv
import numpy as np
import os 

with open("/Volumes/KINGSTON/workspace/python2015/cas/titanic3_train.csv", 'rb') as f:
    csv_file_object = csv.reader(f, delimiter=';')
    header = csv_file_object.next() # next() skips the first line holding the column headers
    data_raw=[] # strings
    for row in csv_file_object:
        data_raw.append(row)


# DEVIATION FROM SCRIPT no. 1

# thinking about the data:
# if a passenger was registered on a lifeboat (i.e. if there is a value
# in the 'boat' variable), the person obviously did not drown;
# while the person may have died on the lifeboat or on the rescue ship
# (e.g. from cold), the probability that the person survived is high;
# expecting a correlation with 'survived' of close to 1
# (assumption to be checked later in the script)

#   *** predictive variable no. 1 for submission: 'boat' ***

# the same rationale applies to the variable 'body'; if there is an entry
# in the 'body' variable, the passenger obviously died (drowned, died from
# cold, etc.);
# expecting a correlation with 'survived' of -1
# (assumption to be checked later in the script)

#   *** predictive variable no. 2 for submission: 'body' ***

# BACK TO THE SCRIPT ...


# some data viewing and manipulation

print "-"*30
print "# some data viewing and manipulation"
# optional: print raw data to get a feel for the format
# print "raw data", data_raw
data = np.array(data_raw)
print "data", data
# also check variables in Python Variable explorer: type: string432, size: 1048 x 16
print "first row", data[0]
print "some data point", data[0, 3]
print "variable 'gender'", data[0::,5]

# float from string

print "pclass str", data[0::,1]
pclass = data[0::,1].astype(np.float)
print "pclass float", pclass
print "-"*30

# survivors, passengers (no filter, all passengers)

print
print "# survivors, passengers (no filter, all passengers)"
number_survived = np.sum(data[0::,2].astype(np.float))
number_passengers = np.size(data[0::,2].astype(np.float))
proportion_survivors = number_survived / number_passengers
print "proportion of survivors to passengers", proportion_survivors

# by gender

print
print "# by gender"
women_only_stats = data[0::,5] == "female" # True/False-array, i.e. a filter
# print "women_only_stats", women_only_stats # optional to check format
men_only_stats = data[0::,5] != "female"
women_onboard = data[women_only_stats,2].astype(np.float) # binary
# print "women_onboard", women_onboard # optional to check format
men_onboard = data[men_only_stats,2].astype(np.float)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
print "passengers on board", np.size(women_onboard) + np.size(men_onboard)
print "women on board", np.size(women_onboard)
print "women survived", int(np.sum(women_onboard))
print "survival ratio women to women on board %s" % proportion_women_survived
print "men on board", np.size(men_onboard)
print "men survived", int(np.sum(men_onboard))
print "survival ratio men to men on board %s" % proportion_men_survived
print


# DEVIATION FROM SCRIPT no. 2

# apply above methodology to compute absolute values and ratios
# to other variables, e.g.:

# class: 1st class passengers

pcl_1_tf = data[0::,1] == "1" # True/False-array, i.e. filter
# print "pcl_1", pcl_1_tf # optional to check format
pcl_1_bin = data[pcl_1_tf,2].astype(np.float)
pcl_1_survived = np.sum(pcl_1_bin)
pcl_1_onboard = np.size(pcl_1_bin)
print "1st class passengers on board", pcl_1_onboard
print "1st class passengers survived", int(pcl_1_survived)
# pcl_1_to_all = 
pcl_1_sr_to_all_surv = round(pcl_1_survived / (np.sum(women_onboard) + np.sum(men_onboard)), 2)
pcl_1_sr_to_pcl_1 = round(pcl_1_survived / pcl_1_onboard, 2)
print "proportion 1st class passengers to all passengers", 
print "survival ratio 1st class survivors to all survivors", pcl_1_sr_to_all_surv
print "survival ratio 1st class within", pcl_1_sr_to_pcl_1 
print "\n--> above average survival probability,\
good to be a 1st class passenger"
print "could be submitted as another interim result"

# Further Ideas on absolute values and ratios:

# also explore absolute values and ratios for variables:
# relatives (siblings, parents), fares

# BACK TO THE SCRIPT ...


print
print "-"*30

# empty fare values <- mean fare of corresponding class

# mean fare per pclass
print
fare_mean_per_pclass = []
for i in range(len(np.unique(data[0::,1]))):
    fare_mean_per_pclass.append(0)
    cnt = 0 # number of tickets with a value in pclass i
    for j in range(len(data[0::,10])):
        if data[j, 1].astype(np.int) == i+1:
            try: #try to cast the jth fare value as float
                fare_mean_per_pclass[i] += data[j, 10].astype(np.float)
                cnt += 1
            except: #if it can't be casted to float: ignore it
                fare_mean_per_pclass[i] += 0 #just ignore empty values
    if cnt > 0: fare_mean_per_pclass[i] /= float(cnt) #calculate mean
# print "Mean fare per pclass: ", fare_mean_per_pclass

# validating below loop:
# (for-loop formula as suggested by task description was incorrect)

print "# check missing data replacement loop"
print len(data[0::,10])
print "fare at row 980: '", data[980, 10], "' i.e. missing" # missing value before replacing with mean_fare
print "class:", data[980, 1] # third class
print "mean fare:", fare_mean_per_pclass[2] # third class corresponding to index 2

for i in range(len(data[0::,10])): # replace the empty values with the pclass mean
    try:
        test = float(data[i, 10]) # if this works, all is well with row i
    except ValueError:
        data[i, 10] = fare_mean_per_pclass[data[i, 1].astype(np.int) - 1] # index: current pclass-1

# validating above loop:
print "missing fare value at row 980 replaced by mean_fare:", data[980, 10]


# DEVIATION FROM SCRIPT no. 2

# age: p14 P08_Data_Science.pdf suggests to replace missing values with the \
# median age
# age is at py column 6

print
print type(data[0::,6]) # type: numpy.ndarray

# replace blanks by 0's
for i in range(len(data[0::,6])):
    try:
        test = float(data[i, 6])
    except ValueError:
        data[i, 6] = 0

# replace 0's median
age_list_str = np.array(data[0::,6]).tolist()
print type(age_list_str) # type: list
age_list_fl = [float(i) for i in age_list_str]
# print "age_list_fl", age_list_fl
# age_list_fl = map(float, age_list_str)
age_median = np.median(age_list_fl)
# print "age median:", age_median

age_list_fl_m = []
for i in range(len(data[0::,6])):
    if age_list_fl[i] == 0:
        age_list_fl[i] = age_median
        age_list_fl_m.append(age_list_fl[i])
    else:
        age_list_fl_m.append(age_list_fl[i])

# print "age_list_fl_m", age_list_fl_m

# !! problem: overwriting the "age" values does not work, so below 'corrected'
# list is not corrected but still populated with 0's

# print "age, corrected list:", age_list_cor
# print "age, corrected numpy.ndarray:", data[0::,6]

# repeat for missing values of any other variables
# ...

fare_list = data[0::,10].astype(np.float)
# print fare_list

titles = ["Fares", "Age"]
data_list = [fare_list, age_list_fl_m]

"""
# idea: dictionary

keys = titles = ["Fares", "Age"]
values = data_list = [fare_list, age_list_fl_m]
dict_from_two_lists = dict(zip(keys, values))
print "dict_from_two_lists: ", dict_from_two_lists

"""
print
print "-"*30
print

print "# descriptive stats  /  idea: get a feel for the variables"
for title in titles:
    print titles.index(title)+1,".\t", title
print "tmean:\tstd.dev:\tmedian:\tmin:\tmax:"
for i in data_list:
    print round(np.mean(i),2),"\t", round(np.std(i),2),"\t",\
    round(np.median(i),2),"\t", round(np.min(i),2),"\t", round(np.max(i),2)

# idea: do descriptive stats for more variables

# BACK TO THE SCRIPT ...


# by gender, class, price

print
print "-"*30
print
print "survival table"

fare_ceiling = 40 # ceiling for fare
# modify the data in the Fare column to =39, if it is greater or equal to the ceiling
data[data[0::,10].astype(np.float) >= fare_ceiling, 10] = fare_ceiling - 1.0
fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size
# print "number_of_price_brackets ", number_of_price_brackets 
number_of_classes = len(np.unique(data[0::,1])) # no. of pclasses, i.e. [1, 2, 3]
# print "number_of_classes ", number_of_classes 

# Initialize the survival table with all zeros
survival_table = np.zeros((2, number_of_classes, number_of_price_brackets)) # gender, classes, fare brackets
# print "plain survival table\n", survival_table # optional to check format

for i in xrange(number_of_classes):
    for j in xrange(number_of_price_brackets):
        women_only_stats_t = data[ \
            (data[0::,5] == "female") \
            &(data[0::,1].astype(np.float) == i+1) \
            &(data[0::,10].astype(np.float) >= j*fare_bracket_size) \
            &(data[0::,10].astype(np.float) < (j+1)*fare_bracket_size) \
            , 2]
        men_only_stats_t = data[ \
            (data[0::,5] != "female") \
            &(data[0::,1].astype(np.float) == i+1) \
            &(data[0::,10].astype(np.float) >= j*fare_bracket_size) \
            &(data[0::,10].astype(np.float) < (j+1)*fare_bracket_size) \
            , 2]
        survival_table[0,i,j] = np.mean(women_only_stats_t.astype(np.float))
        survival_table[1,i,j] = np.mean(men_only_stats_t.astype(np.float))
        survival_table[ survival_table != survival_table ] = 0

"""
# build for loop for labels

labels_table = np.zeros((2, number_of_classes, number_of_price_brackets))
st_pclass = [1, 2, 3]
st_price_brackets = ["<10", "<20", "<30", "<40"]
st_gender = ["f", "m"]
for i in xrange(st_pclass):
    for j in xrange(st_price_brackets):
        st_gender[0,i,j]
        st_gender[1,i,j]
        labels_table[0,i,j] = st_gender
        labels_table[1,i,j] = st_gender
"""

print
print "    f 1 <10\t    f 1 <20\t    f 1 <30\t    f 1 <40"
print "    f 2 <10\t    f 2 <20\t    f 2 <30\t    f 2 <40"
print "    f 3 <10\t    f 3 <20\t    f 3 <30\t    f 3 <40"
print
print "    m 1 <10\t    m 1 <20\t    m 1 <30\t    m 1 <40"
print "    m 2 <10\t    m 2 <20\t    m 2 <30\t    m 2 <40"
print "    m 3 <10\t    m 3 <20\t    m 3 <30\t    m 3 <40"
print

print survival_table

survival_table[ survival_table < 0.5 ] = 0
survival_table[ survival_table >= 0.5 ] = 1

print
print survival_table
print

# print prediction of survival table to file


"""
#open the test set and a new submission file
test_file = open('titanic3_test.csv', 'rb')
test_file_object = csv.reader(test_file , delimiter=';')
header = test_file_object.next()
predictions_file = open("grm_titanic_submission2_gender_class_ticket_based.csv", "wb")
p = csv.writer(predictions_file, delimiter=';')
p.writerow(["key", "value"])

# in the test file, not all passengers are binned, so:
# We are going to loop through each passenger in the test set
for row in test_file_object:
# For each passenger we loop throu each price bin
    for j in xrange(number_of_price_brackets):
        try: # Some passengers have no fare data so try to make...
            row[9] = float(row[9]) # a float
        except: # If fails: no data, so...
            bin_fare = 3 - float(row[1]) # bin the fare according to pclass 
            break
        if row[9] > fare_ceiling: # If there is data see if it is greater than fare ceiling
            bin_fare = number_of_price_brackets-1 # If so set to highest bin
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
"""

# modified version: by gender, class, fare ... AND:
# overwrite prediction if boat == 1 or body == 1

print
print "-"*30
print

print "submission/output no. 3:"
print "# modified version: by gender, class, fare ... AND:"
print "# overwrite prediction if boat == 1 or body == 1"

#open the test set and a new submission file
test_file = open("/Volumes/KINGSTON/workspace/python2015/cas/titanic3_train.csv", 'rb')


test_file_object = csv.reader(test_file , delimiter=';')
header = test_file_object.next()
predictions_file = open("grm_titanic_submission3_gender_class_ticket_plus_based.csv", "wb")
p = csv.writer(predictions_file, delimiter=';')
p.writerow(["key", "value"])

# in the test file, not all passengers are binned, so:
# We are going to loop through each passenger in the test set
for row in test_file_object:
# For each passenger we loop throu each price bin
    for j in xrange(number_of_price_brackets):
        try: # Some passengers have no fare data so try to make...
            row[9] = float(row[9]) # a float
        except: # If fails: no data, so...
            bin_fare = 3 - float(row[1]) # bin the fare according to pclass 
            break
        if row[9] > fare_ceiling: # If there is data see if it is greater than fare ceiling
            bin_fare = number_of_price_brackets-1 # If so set to highest bin
            break
        # If passed these tests then loop through each bin
        if row[9] >= j * fare_bracket_size \
            and row[9] < (j+1) * fare_bracket_size:
                bin_fare = j # If passed these tests then assign index
                break
    pred =""    
    if row[12] <> "":
        pred = 1
        # raw_input(row[12])
    elif row[13] <> "":
        pred = 0   
        # raw_input(row[13])        
    elif row[4] == 'female': #If the passenger is female 
        # print("f",row[12],row[13])        
        # raw_input("f")         
        pred=int(survival_table[0, float(row[1])-1, bin_fare]) 
    else: #passenger is male 
        pred=int(survival_table[1, float(row[1])-1, bin_fare])        
        # raw_input("m")
    p.writerow([row[0], "%d" % pred]) 
        # Close out the files.

test_file.close()
predictions_file.close()


# some ideas on multivariate linear regression

"""
def get_linear_regression(xi,y):
    A = np.array([ xi, np.ones(len(xi))])
    a, b = np.linalg.lstsq(A.T,y)[0] # obtaining the parameters
    return a, b # return as a tuple
"""

"""
import numpy as np
import statsmodels.api as sm

y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

x = [
     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
     ]

def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

print reg_m(y, x).summary()
"""

"""
# Scatter plot with regression line
ax = fig.add_subplot(1,3,3)
line = w[0]*shots + w[1]
plt.plot(shots,goals,'o',shots,line)
plt.title('Shots vs goals')
plt.xlabel('number of shots')
plt.ylabel('number of goals')
plt.grid(True)
"""


"""

# Submission Tree

import csv as csv
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestClassifier

# Open up the CSV file into a Python object
with open('../data/titanic3_train.csv', 'rb') as f: # Load the training file
    csv_file_object = csv.reader(f, delimiter=';')
    csv_file_object.next() # next() skips the first line holding the column headers
    orig_train_data = []
    for row in csv_file_object: # Run through each row in the csv, add it to the data variable
        orig_train_data.append(row)
# Then convert from a list to an array
# (Be aware that each item is currently a string in this format) orig_train_data = np.array(orig_train_data)

rows = len(orig_train_data[0::, 0]) # Number of rows in the training data 
cols = 8 # Number of columns in the training data
train_data = np.zeros((rows, cols)) # Array to store the data used for training

# SURVIVED: Store data 'survived' in train_data
train_data[0::, 0] = orig_train_data[0::, 2].astype(np.float)

# PCLASS: Store data 'pclass' in train_data
train_data[0::, 1] = orig_train_data[0::, 1].astype(np.float)
# SIBSP: Store data 'sibsp' in train_data
train_data[0::, 2] = orig_train_data[0::, 7].astype(np.float)
# PARCH: Store data 'parch' in train_data
train_data[0::, 3] = orig_train_data[0::, 8].astype(np.float)

# SEX: Prepare data 'sex' and store it in train_data # First: get the most frequent gender
gender_data = orig_train_data[0::, 5]
num_female = sum(gender_data == 'female')
num_male = sum(gender_data == 'male')
# Set the most frequent gender (female = 0, male = 1)
most_freq_gender = 0 if num_female >= num_male else 1 # Second: store gender data in train_data
for i, sex in enumerate(gender_data):
    if sex == '':
        train_data[i, 4] = most_freq_gender # Most freq. gender is used if 'sex' is undefined
    if sex == 'female':
        train_data[i, 4] = 0
    if sex == 'male':
        train_data[i, 4] = 1

# AGE: Prepare data 'age' and store it in train_data
# First: get the median age
# Convert 'age' to float, empty values to 0
age_data = [0 if age == '' else float(age) for age in orig_train_data[0::, 6]]
median_age = stats.nanmedian(age_data) # Second: store age data in train_data
# Alternative: train_data[0::, 5] = [median_age if age == 0 else age for age in age_data]
for i, age in enumerate(age_data):
    if age == 0:
        train_data[i, 5] = median_age # Most freq. age is used if 'age' is undefined
    else:￼
        train_data[i, 5] = age
# FARE: Prepare data 'fare' and store it in train_data # First: get the 'fare' and 'pclass' data
# Convert 'fare' to float, empty values to 0
fare_data = [0 if fare == '' else float(fare) for fare in orig_train_data[0::, 10]]
fare_data = np.array(fare_data) # Convert from a list to an array
pclass_data = train_data[0::, 1] # Get the 'pclass' values from train_data pclass_data_unique = list(enumerate(np.unique(pclass_data))) # Get the unique 'pclass' values
# Second: replace fares with value 0 with the median fare of the corresponding 'pclass'
for i, unique_pclass in pclass_data_unique:
    # Get array of fares corresponding to the current pclass 
    pclass_fare = fare_data[pclass_data == unique_pclass]
    # Calculate the median of the previously received fares 
    median_fare = stats.nanmedian(pclass_fare)
    pclass_fare[pclass_fare == 0] = median_fare # Replace fares with value 0 with median fare
    fare_data[pclass_data == unique_pclass] = pclass_fare # Third: store fare data in train_data
    train_data[0::, 6] = fare_data[0::]
# EMBARKED: Prepare data 'embarked' and store it in train_data 
# First: get the most common 'embarked' value
embarked_data = list(orig_train_data[0::, 12])

mc_embarked = max(set(embarked_data), key=embarked_data.count)
# Second: replace empty entries with the most common 'embarked' value
embarked_data = [mc_embarked if embarked == '' else embarked for embarked in embarked_data] embarked_data = np.array(embarked_data)
# Third: convert all 'embarked' values to int # Get the unique 'embarked' values
embarked_data_unique = list(enumerate(np.unique(embarked_data)))
for i, unique_embarked in embarked_data_unique:
    embarked_data[embarked_data == unique_embarked] = i
# Fourth: store embarked data in train_data 
train_data[0::, 7] = embarked_data[0::].astype(np.float)

# Open up the CSV file into a Python object
with open('../data/titanic3_test.csv', 'rb') as f: # Load the test file
    csv_file_object = csv.reader(f, delimiter=';')
    csv_file_object.next() # next() skips the first line holding the column headers
    orig_test_data = []
    for row in csv_file_object: # Run through each row in the csv, add it to the data variable
        orig_test_data.append(row)
# Then convert from a list to an array
# (Be aware that each item is currently a string in this format)
orig_test_data = np.array(orig_test_data)


# etc.

"""