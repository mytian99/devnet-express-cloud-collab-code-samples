import requests,uptime,datetime,json

ut = str(datetime.timedelta(seconds=uptime.uptime()))
body = {"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vZTQ0MWFkOTAtMzMwNi0xMWU4LTkyMzQtMzliZDY1ZmQ4YmVj", "text" : ut}
headers = {
    "Authorization": "Bearer MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0",
    "Content-Type": "application/json"
    }
requests.request("POST", url="https://api.ciscospark.com/v1/messages",
    data=json.dumps(body), headers=headers)