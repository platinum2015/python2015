def increase(my_list, factor = 2, method = "mult"):
    '''Increase each element in my_list (a list of numbers):
       If method == "add", the factor is added to each element.
       If method == "exp", each element is raised to the power of factor.
       If method has any other value, each element is multiplied by the factor.
       Attention: Modifies the elements in the original object!'''
    for i in range(len(my_list)):
        if method == "add":
            my_list[i] = my_list[i] + factor
        elif method == "exp":
            my_list[i] = my_list[i] ** factor
        else:
            my_list[i] = my_list[i] * factor

dozen = range(1, 13) #1..12
print(dozen)
increase(dozen) #2..24 (*2)
print(dozen)
increase(dozen, method="add") #4..26 (+2)
print(dozen)
increase(dozen, 3, "exp") #64..17576 (**3)
print(dozen)

