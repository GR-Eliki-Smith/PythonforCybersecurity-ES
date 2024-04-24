#!/usr/bin/env python3
# Sample script that writes to a file
# By Eliki Smith 4/24/24

name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What is your first pet's name? ")
maiden_name = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

with open('hackme.txt','w') as f:
    f.write(f"Name: {name}\n")
    f.write(f"Favorite Color: {color}\n")
    f.write(f"First Pet's Name:{pet}\n")
    f.write(f"Mother's Maiden Name:{maiden_name}\n")
    f.write(f"Elementary School:{school}\n")