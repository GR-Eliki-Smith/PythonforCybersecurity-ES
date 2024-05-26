#!/usr/bin/env python3
#Dad jokes api script
#By Eric Smith - 05/26/24

import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)
joke = response.json()["joke"]

print(joke)