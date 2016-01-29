def hello1():
    print "Hello, world"

def hello2(name):
    print "Hello,", name
    return

def hello3(name, count):
    for i in range(count):
        hello2(name)

def is_even(a):
    '''returns True if the given integer a is an even number, else False'''
    if a % 2 == 0:
        return True
    else:
        return False

hello2('Thilo')
hello1()
x = 1
hello3('Thilo', x if is_even(x) else x+1)

def my_func(x):
    for i in range(x):
        print "yippih"

my_func(x)
