import json
import os
import pyautogui
from time import sleep
from pyautogui import typewrite

class GlobalSettings():
    def __init__(self):
        self.fileLoaded : bool = False
        self.activeLine : int = 1
        self.activeFile : str = ""
        self.activeData : dict = []
    
    def setFileLoaded(self, isItSet : bool):
        self.fileLoaded = isItSet
    def getFileLoaded(self):
        return self.fileLoaded
    
    def setActiveLine(self,whatLine: int):
        self.activeLine = whatLine
    def getActiveLine(self):
        return self.activeLine
    
    def setActiveFile(self,whatFile: str):
        self.activeFile = whatFile
    def getActiveFile(self):
        return self.activeFile
    
    def setActiveData(self,whatData : dict):
        self.activeData = whatData
    def getActiveData(self):
        return self.activeData

settings = GlobalSettings()

def getList():


    if (os.path.exists(r"ExameWork\Lists\ary_" + settings.getActiveFile() + ".json")):
        file_path = r"ExameWork\Lists\ary_" + settings.getActiveFile() + ".json"
        with open(file_path) as file:
            settings.setFileLoaded(True)
            settings.setActiveData(json.load(file))
            
    else:
        print("File Dont exist")
        settings.setActiveFile("")
        sleep(1)


def createList(name : str):
    if (os.path.exists(r"ExameWork\Lists\ary_"+name+".json")):
        print("That List allready exists")
    else:
        open(r"ExameWork\Lists\ary_"+name+".json", "x")
        settings.setActiveFile(name)
        settings.setActiveData([])
        saveData()
        settings.setFileLoaded(True)
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

def saveData():
    if (os.path.exists(r"ExameWork\Lists\ary_" + settings.getActiveFile() + ".json")):
        json_object = json.dumps(settings.getActiveData(), indent=4)
        with open(r"ExameWork\Lists\ary_" + settings.getActiveFile() + ".json", "w") as outfile:
            outfile.write(json_object)
        print("Save Sucssess")
    else:
        print(settings.getActiveFile())
        print("File Dose not Exist")
    return

def addItem(item : object):
    indexForWhereToPutTheItem = settings.getActiveLine()-1
    data = settings.getActiveData()
    data.insert(indexForWhereToPutTheItem,item)
    settings.setActiveData(data)
    return

def removeItem():
    data = settings.getActiveData()
    data.pop(settings.getActiveLine()-1)
    settings.setActiveData(data)
    return

def editItem():
    pos = settings.getActiveLine()-1
    data = settings.getActiveData()
    typewrite(data[pos]["Name"])
    data[pos]["Name"] = input("New Name:")
    typewrite(str(data[pos]["Price"]))
    data[pos]["Price"] = int(input("New Price:"))
    settings.setActiveData(data)
    return

def writeData():
    data = settings.getActiveData()
    for i in range(len(data)):
        if(i == settings.getActiveLine()-1):
            print("> ("+str(i+1)+") "+str(data[i])+ " <")
        else:
            print("("+str(i+1)+") "+str(data[i]))

def checkIfInputIsAViableNumber(userInput):
    try:
        userInput = int(userInput)
        data = settings.getActiveData()
        if(userInput < len(data)+1 and userInput >0):
            settings.setActiveLine(userInput)
        else:
            print("No valid input given")
            sleep(1)
    except:
        print("No valid input given")
        sleep(1)
    return

def writeHelp():
    print("-- Help Menu --")
    print("(loadList) Lets you choose a list to work with")
    print("(createList) Creates a new List")
    print("(getLists) Get a list of all lists")
    print("(removeList) Remove a list")
    print("(end) Stops the program")

def init():
    os.system('cls')
    print('Write "help" if you dont know what to do')
    while True:    
        if(settings.getFileLoaded() == True):
            os.system('cls')
            writeData()
            print("(a)Add Item (e)Edit Item (r)Remove Item (1-"+str(len(settings.getActiveData()))+")Change Active Item (s)Save (Exit)Exit file ")
            userInput = input(":")
            match userInput:
                case "a":
                    name = input("Name?:")
                    price = input("Price?:")
                    try:
                        price = int(price)
                        item = {"Name":name,"Price":price}
                        addItem(item)
                    except:
                        print("Price needs to be a number")
                        sleep(1)
                case "e":
                    editItem()
                case "r":
                    removeItem()
                case "s":
                    saveData()
                    sleep(1)
                case "Exit":
                    os.system('cls')
                    settings.setFileLoaded(False)
                case _: 
                    checkIfInputIsAViableNumber(userInput)
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
                    settings.setActiveFile(input("Which?:"))
                    getList()
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
                    writeHelp()
                case "end":
                    break
                case _:
                    print('Write "help" to get valid commands')
        

init()