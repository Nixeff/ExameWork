import json
import os

def getList(name):
    file_path = r"ExameWork\Lists\ary_" + name + ".json"
    with open(file_path) as file:
        return json.load(file)

def createList(name):
    return

def getLists():
    data = os.listdir(path="Lists")
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

    
    