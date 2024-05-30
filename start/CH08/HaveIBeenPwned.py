#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Eliki Smith - 05/29/24

import requests
import hashlib
import random
import string

def generate_password(length=12):
    """
    Generate a random password of specified length.
    
    Args:
    length (int): Length of the password to generate. Default is 12.
    
    Returns:
    str: Randomly generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_pwned(password):
    """
    Check if the password has been exposed in a data breach using the HaveIBeenPwned API.
    
    Args:
    password (str): Password to check.
    
    Returns:
    bool: True if password has been pwned, False otherwise.
    """
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = hashed_password[:5]
    suffix = hashed_password[5:]
    
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
    return 0

# Generate a new password
new_password = generate_password()

# Check if the password has been pwned
pwned_count = check_password_pwned(new_password)
if pwned_count > 0:
    print(f"Password '{new_password}' has been pwned {pwned_count} times. Please choose a different password.")
else:
    print(f"Password '{new_password}' is secure and can be used.")
