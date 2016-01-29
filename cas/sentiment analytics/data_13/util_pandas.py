# -*- coding: utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt 
import numpy as np
import csv
#import cx_Oracle
def d():
    #raw_input(">")
    pass

### descriptions
def pandas_version():
    print pd.__version__

def df_info(df):
    print df.info()    

### files    
def df_from_csv(csv_file,head,delim,quote_char):
    """"
    quote_char :space is NO quotechar
    head 0 = YES , None = NO header
    """
    df  = pd.read_csv(csv_file, header=head,  delimiter=delim,quotechar=quote_char,low_memory=False)
    return df
 
#print & loop 
def loop_print_df(df): #Dataframe
    print 'START print_loop_rows......'
    count = 0
    for row in df.values:
        if count == 0:
            print row
            #print 'type:',type(row),'len:',len(row)
            for i in row:
                print i
            count+=1
            d()
    print '....HEAD & TAIL'        
    print df.head(2),df.tail(2)
    
    print 'COLUMNS ARE:'
    print df.columns
    print 'END print_loop_rows......'

def loop_print_serie(ser): #Series
    print 'START Serie......'
    for row in ser:
        print row,type(row)
        try:
            print ser.mean()
        except:
            pass
        d()
    print 'END Serie......'

def loop_single_column(df,col_name):
    all_column =  df[col_name] #Its a Serie
    print type(all_column),'mean:',all_column.mean()
    for row in all_column :
        print row,type(row)
        d()

def loop_all_column_df(df):
    for col in df.columns:
        print 'starting column',col
        d()
        serie = df[col]   
        #print loop_print_serie(serie)
        print serie.head(3)
        print 'starting column',col

"""
SQL where
SELECT total_bill, tip, smoker, time  FROM tips where rownum <6;
 tips[['total_bill', 'tip', 'smoker', 'time']].head(5)

SELECT * FROM tips WHERE time = 'Dinner'
 tips[tips['time'] == 'Dinner'].head(5)

 alternantive boolean indexing:
 is_dinner = tips['time'] == 'Dinner' #return boolean index
 tips[is_dinner].head(5)
 
SELECT *FROM tips WHERE time = 'Dinner' AND tip > 5.00;
 tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)]

df.mask(df >= 0) is the oopposite


NEGATE : not , ~
 df[~df.bools]

"""
def sql_where_gt (df,col_name,val):
    all_column =  df[df[col_name] > val]
    return all_column#Dataframe

def sql_where_in (df,col_name,val_list):
    all_column =  df[df[col_name].isin(val_list)]
    return all_column#Dataframe

"""
SELECT day, AVG(tip), COUNT(*) FROM tips GROUP BY day;
 tips.groupby('day').agg({'tip': np.mean, 'day': np.size})



SELECT smoker, day, COUNT(*), AVG(tip) FROM tips GROUP BY smoker, day;
 tips.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]})

"""

def sql_sum_group_by(df,group_by_col,cols_list):
    """  select sum(cols_list[0]),...,sum(cols_list[n])
         from df 
         group by  group_by_col[0],...,group_by_col[n]
    """
    cols = []
    for column in cols_list:
        cols.append(column)

    #print df[cols].groupby(group_by_col).sum()    
    return df[cols].groupby(group_by_col).sum()

def sql_count_group_by(df,group_by_col):
    """  select count(group_by_col[0])
         from df 
         group by  group_by_col[0]
    """
    #print df[cols].groupby(group_by_col).sum()   
    print 'Value count is:',df[group_by_col].value_counts()
    print 'Size is:' ,df.groupby(group_by_col)['test.Twitter2013'].size()
    print 'count is(count the not nulls):',df.groupby(group_by_col)['test.Twitter2013'].count()
    return df[group_by_col].value_counts()

def sql_like(df,col,like_str):    
    new_df=df_head_quoted[ df[col].str.contains(like_str)]
    #for x in new_df.values:
        #print x
        #raw_input('>')
    return new_df

def sql_sort(df):
    df.sort(columns=sorting)
    return df
    
def sql_query(stmt,con):
    print 'connecting to DB:'
    #stmt = 'select * from dual'
    df = pd.read_sql_query(stmt, con, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
    #print df 
    return df 

#MISSING Data
def fill_nan_with_average(df):
    return df
#create
def create_df(xdim,ydim):
    data = np.array(range(1,(xdim*ydim)+1))
    df = pd.DataFrame(data.reshape(xdim,ydim))
    return df 

###############################################################################
###############################################################################
###############################################################################
#                                                                             #
#                             M A I N                                         #
#                                                                             #
###############################################################################
###############################################################################
###############################################################################

#Main
print 'START:'
base_dir =  os.path.dirname(os.path.realpath(__file__))


##### open file
#NO HEADER quoted string
test_file = os.path.join(base_dir,"frp_ohne_header.csv")
df  = df_from_csv(csv_file=test_file,
                  head=None,
                  delim=",",
                  quote_char='"' #space is NO quotechar
                  )
# HEADER quoted string
test_file = os.path.join(base_dir,"frpr.csv")
df_head_quoted  = df_from_csv(csv_file=test_file,
                  head=0,
                  delim=",",
                  quote_char='"' #space is NO quotechar
                  )
#loop_print_df(df_head_quoted)
#df_from_csv  print_loop_rows
test_file = os.path.join(base_dir,"allsubsetsRF_F1.txt")
df  = df_from_csv(csv_file=test_file,
                  head=0,
                  delim="\t",
                  quote_char=' ' #space is NO quotechar
                  )
gains={}
for x in df.values:
    baseline=0.55
    avg = (x[2]+x[3]+x[4]+x[5]+x[6]+x[7])/float(6)
    classifier=x[0]
    cost=x[1]
    gain_pro_cost=( avg - baseline)/float(cost)
    #print x[0],cost,avg,gain_pro_cost
    #print gain_pro_cost
    #raw_input(">")
    gains[classifier]=gain_pro_cost

keylist = gains.values()
keylist.sort()
print 

v=sorted(gains.items(), key=lambda x: x[1])
for x in v:
    
    if x[1] > 0.03:
        print x[0],x[1]
        raw_input(">")
7/0
df.drop('IDOfClassifiersUsed', axis=1, inplace=True)

grouped = df.groupby('nrOfClassifiersUsed')

g = grouped.mean()
i=1
for x in df.columns:
    print x,
print
for x in g.values:
    print i,
    for y in x:
        print "%.3f" % y,
    i=i+1   
    print 
print 


    
#describe
####
print 'desc',df.describe()
print 'info',df.info()
print 'Describe a single column:',df['test.Twitter2013'].describe()

########################COLUMN
print 'loop a single column'
loop_single_column(df,'test.Twitter2013')
loop_print_df(df)
loop_all_column_df(df)

###############################################################################
#indexes 
"""
http://pandas.pydata.org/pandas-docs/version/0.16.2/indexing.html
http://pandas.pydata.org/pandas-docs/version/0.16.2/advanced.html

loc by label
iloc by number
ix mixed

scalar acces PERFORMANCE:
at  label
iat position


"""

print 'INDEXES'
idx=df.index
print type(idx)
print 'index',idx

my_df = pd.DataFrame( [
                      [1,2,3,4,5],
                      [6,7,8,9,10],
                      [11,12,13,14,15],
                      [16,17,18,19,None]
                      ],
                      index=['a','b','c','d'],
                      columns=['C1','C2','C3','C4','C5'] 
                     )
                     
print my_df
try:
    print my_df.loc[1:3]
except:
    print 'error:print my_df.loc[1:3]'
list_of_rowid = ['b','d']    
list_of_cols  = ['C3']    
print my_df.loc[list_of_rowid]    # printed labeled indexes
print my_df.loc[list_of_rowid,list_of_cols]    # printed labeled indexes
print my_df.loc[:,list_of_cols]    # printed labeled indexes

print 'iloc'
print my_df.iloc[1:3]
print 'ix'
print my_df.ix[1:3,'C3']

print 'scalar acess'
print my_df.at['b','C2']    # scalar
print my_df.iat[2,0]    # scalar

#to generate a boolean index is_a_gt_zero =  df1.loc['a']>0

#select row between 100:105
print 'select row between 100:105 (cioe 100 101 102 103 104)'
print df['test.Twitter2013'][100:105]
print 'THOSE METHODS ARE ADVICED FOR PERFORMANCE'
print 'loc works on labels in the index 105 included'
print df['test.Twitter2013'].loc[100:105]
print 'iloc works on the positions in the index (so it only takes integers)105 EXcluded'
print df['test.Twitter2013'].iloc[100:105]
print 'ix usually tries to behave like loc but falls back to behaving like iloc if the label is not in the index.'
print df['test.Twitter2013'].ix[100:105]


#s[s.index.isin([2, 4, 6])]


"""
.loc is primarily label based,
     but may also be used with a boolean array. 
     .loc will raise KeyError when the items are not found.
       Allowed inputs are:

        A single label, e.g. 5 or 'a', (note that 5 is interpreted as a label of the index. This use is not an integer position along the index)
        A list or array of labels ['a', 'b', 'c']
        A slice object with labels 'a':'f'
                (note that contrary to usual python slices, both the start and the stop are included!)
        A boolean array

.iloc is primarily integer position based (from 0 to length-1 of the axis),
     but may also be used with a boolean array. .iloc will raise IndexError if a requested indexer is out-of-bounds, except slice indexers which allow out-of-bounds indexing. 
     
     An integer e.g. 5
     A list or array of integers [4, 3, 0]
     A slice object with ints 1:7
     A boolean array

.ix supports mixed integer and label based access. It is primarily label based,
    but will fall back to integer positional access unless the corresponding axis is 
    of integer type. .ix is the most general and 
    will support any of the inputs in .loc and .iloc. .ix also supports foating point label schemes. 
    .ix is exceptionally useful when dealing with mixed positional and label based hierachical indexes.

 However, when an axis is integer based, ONLY label based access and not positional access is supported. 
 in such cases, it’s usually better to be explicit and use .iloc or .loc.
 
"""

###############################################################################
# SQL LIKE
"""
#http://pandas.pydata.org/pandas-docs/version/0.16.2/comparison_with_sql.html

"""

print 'SQL like'
col_name='test.Twitter2013'
top = sql_where_gt (df,col_name,0.685)

col_name = 'nrOfClassifiersUsed'
top = sql_where_in (df,col_name,['2','4','2,4'])
print sql_where_in(df,col_name,[1,12]).ix[:,[1,2,3]]

#select * where
loop_print_df(top)
#select column_1 where
loop_print_serie(top[col_name])

#sort by column
# result = df.sort(['A', 'B'], ascending=[1, 0])
sorting='test.Twitter2013'
print 'SORT by',sorting
pandas_version()
sorted_asc = df.sort(columns=sorting)
sorted_desc = df.sort(columns=sorting, ascending=False)
print sorted_asc['test.Twitter2013'].head(5)
print sorted_desc['test.Twitter2013'].head(5)


#print "select ci c2 c3 where c4=1"
#idx=df[df["nrOfClassifiersUsed"]==1].index
#print df[["IDOfClassifiersUsed", "nrOfClassifiersUsed","dev","test.Twitter2014"]].loc[idx].head(3)


print 'Value counts:'
print sql_count_group_by(df,'nrOfClassifiersUsed')
sql_count_group_by(df,'nrOfClassifiersUsed').plot(kind='bar')

my_df = pd.DataFrame( [
                      [1,2,1,4,5],
                      [1,2,4,9,10],
                      [2,3,4,14,99],
                      [2,3,4,19,None]
                      ],
                      index=['a','b','c','d'],
                      columns=['C1','C2','C3','C4','C5'] 
                     )
print '*'*33

    
print 'select sum(cols_list) from df group by  group_by_col'
#print sql_sum_group_by(my_df,'C1',['C1','C2','C5'])    
print sql_sum_group_by(my_df,['C1','C2','C3'],['C1','C2','C3','C4','C5'])    

print '.......................... group by and sum max min'
print my_df
print my_df.groupby('C3').aggregate(sum)
print '..........................'
print my_df.groupby('C3').aggregate(max)
print '..........................'
print my_df.groupby('C3').aggregate(min)

print "MAX"
#idx=df[df["nrOfClassifiersUsed"]==1].index

#print type(idx)
df.columns=["ID","nr","dev","14","sqrc","13","sms","journal"]
maxs=df[["nr","dev","14","13","sms","journal"]].groupby('nr').aggregate(max)
print "MIN"
mins= df[["nr","dev","14","13","sms","journal"]].groupby('nr').aggregate(min)
print df.columns

for col in ["dev","14","sqrc","13","sms","journal"]:
    maxs=df[["nr",col]].groupby('nr').aggregate(max)
    mins= df[["nr",col]].groupby('nr').aggregate(min)
    #add a column
    maxs["min_col"]=mins
    print maxs
    #raw_input(">")

col = ["dev","14","sqrc","13","sms","journal"]
df2=df[col]
df_idnr=df[["ID","nr"]]
avgs=df2.apply(np.mean,axis=1)
df_idnr["means"] = avgs
u= df_idnr.sort(['means'], ascending=[1])
#for x in u.values:
    #print x
    #raw_input(">")

#print grouped['C5'].filter(lambda x: x.sum() > 98)

#print df2 

print 'APPLY sum_all_row,sum_all_column'
print my_df
print my_df.apply(np.sum,axis=1)#sum  x row
print my_df.apply(np.sum,axis=0)#sum  x column



def f_apply(x):    
   return x[0] + x[2]  
print my_df.apply(f_apply, axis=1)

"""
http://pandas.pydata.org/pandas-docs/version/0.16.2/groupby.html
Group By: split-apply-combine

split

apply
    aggregate
        sum 
        mean
        count size 
    transform
        standardize
        fillna
    filter
        discard,filter out 
combine

"""
print 'Group By: split-apply-combine'
####split
df = pd.DataFrame( [
                      [1,2,1,4,5],
                      [1,0,4,9,10],
                      [2,3,4,14,99],
                      [2,3,4,19,None]
                      ],
                      index=['a','b','c','d'],
                      columns=['C1','C2','C3','C4','C5'] 
                     )
key ='C1'                
print df     
#print df.groupby(key, axis=1)
print df.groupby(key).first() #only first row per group
print df.groupby(key).last() #only last row per group
print df.groupby(key).sum()
print df.groupby(key).groups #teh row in the group
#print df.groupby([key1, key2])                     
print df.groupby(['C1','C2']).sum()
#####apply
#####apply.aggregate
#####apply.aggregate.sum 
#####apply.aggregate.mean
#####apply.aggregate.count size 
key ='C1'
grouped = df.groupby(key)
print grouped.agg([np.sum, np.mean, np.std])
print 'rename col'
print grouped['C5'].agg({'somma_c5' : np.sum,'media_c5' : np.mean})
print 'rename col + Different functions'
print grouped.agg({'C3' : np.sum,'C4' : lambda x: np.std(x, ddof=1)})

#####apply.transform
#####apply.transform.standardize
#####apply.transform.fillna
#####apply.filter
#####apply.filter.discard,filter out 
print 'HAVING COUNT(*) >'
print grouped['C5'].filter(lambda x: x.sum() > 98)
#####combine
#loop_all_column_df(df_head_quoted)
df_like = sql_like(df_head_quoted,'STATUS','ER_11')
print df_like

con = cx_Oracle.connect('datamask_ref/dmask_60ref@gpvmd')
stmt = 'select dm_owner,dm_table,dm_column,dm_action,dm_records,dm_when,dm_function from datamask_ref.data_masking_input'
dfsql = sql_query(stmt,con)
loop_print_df(dfsql)

###############################################################################
#  Merge concat append
print 'NOTE with CONCAT INDEX are duplicated!!!!!!!!!!!!!!!!!!!!'

df1=pd.DataFrame( list(range(1,4)))
df2=pd.DataFrame( list(range(4,7)))
df3=pd.DataFrame( list(range(7,10)))
to_be_merged = [df1,df2,df3]
df_merge = pd.concat(to_be_merged)
print df_merge#.value_counts()
print 'ignore_index=True to have brand new indexes'
df_merge = pd.concat(to_be_merged, ignore_index=True)

print 'to remove duplicate:pd.concat([df1, df2]).drop_duplicates()'
#pd.concat([df1, df2]).drop_duplicates()
print df_merge
##########JOIN
my_df1 = pd.DataFrame( [
                      [1,'john'],
                      [2,'tim'],
                      [3,'rob'],
                      [3,'gus']
                      ],
                      columns=['id','name'] 
                     )
                     
my_df2 = pd.DataFrame( [
                      [1,'IT'],
                      [2,'FI'],
                      [4,'LO'],
                      [3,'HR']
                      ],
                      columns=['id','dept'] 
                     )
print my_df1
print my_df2
print 

##LEFT
print pd.merge(my_df1,my_df2,on ='id',how='left')
##RIGHT
print pd.merge(my_df1,my_df2,on ='id',how='right')
##FULL
print pd.merge(my_df1,my_df2,on ='id',how='outer')
             
###############################################################################
#Missing values                     
missing_df = pd.DataFrame( [[1,2,3,4,5],[None,7,8,9,10],[11,12,13,14,15]])
print pd.isnull(missing_df) 
print 'fill na',missing_df.fillna(value=99)
print 'drop na',missing_df.dropna(how='any')
# drop single column df.dropna(axis=0)
print missing_df



###############################################################################
#dump to file
test_file = os.path.join(base_dir,'foo.xlsx')
my_df.to_excel(test_file, sheet_name='Sheet1')
test_file = os.path.join(base_dir,'foo.csv')
my_df.to_csv(test_file)
test_file = os.path.join(base_dir,'foo.h5')
dataframe = 'df'
my_df.to_hdf(test_file,dataframe)

###############################################################################
#TO CLIPBOARD
#http://pandas.pydata.org/pandas-docs/version/0.16.2/generated/pandas.DataFrame.to_clipboard.html#pandas.DataFrame.to_clipboard
my_df.to_clipboard(excel=None, sep=None)

###############################################################################
#WORKING WITH STRING
print 'WORKING WITH STRING'
df_str = pd.DataFrame( [
                      ['ciccio','IT'],
                      ['pasciccio','FI'],
                      ['pippo','LO'],
                      ['OKIDIKI','HR']
                      ],
                      columns=['id ','dept id'] 
                     )
column = 'id '                     
print df_str[column].str.lower()
print df_str[column].str.upper()
print df_str[column].str.strip()
df_str.columns = df_str.columns.str.strip().str.lower().str.replace(' ', '_')
print df_str
#replace
print df_str.replace(['ciccio','LO'], ['NEW_kikkio','NEW_'])
print df_str
print df_str.replace(['ciccio','LO'], ['NEW_kikkio','NEW_'],inplace=True)
print df_str 

#http://pandas.pydata.org/pandas-docs/version/0.16.2/text.html#method-summary



