def function(a_string):
    print id(a_string)
    return a_string + '.'

s1 = 'Hello'
print id(s1)
s2 = function(s1)
print id(s2)
