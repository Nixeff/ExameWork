import json
import os

def getList(name):
    return json.load(open(r'ExameWork\Lists\list_'+name+'.json'))

def createList(name):
    return

def getLists():
    data = os.listdir(path="ExameWork\Lists")
    print(len(data));
    for i in range(len(data)):
        print((data[i].strip(".json")).strip("ary_"))
        return
    

match input():
    case "loadList":
        data = getList(input("Which?:"))
        print(data)
    case "createList":
        print("Created List")
    case "getLists":
        getLists()

    
    