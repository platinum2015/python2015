def derivative(my_function):
    '''Returns a function that computes the numerical derivative of the given
       function my_function'''
    def df(x, h=0.0001):
        return ((my_function(x+h) - my_function(x-h)) / (2*h))
    return df

def f(x):
    '''The mathematical function f(x) = x^3'''
    return x*x*x

df = derivative(f)   #f'
ddf = derivative(df) #f''
for x in range(-10, 10):
    print x, f(x), df(x), ddf(x)
