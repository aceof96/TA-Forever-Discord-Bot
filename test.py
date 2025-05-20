import os
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


UserList = {}
UserList = pickle.load(open('UserList.pickle', "rb"))
URL = f"https://api.taforever.com/data/game"
for i in UserList:
    queryURL = URL+ f"?filter=host.id==" + f"{i}"
    print(queryURL)
    userdata = requests.get(queryURL)
    game_dict = json.loads(userdata.text)
    json_response = userdata.json()
    for games in game_dict["data"]:
        print(games["id"])
        print(games["attributes"]["name"],f"playerstat#", games["relationships"]["playerStats"]['data'][0]['id'],f"playerstat#",games["relationships"]["playerStats"]['data'][1]['id'] , f"     Start Time", games["attributes"]["startTime"])
        StatID1 = games["relationships"]["playerStats"]['data'][0]['id']
        StatID2 = games["relationships"]["playerStats"]['data'][1]['id']
        playerStat1Query = f"http://api.taforever.com/data/gamePlayerStats/" +f"{StatID1}"
        playerStat2Query = f"http://api.taforever.com/data/gamePlayerStats/" +f"{StatID2}"
        StatData1 = requests.get(playerStat1Query)
        stat_dict1 = json.loads(StatData1.text)
        statData2 = requests.get(playerStat2Query)
        stat_dict2 = json.loads(statData2.text)
        id1 = stat_dict1["data"]["relationships"]["player"]["data"]["id"]
        id2 = stat_dict2["data"]["relationships"]["player"]["data"]["id"]
        mapjson = games["attributes"]["replayMeta"]
        map = json.loads(mapjson)
        print(id1, UserList.get(id1) ,stat_dict1["data"]["attributes"]["result"], UserList.get(id2),id2,stat_dict2["data"]["attributes"]["result"] , "on" , map["mapName"])
        print(map["mapName"])