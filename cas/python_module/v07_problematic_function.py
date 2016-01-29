def problematic_function(my_list = []):
    my_list.append(1)
    return my_list

print problematic_function()
print problematic_function()
print problematic_function([])

