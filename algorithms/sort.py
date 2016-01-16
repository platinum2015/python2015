    # -*- coding: utf-8 -*-
import random

def insertion_sort(array):
    """ Insertion  sort an In place algorithm"""
    length = len(array)
    j = 1
    while j < length:
        current = array[j]
        i = j - 1
        previous = array[i] 
        print previous,":",current    
        while i >= 0 and array[i] > current:#Find rigt position for current
            array[i + 1] = array[i]
            array[i] = current
            i = i - 1
            #print array
        array[i + 1] = current
        j = j + 1 
    print "sorted array:",array 


array=[6,7,4,6,1,3,7]
#array  = random.sample(xrange(10000), 1000)
insertion_sort(array)
print "*"*30

def merge(array,left,right,end):
    print array   , end 
    sorted_array=[]
    i = 0
    left_end = right-1
    l_not_end = True
    r_not_end = True
    while i <= end:
        print "i:",i," left:",left," lend:",left_end," right:", right , " end:",end
        i = i + 1
        if left < left_end and right < end:#normal case
            if  array[left] < array[right]:
                sorted_array.append(array[left])
                left = left + 1
                print "L std",sorted_array
            else:
                sorted_array.append(array[right])
                right = right + 1
                print "R std",sorted_array
        elif right == end and r_not_end:#right end reach, add left
            sorted_array.append(array[right])
            print "R =",sorted_array
            r_not_end = False
        elif left ==  left_end  and l_not_end: #left end reach, add right
            sorted_array.append(array[left])
            l_not_end = False            
            print "L =",left,sorted_array
        elif right < end:#right end reach, add left
            sorted_array.append(array[right])
            right = right + 1
            print "R full",sorted_array
        elif left <  left_end:#left end reach, add right
            sorted_array.append(array[left])
            left = left + 1        
            print "L full",sorted_array
    #print sorted_array
    return sorted_array        


def merge_sort(array,start,end):
    array_sorted = []    
    middle = (start + end)/2
    print "array:",array," start:",start,"middle:",middle,"end:",end
    raw_input(">")
    if start < end:        
        left = merge_sort(array[start:middle+1],0,middle-start)
        print left
        raw_input("left>")
        right = merge_sort(array[middle+1:end+1],0,end - (middle+1))
        print right
        raw_input("right>")
        to_combine = left + right  
        print to_combine
        raw_input("comb>")
        #HERE SEND "2 + 1 instead of 1 + 2 format
        array_sorted = merge(to_combine,
                             0,
                             len(to_combine)/2,
                             len(to_combine)-1
                             )
    else:        
        array_sorted = array
        print array
        raw_input("(was base)>")
    return array_sorted
        
array=[40,50,60,1,2,3,8]#must be half sorted...
array=[1,2,3,4,5,6,7,8,9,10,11,12]#must be half sorted...
array=[40,50,60,1,2,3,8]#must be half sorted...
print "....",len(array) / 2
x=merge(array,
         0,
         len(array) / 2, #q 
         len(array) -1 #r
         )
print x 
      
print "*"*30
array=[100,3,2]#must be half sorted...
s=merge_sort(array,0,len(array)-1)
print "-"*30
print s