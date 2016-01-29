#idea by http://www.python-kurs.eu/schleifen.php
import random

print "Guess my number (between 1 and 100; 0 to give up):"
to_be_guessed = int(100 * random.random()) + 1
guess = 0

while guess != to_be_guessed:
    guess = input("Your guess: ")
    if guess > 0:
        if guess > to_be_guessed:
            print "  too big"
        elif guess < to_be_guessed:
            print "  too small"
    else:
        print "Too bad you're giving up!"
        break
else:
    print "Congratulations,", guess, "is correct!"
