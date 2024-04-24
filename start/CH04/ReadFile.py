#!/usr/bin/env python3
# Sample script that reads from a file
# By Eliki Smith 4/24/24

file = open('hackme.txt','r')
print("Here is someone to hack - information")
for line in file:
    print(line)

file.close()