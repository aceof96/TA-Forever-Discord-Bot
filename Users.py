import os
import json
import pickle
import requests

URL = f"https://api.taforever.com/data"

def AddUserbyName(username):
    queryURL = URL+ f"/player" + f"?filter=login==" + "\"" + f"{username}" + "\""
    print(queryURL)
    userdata = requests.get(queryURL)
    user_dict = json.loads(userdata.text)
    id = user_dict["data"][0]['id']
    UserList = {}
    UserList = pickle.load(open('UserList.pickle', "rb"))
    if id not in UserList:
        UserList[id] = username
        with open('UserList.pickle', 'wb') as handle:
            pickle.dump(UserList, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print("User has been added Succesfully")
    UserList = pickle.load(open('UserList.pickle', "rb"))
    print(UserList)
    return(UserList)

def DelUserbyName(username):
    queryURL = URL+ f"/player" + f"?filter=login==" + "\"" + f"{username}" + "\""
    print(queryURL)
    userdata = requests.get(queryURL)
    user_dict = json.loads(userdata.text)
    id = user_dict["data"][0]['id']
    UserList = {}
    print(id)
    UserList = pickle.load(open('UserList.pickle', "rb"))
    if id  in UserList:
        UserList.pop(id)
        print("hello")
        with open('UserList.pickle', 'wb') as handle:
            pickle.dump(UserList, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print("User has been removed Succesfully")
    UserList = pickle.load(open('UserList.pickle', "rb"))
    print(UserList)
    return(UserList)


def AddUserId(userid):
    queryURL = URL+ f"/player" + f"?filter=id==" + "\"" + f"{userid}" + "\""
    print(queryURL)
    userdata = requests.get(queryURL)
    user_dict = json.loads(userdata.text)
    username = user_dict["data"][0]['attributes']['login']
    UserList = {}
    UserList = pickle.load(open('UserList.pickle', "rb"))
    if userid not in UserList:
        UserList[userid] = username
        with open('UserList.pickle', 'wb') as handle:
            pickle.dump(UserList, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print("User has been added Succesfully")
    UserList = pickle.load(open('UserList.pickle', "rb"))
    print(UserList)

def RemoveUserId(userid):
    UserList = {}
    UserList = pickle.load(open('UserList.pickle', "rb"))
    if userid in UserList:
        UserList.pop(userid)
        with open('UserList.pickle', 'wb') as handle:
            pickle.dump(UserList, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print("User has been removed Succesfullyclea")
    UserList = pickle.load(open('UserList.pickle', "rb"))
    print(UserList)


#AddUserbyName("Chenman")
#DelUserbyName("CorKrag")
#AddUserId('779')
#RemoveUserId('779')