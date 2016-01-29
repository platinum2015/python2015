def outer(x):
    def inner():
        return x+1
    return inner()

y = 1
print outer(y)
print inner()
