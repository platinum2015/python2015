from datetime import date

today = date.today()

# Ask the user for his/her birthday
bday_day = int(raw_input("What day is your birthday [1-31]? "))
bday_month = int(raw_input("What month is your birthday [1-12]? "))

your_birthday = date(today.year, bday_month, bday_day)

# Check if it is next year
if your_birthday < today:
    your_birthday = your_birthday.replace(year=today.year + 1)

#Calculate the number of days until the bday
time_to_birthday = abs(your_birthday - today)

# Print number of days, be nice if bday is today
print "Today is ", today
if time_to_birthday.days == 0:
    print "Happy Birthday!"
else:
    print "Another",time_to_birthday.days,"days till your birthday"
