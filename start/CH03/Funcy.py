#!/usr/bin/env python3
# example working with Functions
#By Eliki Smith - 4/24/24

def send_message():
    for i in range(5):
        print("Yeah it is")

user_input = input("Is the sky blue? (yes/no) ")

if user_input.lower() == "yes":
    send_message()
else:
    print("Okay, maybe another time.")