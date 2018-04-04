# Importing necessary modules
import requests
import json

#Disable warnings
requests.packages.urllib3.disable_warnings()

#Variables

url = "https://api.ciscospark.com/v1"
api_call = "/people"
#replace below {access-token} with your personal access token
access_token = "Bearer MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0"

#Header information
headers = { 
    "content-type" : "application/json; charset = utf-8",
    "authorization" : access_token
}

#Parameter variable
param = "?email=sqtest-ciscospark-travisuser@squared.example.com"
#param = "?email=c.tian@latrobe.edu.au"
#param = "?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNDg0NzM3ZTAtMjRhOS0xMWU4LWI0MmItMTE3ZmNjZGRhOTQ2"
#param = "?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZTQ0MWFkOTAtMzMwNi0xMWU4LTkyMzQtMzliZDY1ZmQ4YmVj"


#Coombine URL, API call and parameters variables
url +=api_call+param

response = requests.get(url, headers = headers, verify = False).json()

#Print the respond body
#print (response.text)

#'''
for item in response["items"]:
    print('Name: ' + item['displayName'])
    print('Email: ' + item['emails'][0])
#'''