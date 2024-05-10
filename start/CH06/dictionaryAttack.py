#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Eliki Smith - 5/10/24

import hashlib

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def find_passwords(shadow_file, password_list):
    passwords_found = []
    shadow_hashes = [line.strip().split(':')[1] for line in shadow_file]
    
    for password in password_list:
        hashed_password = hashlib.sha256(password.strip().encode()).hexdigest()
        if hashed_password in shadow_hashes:
            passwords_found.append(password.strip())
    
    return passwords_found

shadow_file_path = '/home/justincase/PythonforCybersecurity-ES/start/CH06/shadow.txt'
password_list_path = '/home/justincase/PythonforCybersecurity-ES/start/CH06/10-million-password-list-top-1000000.txt'

shadow_file = read_file(shadow_file_path)
password_list = read_file(password_list_path)

found_passwords = find_passwords(shadow_file, password_list)

with open('found_passwords.txt', 'w') as output_file:
    for password in found_passwords:
        output_file.write(password + '\n')
