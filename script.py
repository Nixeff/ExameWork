import json
import os
import pyautogui
from time import sleep
from pyautogui import typewrite

fileLoaded : bool = False
activeLine : int = 1
activeFile : str = ""
activeData : dict = []

def getList(name : str):
    if (os.path.exists(r"ExameWork\Lists\ary_" + name + ".json")):
        file_path = r"ExameWork\Lists\ary_" + name + ".json"
        with open(file_path) as file:
            return json.load(file)
    else:
        print("File Dont exist")
        sleep(1)
        return False

def createList(name : str):
    if (os.path.exists(r"ExameWork\Lists\ary_"+name+".json")):
        print("That List allready exists")
    else:
        open(r"ExameWork\Lists\ary_"+name+".json", "x")
        saveData(name, [])
    return

def removeList(name: str):
    if (os.path.exists(r"ExameWork\Lists\ary_"+name+".json")):
        if(input("Are you sure? (y/n)") == "y"):
            os.remove(r"ExameWork\Lists\ary_"+name+".json")
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

def saveData(file: str, data: dict):
    if (os.path.exists(r"ExameWork\Lists\ary_" + file + ".json")):
        # Serializing json
        json_object = json.dumps(data, indent=4)
        
        # Writing to sample.json
        with open(r"ExameWork\Lists\ary_" + file + ".json", "w") as outfile:
            outfile.write(json_object)
        print("Save Sucssess")
    else:
        print(file)
        print("File Dose not Exist")
    return

def addItem(pos : int, item : str):
    activeData.insert(pos,item)
    return

def removeItem(pos : int):
    activeData.pop(pos)
    return

def editItem(pos:int):
    typewrite(activeData[pos]["Name"])
    activeData[pos]["Name"] = input("New Name:")
    typewrite(str(activeData[pos]["Cost"]))
    activeData[pos]["Cost"] = int(input("New Price:"))
    return

def init(fileLoaded,activeLine,activeFile,activeData):
    os.system('cls')
    print('Write "help" if you dont know what to do')
    while True:    
        if(fileLoaded == True):
            os.system('cls')
            for i in range(len(activeData)):
                if(i == activeLine-1):
                    print("> ("+str(i+1)+") "+str(activeData[i])+ " <")
                else:
                    print("("+str(i+1)+") "+str(activeData[i]))
            print("(a)Add Item (e)Edit Item (r)Remove Item (1-"+str(len(activeData))+")Change Active Item (s)Save (Exit)Exit file ")
            iput = input(":")
            match iput:
                case "a":
                    name = input("Name?:")
                    price = input("Price?:")
                    try:
                        price = int(price)
                        item = {"Name":name,"Price":price}
                        addItem(activeLine-1,item)
                    except:
                        print("Price needs to be a number")
                        sleep(1)
                case "e":
                    editItem(activeLine-1)
                case "r":
                    removeItem(activeLine-1)
                case "s":
                    saveData(activeFile,activeData)
                    
                    sleep(1)
                case "Exit":
                    os.system('cls')
                    fileLoaded = False
                case _: 
                    try:
                        iput = int(iput)
                        if(iput < len(activeData)+1 and iput >0):
                            activeLine = iput
                        else:
                            print("No valid input given")
                            sleep(1)
                    except:
                        print("No valid input given")
                        sleep(1)
                            

                
        else:
            match input("Input:"):
                case "renameList":
                    os.system('cls')
                    getLists()
                    tempName = input("Where?:")
                    if (os.path.exists(r"ExameWork\Lists\ary_" + tempName + ".json")):
                        os.rename(r"ExameWork\Lists\ary_" + tempName + ".json", r"ExameWork\Lists\ary_" +input("New Name:")+".json")
                case "loadList":
                    os.system('cls')
                    getLists()
                    activeFile = input("Which?:")
                    data = getList(activeFile)
                    if data == False:
                        print("Not a valid file")
                    else:    
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
                case "help":
                    os.system('cls')
                    print("-- Help Menu --")
                    print("(loadList) Lets you choose a list to work with")
                    print("(createList) Creates a new List")
                    print("(getLists) Get a list of all lists")
                    print("(removeList) Remove a list")
                    print("(end) Stops the program")
                case "end":
                    break
                case _:
                    print('Write "help" to get valid commands')
        

init(fileLoaded,activeLine,activeFile,activeData)