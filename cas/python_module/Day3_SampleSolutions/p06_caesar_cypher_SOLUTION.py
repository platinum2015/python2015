# This program creates a secret message using a simple encryption algorithm
# called a Caesar cypher, which shifts each letter ahead by 3 places.
# The program can also decode an encoded message using the opposite algorithm.

# A helper that can perform either encryption or decryption, shifting every
# letter by the given number of places, wrapping around as necessary.

def caesar_cypher(message, key):
    message = message.lower()
    secret = ""
    for character in message:
        if character in "abcdefghijklmnopqrstuvwxyz":
            num = ord(character)
            num += key
            if num > ord("z"):     # wrap if necessary
                num -= 26
            elif num < ord("a"):
                num += 26
            secret = secret + chr(num)
        else:
            # don't modify any non-letters in the message; just add them as-is
            secret = secret + character
    return secret

# Encrypts the given string using a Caesar cypher and returns the result.
def encrypt(message, key):
    return caesar_cypher(message, key)

# Decrypts a string that was previously encrypted using a Caesar cypher and returns the result.
def decrypt(message, key):
    return caesar_cypher(message, -key)


# main program
msg = raw_input("Your message to encode? ")
if len(msg) > 0:
    # wants to encrypt
    secret = encrypt(msg, 3)
    print "The encoded message is:" + secret
else:
    # empty message; wants to decrypt
    secret = raw_input("Your message to decode? ")
    if len(secret) > 0:
        msg = decrypt(secret, 3)
        print "The decoded message is:" + msg