#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Eliki Smith 4/30/24

#Ask for Message
message = input("What is the message? ")
message = message.lower()
#Foreach Letter
for letter in message:
    print(letter)
    #change to number
    letter_number = ord (letter)
    #is this a letter?
    if letter_number >= 97 and letter_number <= 122:
        #Add 13
        letter_number = letter_number + 13
        #GTR than 26?
        if letter_number > 122:
            #Sub 26
            letter_number -= 26
    #Change to letter
    print(letter_number)
# Print message
#print(new_message)