import requests

URL = "https://api.ciscospark.com/v1/messages"
ACCESS_TOKEN = "MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0"

HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
PAYLOAD = {"toPersonEmail" : "adventure@sparkbot.io", "text" : "Hello"}

response = requests.post(url=URL, json=PAYLOAD, headers=HEADERS)

markdown = ["**Warning!!!**",
            "*Warning!!!*",
            "[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)"]

for message in markdown:
    MDPAYLOAD = {"toPersonEmail": "adventure@sparkbot.io", "markdown": message}
    mdresponse = requests.post(url=URL, json=MDPAYLOAD, headers=HEADERS)

print("response status code is: ", mdresponse.status_code)
print(mdresponse.text)