print "INDIAN TAKEAWAY!"
print "Please enter the number of your dish: "
dish_nr = input()
print "Thank you for ordering",
if dish_nr == 1:
    print "Achari Paneer"
elif dish_nr == 2:
    print "Gajar Ka Achar"
elif dish_nr == 3:
    print "Aloo Dum"
elif dish_nr == 4:
    print "Kabuli Chana"
elif dish_nr == 5:
    print "Baingan Bharta"
elif dish_nr == 6:
    print "Apple Jalebi"
else:
    print "Sorry, this dish is unknown to me!"
