print "Please think of a number from 1 to 10. Ready?"
res = raw_input();

greater = "Is the number greater than"
equal = "Is the number equal to"

print greater, 5, "?"
res = raw_input();
if res == "yes": #6<=n<=10
    print greater, 7, "?"
    res = raw_input()
    if res == "yes": #8<=n<=10
        print greater, 9, "?"
        res = raw_input()
        if res == "yes": #n=10
            n = 10
        else: #8<=n<=9
            print equal, 8, "?"
            res = raw_input()
            n = 8 if res=="yes" else 9
    else: #6<=n<=7
        print equal, 6, "?"
        res = raw_input()
        n = 6 if res=="yes" else 7
else: #1<=n<=5
    print greater, 2, "?"
    res = raw_input();
    if res == "yes": #3<=n<=5
        print greater, 4, "?"
        res = raw_input()
        if res == "yes": #n=5
            n = 5
        else: #3<=n<=4
            print equal, 3, "?"
            res = raw_input()
            n = 3 if res=="yes" else 4
    else: #1<=n<=2
        print equal, 1, "?"
        res = raw_input()
        n = 1 if res=="yes" else 2
        
print "You choose number", n, "!"
