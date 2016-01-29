# Read in Restaurants until empty line
restaurants = []
while True:
    restaurant = raw_input("Another favorite Restaurant: ")
    if restaurant == "":
        break
    else:
        restaurants.append(restaurant)

# Choose one randomly
import random
selected = random.choice(restaurants)

# Print all restaurants and mark selected
print
for item in restaurants:
    if item ==selected:
        print "->",item
    else:
        print "  ",item
