from asyncio import sleep
import json
import os

fileLoaded = False
activeLine = 1
activeFile = ""
activeData = []

def getList(name):
    file_path = r"ExameWork\Lists\ary_" + name + ".json"
    activeFile = name
    with open(file_path) as file:
        return json.load(file)

def createList(name):
    if (os.path.exists(r"ExameWork\Lists\ary_"+name+".json")):
        print("That List allready exists")
    else:
        open(r"ExameWork\Lists\ary_"+name+".json", "x")
        addData(name, [])
    return

def removeList(name):
    if (os.path.exists(r"ExameWork\Lists\ary_"+name+".json")):
        if(input("Are you sure? (y/n)") == "y"):
            os.remove(r"Lists\ary_"+name+".json")
        else:
            print("")
    else:
        print("List dose not exist")
    return

def getLists():
    data = os.listdir(path=r"ExameWork\Lists")
    for i in range(len(data)):
        print((data[i].strip(".json")).strip("ary_"))
    return

def addData(file, data):
    if (os.path.exists(r"ExameWork\Lists\ary_"+file+".json")):
        # Serializing json
        json_object = json.dumps(data, indent=4)
        
        # Writing to sample.json
        with open(r"ExameWork\Lists\ary_"+file+".json", "w") as outfile:
            outfile.write(json_object)
    return

while True:    
    if(fileLoaded == True):
        os.system('cls')
        for i in range(len(activeData)):
            if(i == activeLine-1):
                print("> ("+str(i+1)+") "+str(activeData[i])+ " <")
            else:
                print("("+str(i+1)+") "+str(activeData[i]))
        print("(a)Add Item (e)Edit Item (r)Remove Item (1+)Change Active Item (Exit) exit file ")
        iput = input(":")
        match iput:
            case "a":
                print("Add Item")
            case "e":
                print("Edit Item")
            case "r":
                print("Remove Item")
            case "Exit":
                fileLoaded = False
            case _: 
                try:
                    iput = int(iput)
                    activeLine = iput
                except:
                    print("No valid input given")
                    sleep(1)
                        

            
    else:
        match input("Input:"):
            case "loadList":
                os.system('cls')
                getLists()
                data = getList(input("Which?:"))
                activeData = data
                fileLoaded = True
                print(data)
            case "createList":
                os.system('cls')
                createList(input("Name?:"))
            case "getLists":
                os.system('cls')
                getLists()
            case "removeList":
                os.system('cls')
                getLists()
                removeList(input("Name?:"))
            case "end":
                break
    


    