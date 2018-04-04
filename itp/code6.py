from ciscosparkapi import CiscoSparkAPI
import requests
#import  CiscoSparkAPI 
# MISSION: Module name is missing
import json

# Global variables

ACCESS_TOKEN = "MTU3NmUzZDMtMGRiYi00OGJkLTgxNzItNGVjNWQ3YjA4ODJiY2MyZDVmMTktZTA0" 
# Token can be obtained from https://developer.ciscospark.com/ page

HEADERS = {"Content-type": "application/json",
           "Authorization": "Bearer " + ACCESS_TOKEN}


def create_team(team_name):
    """
    This function will create a team based on
    provided name and will return team's ID
    """
    print("Creating the team ...")

    URL = "https://api.ciscospark.com/v1/teams" 
    # MISSION: Provide URL for creating Team
    PAYLOAD = {"name": team_name}

    response = requests.post(url=URL, json=PAYLOAD, headers=HEADERS)

    if response.status_code == 200:
        response = response.json()
        print("Team was successfully created.")
        print("Name: " + response["name"])
        print("ID: " + response["id"])
        return response["id"]
    else:
        print("Something went wrong.\n"
              "Please check the script and run it again!")
        exit()


def create_room(room_name, team_id):
    """
    This function will create a room based on
    provided name, associate a team with it and return the
    room ID
    """
    print("Crating the room...")
    URL = "https://api.ciscospark.com/v1/rooms"
    PAYLOAD = {"title": room_name, "teamId": team_id} 
    # MISSION: Key responsible for team ID is missing

    response = requests.post(url=URL, json=PAYLOAD, headers=HEADERS)

    if response.status_code == 200:
        response = response.json()
        print("Room was successfully created.")
        print("Name: " + response["title"])
        print("ID: " + response["id"])
        return response["id"]
    else:
        print("Something went wrong.\n"
              "Please check the script and run it again!")
        exit()


def post_message(room_id):
    """
    This function will post a message to the
    room based on provided room ID
    """
    text = input("test from Sam Tian ")
    URL = "https://api.ciscospark.com/v1/messages"
    PAYLOAD = {"roomId": room_id, "text": text}

    response = requests.post(url=URL, json=PAYLOAD, headers=HEADERS) 
    #MISSION: requests method is missing

    if response.status_code == 200:
        print("Your message was successfully posted to the room")
    else:
        print("Something went wrong.\n"
              "Please check the script and run it again!")
        exit()


def main():
    """
    Main function
    """
    team_id = create_team("IT-Pro Team")
    room_id = create_room("Room for IT Professionals", team_id)
    post_message(room_id)


if __name__ == "__main__":
    main()