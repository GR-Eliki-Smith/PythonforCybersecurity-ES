#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By Eliki Smith - 05/23/24

import requests
import configparser

def get_api_key(key_name):
    config = configparser.ConfigParser()
    config.read('/home/justincase/secrets.ini')
    api_key = config["APIKeys"][key_name]
    return api_key

token = get_api_key("github")

url = "https://api.github.com/user/repos"

payload={}
headers={
    'Accept': 'application/json',
    'Authorization': 'Bearer' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)