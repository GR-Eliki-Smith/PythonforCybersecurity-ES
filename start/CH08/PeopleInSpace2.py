#!/usr/bin/env python3
# Script that tells us how many people there are in space
#By Eliki Smith - 05/21/24

#Import things
import requests

#get people in space function
def get_people_in_space():
    url = "http://api.open-notify.org/astros.json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    items = response.json()
    return items

#Print basic details
astronauts = get_people_in_space()
print(astronauts)

#Print only the number of people in space
ast_num = astronauts["number"]
print ("There are currently {0} people in space".format( ast_num ))