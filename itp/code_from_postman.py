import requests

url = "https://api.ciscospark.com/v1/rooms"

headers = {
    'Authorization': "Bearer MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0",
    'Content-Type': "application/json; charset=utf-8",
    'Cache-Control': "no-cache",
    'Postman-Token': "86cbf527-4bd7-491c-a266-8d14d6d0c02a"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)