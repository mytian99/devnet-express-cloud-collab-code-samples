import requests

URL = "https://api.ciscospark.com/v1/messages"
ACCESS_TOKEN = "MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0"

HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
PAYLOAD = {"toPersonEmail" : "ltu@sparkbot.io", "text" : "about"}

response = requests.post(url=URL, json=PAYLOAD, headers=HEADERS)

print("response status code is: ", response.status_code)
print(response.text)