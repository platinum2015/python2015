# List of restaurants
restaurants = ['Mensa', 'Royal Mangal City', 'Migros', 'Tibits']

# Computer, choose one
import random
which_one = int(random.uniform(0,len(restaurants)))

# Let me know where I eat today
print "Why don't you go to ",restaurants[which_one]," today?"
