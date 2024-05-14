#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Eliki Smith - 05/14/24
import os

file_path = os.path.dirname(__file__)
# prompt for file
log_file = input("Which file to analyze? ")
# Open File
f = open(file_path + "/" + log_file, "r")

# Read File line by line
while True:
    line = f.readline()
    if not line:
        break
    # check for 404
    if " 404 " in line:
        if "favicon.ico" in line:
            pass
    elif "%" in line:
        # Print line
        print(line)