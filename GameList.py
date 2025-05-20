import os
import json
import pickle
import requests

def checkIfExisiting(gameID):
    GameList = {}
    GameList = pickle.load(open('GameList.pickle', "rb"))
    if gameID not in GameList:
        GameList.add(gameID)
        with open('GameList.pickle', 'wb') as handle:
            pickle.dump(GameList, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print("New Game Found")
        return False
    print("game already exists")
    return True



def RemoveGame(gamesID):
    GameList = {}
    print(gamesID)
    GameList = pickle.load(open('GameList.pickle', "rb"))
    try:
        GameList.remove(gamesID)
    except:
        print("oops")
        print(gamesID)
    with open('GameList.pickle', 'wb') as handle:
               pickle.dump(GameList, handle, protocol=pickle.HIGHEST_PROTOCOL)


#71255
#RemoveGame('71255')               
#GameList = {}
#GameList = pickle.load(open('GameList.pickle', "rb"))
#GameList.remove('1766')
#with open('GameList.pickle', 'wb') as handle:
#            pickle.dump(GameList, handle, protocol=pickle.HIGHEST_PROTOCOL)

#print(GameList)
#UserList = {'1614'}
#with open('GameList.pickle', 'wb') as handle:
    #pickle.dump(UserList, handle, protocol=pickle.HIGHEST_PROTOCOL)

#print(checkIfExisiting('1614'))

#GameList = {}
#GameList = pickle.load(open('GameList.pickle', "rb"))
#print(GameList)