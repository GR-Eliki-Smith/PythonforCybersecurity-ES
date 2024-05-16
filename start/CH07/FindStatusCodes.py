#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By Eliki Smith - 05/14/24
import os
import re

#setup pattern to match
re_pattern = r'\s\d\d\d\s'

file_path = os.path.dirname (__file__)
#prompt for filename
log_file = input ("Which file to analyze? ")
#Open File
f = open (file_path + "/" +log_file, "r")

results_dict = {}

#Read file line by line
while True:
    line = f.readline()
    if not line:
        break
    m = re.search(re_pattern, line)
    if m: 
        #print(m.group())
        item = m.group()
        #is item in dictionary?
        if item in results_dict.keys():
            #if YES, add 1 to count
            results_dict[item] = results_dict[item] + 1
        else:
            #else, add to dictionary
            results_dict[item] = 1

        for w in sorted(results_dict, key = results_dict.get, reverse = True):
            print (w, results_dict[w])