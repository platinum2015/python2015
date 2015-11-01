# List of restaurants
my_restaurants = ['Mensa', 'Royal Mangal City', 'Migros', 'Tibits']

# Your like Bloom and not Tibits
your_restaurants = my_restaurants # or copy.deepcopy(my_restaurants)
your_restaurants[-1] = 'Bloom'

# Print our restaurants

print "These are MY favorite restaurants"
for rest in my_restaurants:
    print rest

print "These are YOUR favorite restaurants"
for rest in your_restaurants:
    print  rest
            
print(id(my_restaurants),type(my_restaurants))
print(id(your_restaurants),type(your_restaurants))