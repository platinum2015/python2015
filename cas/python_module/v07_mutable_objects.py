def increase(my_list, factor):
    '''Increase each element in my_list (a list of numbers) by factor.
       Attention: Modifies the elements in the original object!'''
    for i in range(len(my_list)):
        my_list[i] = my_list[i] * factor

dozen = range(1, 13) #1..12
print(dozen)
increase(dozen, 2) #2..24
print(dozen)
        
