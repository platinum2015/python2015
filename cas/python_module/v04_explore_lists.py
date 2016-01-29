#Create a list with 4 of your favorite restaurants
rs = ['Bloom', 'Tibits', 'Tres Amigos', 'Sonne']

#Print all restaurants using a for loop
for r in rs:
    print r 

#Append a 5th restaurant to the list
rs.append('Migros')
print rs

#Delete the 1st restaurant in the list
del(rs[0])
print rs

#Inspect the first three restaurants
print rs[:3]

#Print all restaurants in reverse order using a loop
for r in rs[::-1]:
    print r
