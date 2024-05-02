#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Eliki Smith 5/2/24

# loop thought numbers 0-127
for number in range(256):
        letter = chr(number)
        #print number and chr() of number
        print(f"{number} - '{letter}' ")