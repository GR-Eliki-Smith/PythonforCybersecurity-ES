import requests
import json


api_key = "896388d984f2fe4ed42504b44db71ad2425d719a7e0edeae7617c9693d7fffbb"
url = "https://www.virustotal.com/vtapi/v2/url/scan"
params = {
    "url": "https://github.com/Lewisk3/GZDoom_Descent/releases",
    "apikey": api_key
}
response = requests.post(url, data=params)
print(json.dumps(response.json(), indent=4))


