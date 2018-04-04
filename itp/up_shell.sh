#!/bin/sh
uptime=`uptime`
curl -X POST \
  --header "Authorization: Bearer MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0" \
  --header "Content-Type: application/json" \
  --data '{"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vZTQ0MWFkOTAtMzMwNi0xMWU4LTkyMzQtMzliZDY1ZmQ4YmVj","text" : "'"$uptime"'"}' \
  https://api.ciscospark.com/v1/messages