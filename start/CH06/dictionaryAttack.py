#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Eliki Smith - 5/10/24
import crypt
import os

file_path = os.path.dirname(__file__)

#ask for ID and salt
id_salt = input ("what is the id and salt? ")
#ask for fully salted hash
salted_pass = input ("What is the fully salted hash? ")

#open password file
f = open(file_path + "/10-million-password-list-top-1000000.txt", "r")
# for each guess in pass file
for guess in f:
    guess = guess.strip()

    #Hash the guesses
    hashed_guess = crypt.crypt( guess, id_salt )
    #is guess = to target?
    if hashed_guess == salted_pass:
        #print guess and quit
        print(guess)
        exit()