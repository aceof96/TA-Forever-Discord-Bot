import os
import wget
from dotenv import load_dotenv
import discord
import requests
import json
import pandas as pd
import datetime
import numpy as np
import pickle
from GameList import *
import asyncio
from discord.ext import tasks, commands
from itertools import cycle
import urllib
import urllib.request
import time
from Users import *

#intialises mappy variable so it can be used across main and latest function to return the maps url to post the maps img in discord
mappy = ""
#latest() cycles through all players and checks each player for a new game played, return new game or "No games found!" if a new game is not discovered among the players
def latest():
    #load in list of existing users from UserList.pickle file stored as arrays in binary file
    UserList = {}
    UserList = pickle.load(open('UserList.pickle', "rb")) 
    #URL for TAForEver API connections
    URL = f"https://api.taforever.com/data/game"
    #Cycle through each Player in the List, seek new game entries and return game results and data in a string to be posted to discord
    for i in UserList:
        #queryURL adds the users ID to the API call,  https://api.taforever.com/data/game?filter=host.id==(PlayersID) returns a list of all games the player has played
        queryURL = URL+ f"?filter=host.id==" + f"{i}"
        print(queryURL)
        #make the API call and store in variable userdata
        userdata = requests.get(queryURL)
        #parse the returned Json data into game_dict
        game_dict = json.loads(userdata.text)
        #need to confrim json_response is now redunant 
        json_response = userdata.json()
        #for each game in the players game history
        for games in game_dict["data"]:
            #Call checkIfExisiting() for each game ID found, if the game has not already been logged and posted to discord, gather the games data and return the game if the return is false a game has been found
            if checkIfExisiting(games["id"]) == False:
                #testing prints
                print(games["id"])
                print(games["attributes"]["name"],f"playerstat#", games["relationships"]["playerStats"]['data'][0]['id'],f"playerstat#",games["relationships"]["playerStats"]['data'][1]['id'] , f"     Start Time", games["attributes"]["startTime"])
                #StatID1 string to make api call to gather first player found results from the game, same for StatID2 second player results query
                StatID1 = games["relationships"]["playerStats"]['data'][0]['id']
                StatID2 = games["relationships"]["playerStats"]['data'][1]['id']
                #PlayerStat1Query and playerStat2Query are the full API calls to gather the games results data for both players as result data is stored in player specific call for all players
                playerStat1Query = f"http://api.taforever.com/data/gamePlayerStats/" +f"{StatID1}"
                playerStat2Query = f"http://api.taforever.com/data/gamePlayerStats/" +f"{StatID2}"
                #StatData1 and statData2 makes the api calls to server 
                #stat_dict1 and stat_dict2 parses the json data
                StatData1 = requests.get(playerStat1Query)
                stat_dict1 = json.loads(StatData1.text)
                statData2 = requests.get(playerStat2Query)
                stat_dict2 = json.loads(statData2.text)
                #user ids
                id1 = stat_dict1["data"]["relationships"]["player"]["data"]["id"]
                id2 = stat_dict2["data"]["relationships"]["player"]["data"]["id"]
                #result1 and result2, stores which player showed victory and which player showed defeat
                result1 = str(stat_dict1["data"]["attributes"]["result"])
                result2 =str(stat_dict2["data"]["attributes"]["result"])
                #store the map played in mapjson
                mapjson = games["attributes"]["replayMeta"]
                print(mapjson)
                #print("Hi?")
                #if mapjson varible is empty or a player is not showing the victory or defeat the game is still in play. remove the game and return to cycle back through later when the game is completed.
                if mapjson == None or result1 != "VICTORY" and result1 != "DEFEAT": 
                    print("ingame removing")
                    time.sleep(60)
                    RemoveGame(games["id"])
                    return "No new games found!"
                #map parses the maps data
                map = json.loads(mapjson)
                #MapName stores the map played name as a string
                MapName = str(map["mapName"])
                gameTime = str(games["attributes"]["startTime"])
                #initialise ResultComment to be used later
                ResultComment = ""
                #MapURL first part of api call to return maps img
                MapURL = f"https://content.taforever.com/maps/previews/mini/"
                #queryMapURL the full query to the URL of the img for the map
                queryMapURL = MapURL + str(MapName) + f".png"
                print(queryMapURL)
                #removes all spaces from the URL call as many map names have spaces which breaks the URL
                queryMapURL= queryMapURL.replace(" ", "%20")
                print(queryMapURL)
                #urllib.request.urlretrieve(queryMapURL, 'map.png')
                print("no img")
                mappy = queryMapURL
                print("? ", mappy)
                #urllib.urlretrieve(queryMapURL, "map.png")
                #if the player won the match set ResultComment to ANNHILATED if lost set to GOT WRECKED BY
                #return the games result string "Player1 result against player 2 on map name and the URL to the map" is then msged to discord in the Main function
                if result1 == "VICTORY":
                    ResultComment = "ANNHILATED"
                elif result1 == "DEFEAT":
                    ResultComment = "GOT WRECKED BY"
                return (str(UserList.get(id1)) + " " + ResultComment + " " + str(UserList.get(id2)) + " " +  " on " + MapName + " " + gameTime + "|" + mappy)
    return "No new games found!"
#discord bot intialisation 
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#status to cycle the status of the discord bot in discord 
status = cycle(['Return OF THE GHENIM!', 'YoMAMA', 'NO! CTRLDED COMMANDER', 'CRTL DEEZ NUTZ', 'MEG Will FALL!', 'Dismal Kunt','TO TO TO TOTAL ANNNNNIHILATION'])
#Main loop, runs every 60seconds to refresh player games without pinging the game server too often
@tasks.loop(seconds=60)
async def check_games():
    #cycle the bots status in discord
    await client.change_presence(activity=discord.Game(next(status)))
    #input which dicord channel you want the bot to post and be active in
    load_dotenv()
    CHANNEL = os.getenv('DISCORD_CHANNEL')
    channel = client.get_channel(CHANNEL)
    #URL = f"https://content.taforever.com/maps/previews/mini/RANKED%201v1%20Ayri.png"
    #map = requests.get(URL)
    #if os.path.isfile('map.png'):
    #runs latest to get lates to get the latest game to post if existing
    message = str(latest())
    mes = message.split("|")
    #checks if a new game was returned if a new game is found sends a message with the games stats and a second msg with the map played image
    if message != "No new games found!":
        await channel.send(mes[0])
        await channel.send(mes[1])
    #await channel.send(str(latest()))
    print(mappy)
  #  await channel.send("https://content.taforever.com/maps/previews/mini/RANKED%201v1%20Baydot.png")
    #else:
 #   await channel.send(str(latest()))
 #   try:
 #       os.remove('map.png')
 #   except OSError:
 #       pass


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    check_games.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
        return
    if message.content.startswith('$AddUserbyName'):
        name = message.content.split(' ')[1]
        await message.channel.send(AddUserbyName(name))
    if message.content.startswith('$DelUserbyName'):
        name = message.content.split(' ')[1]
        await message.channel.send(DelUserbyName(name))

#client = check_games(intents=discord.Intents.default())
#discord token should be placed below

#get discord token from .env and client run discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)



#GameList = {}
#GameList = pickle.load(open('GameList.pickle', "rb"))
#print(GameList)
#print(UserList)


