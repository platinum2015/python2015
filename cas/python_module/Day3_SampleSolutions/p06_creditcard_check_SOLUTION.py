# You have been hired by MeisterCard to write a function
# which checks if a given credit card number is valid.
# Your function check(card_number) should take a string card_number as input.
# First, if the string does not follow the format "#### #### #### ####"
# where each # is a digit, then it should return False.
# Then, if the sum of the digits is divisible by 10 (a "checksum" method),
# then the procedure should return True, else it should return False.
# For example, if card_number is the string "9384 3495 3297 0123" then although the
# format is correct, the digit sum is 72 so you should return False.
        
def number_format(s):
    number_parts = s.split(' ')
    if len(number_parts) != 4:
        return False
    for part in number_parts:
        if len(part) != 4:
            return False
        elif not part.isdigit():
            return False
    print "Correct format."
    return True

def check(s):
    if number_format(s):
        digit_sum = 0
        for digit in s:
            if digit != ' ':
                digit_sum += int(digit)
        if digit_sum % 10 == 0:
            print "Correct checksum."
            return True
    return False

card_number = "9384 3495 3297 0121"
print check(card_number)
card_number = "9384 3495 3297 0123"
print check(card_number)
