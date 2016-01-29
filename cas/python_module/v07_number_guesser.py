def guess(number, lower_bound, upper_bound):
    '''Use binary search to find the number to be guessed
       within the range given by lower_bound and upper_bound
       in a minimal number of tries without any random element'''
    if lower_bound == upper_bound:
        return lower_bound
    else:
        middle = (lower_bound+upper_bound) / 2
        print lower_bound, "...", upper_bound, "\tn >", middle, "?"
        if number > middle:
            return guess(number, middle+1, upper_bound)
        else:
            return guess(number, lower_bound, middle)
        
lbound = 1
ubound = 10
n = 2
res = guess(n, lbound, ubound)
print "Result", res
