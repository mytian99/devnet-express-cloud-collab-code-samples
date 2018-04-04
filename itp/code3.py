import requests

URL = "https://api.ciscospark.com/v1/rooms"
ACCESS_TOKEN = "MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0"

HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
PARAMS = {"type" : "group", "max" : "2"}

response = requests.get(url=URL, headers=HEADERS, params=PARAMS)

print("response status code is: ", response.status_code)

print(response.text)