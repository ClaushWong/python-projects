from random import *
import os

#Open File, Retrieve Data and Close File
file_y = open("resource/resource.txt","r")
file_y_read = file_y.readlines()
file_y.close()

#Declare Dictionary
info = {}
resource = {}
#Data use to store the amount of material that user do
data = {}

#Declare list
dataName = {"1":"Log",
            "2":"Pebble",
            "3":"Plank",
            "4":"Stick",
            "5":"Cobblestone",
            "6":"Iron Ore",
            "7":"Gold Ore",
            "8":"Iron Ingot",
            "9":"Gold Ingot",
            "10":"Furnance",
            "11":"Wooden Axe",
            "12":"Wooden Pickaxe",
            "13":"Stone Axe",
            "14":"Stone Pickaxe",
            "15":"Iron Axe",
            "16":"Iron Pickaxe",
            "17":"Gold Axe",
            "18":"Gold Pickaxe",
            "19":"Ruby Ore",
            "20":"Sapphire Ore",
            "21":"Emerald Ore",
            "22":"Ruby Gem",
            "23":"Sapphire Gem",
            "24":"Emerald Gem",
            "25":"Ruby Axe",
            "26":"Ruby Pickaxe",
            "27":"Sapphire Axe",
            "28":"Sapphire Pickaxe",
            "29":"Emerald Axe",
            "30":"Emerald Pickaxe",
            "31":"Chalcocite",
            "32":"Bauxite",
            "33":"Acanthite",
            "34":"Galena",
            "35":"Uraninite",
            "36":"Copper Ingot",
            "37":"Aluminium Ingot",
            "38":"Silver Ingot",
            "39":"Lead Ingot",
            "40":"Uranium"
            }


#Data Storing
for x in range(len(file_y_read)):
    info[str(x+1)] = file_y_read[x]
    splitInfo = info[str(x+1)].split("=")
    resource[str(x+1)] = splitInfo
    #Remove the "\n" from string
    m = list(resource[str(x+1)][1])
    try :
        deleteChar = m.index("\n")
    except :
        pass
    else :
        del(m[deleteChar])
    
    m = "".join(m)
    resource[str(x+1)][1] = m

#Organize types of variable
for x in range(len(resource)):
    try :
        data[str(x+1)] = int(resource[str(x+1)][1])
    except :
        data[str(x+1)] = resource[str(x+1)][1]

#Opening function
def intro():
    print "Welcome to Crafting Simulator Phase 3."
    print "Objective : ---."
    print "Have fun."

def resourceListC():
    global data, dataName
    print "\nResource List :"
    print dataName["1"] , ":" , data["1"]
    print dataName["2"] , ":" , data["2"]
    print dataName["3"] , ":" , data["3"]
    print dataName["4"] , ":" , data["4"]
    print dataName["5"] , ":" , data["5"]
    print dataName["8"] , ":" , data["8"]
    print dataName["9"] , ":" , data["9"]
    print dataName["22"] , ":" , data["22"]
    print dataName["23"] , ":" , data["23"]
    print dataName["24"] , ":" , data["24"]
    print dataName["10"] , ":" , data["10"]
    print dataName["11"] , ":" , data["11"]
    print dataName["12"] , ":" , data["12"]
    print dataName["13"] , ":" , data["13"]
    print dataName["14"] , ":" , data["14"]
    print dataName["15"] , ":" , data["15"]
    print dataName["16"] , ":" , data["16"]
    print dataName["17"] , ":" , data["17"]
    print dataName["18"] , ":" , data["18"]
    print dataName["25"] , ":" , data["25"]
    print dataName["26"] , ":" , data["26"]
    print dataName["27"] , ":" , data["27"]
    print dataName["28"] , ":" , data["28"]
    print dataName["29"] , ":" , data["29"]
    print dataName["30"] , ":" , data["30"]

def w_recipe1(craftID,amt,req):
    global data, dataName
    print "How many" , dataName[craftID] , "you want to craft?"
    amount = raw_input("Amount : ")
    try :
        amount = int(amount)

    except :
        print "This is not an integer. Please try again."
    
    else :
        if amount % amt == 0:
            real_amount = amount / amt
            if data[req] >= real_amount:
                data[req] -= real_amount
                data[craftID] += amount
                print "You successfully craft", amount , dataName[craftID] , "." 
            else :
                print "You lack resource."
        else :
            print "Your input is not valid. Try again."

def s_recipe1(craftID,amt,req):
    global data, dataName
    print "\nHow many",dataName[craftID],"you want to craft?\n"
    amount = raw_input("Amount:")
    try :
        amount = int(amount)
    except :
        print "This is not a integer. Please try again."
    else :
        if data[req] >= amount * amt:
            data[req] -= amount * amt
            data[craftID] += amount
            print "You successfully craft" , amount , dataName[craftID],"."
        else :
            print "You lack of resource."

def a_recipe2(craftID,unlock,req1,req2,amt1,amt2):
    global data, dataName
    if data[craftID] != "True":
        if data[req1] >= amt1 and data[req2] >= amt2:
            print "Item :" , dataName[craftID]
            print "Unlock :" , unlock
            print "Are you confirm want to craft", dataName[craftID] ,"? (y/n)"
            confirmation = raw_input("Action :")
            if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                data[req1] -= amt1
                data[req2] -= amt2
                data[craftID] = "True"
                print "You successfully craft a" , dataName[craftID] , "."
                print "[ Unlocked" , unlock , "]"
            elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                print "Ok... Come back if you want to craft it."
            else :
                print "I'll count it as no..."
                print "Ok... Come back if you want to craft it."
        else :
            print "Lack of resource."
    else :
        print "You already owned this item."

def a_smelt2(smeltID,amt,req1,rst):
    print "\nOhh... You want to smelt the" , dataName[smeltID] ,"hmm.."
    print "For every one of your" , dataName[smeltID] , ", you need to offer" , amt , dataName[int(req1)-1] , "."
    print "How many" , dataName[smeltID] , "you want to smelt?"
    amount = raw_input("Amount :")
    try :
        amount = int(amount)
    except :
        print "This is not an integer. Try again."
    else :
        if data[req1] >= amount * amt and data[smeltID] >= amount:
            print "Amount of" , dataName[smeltID] ,":" , amount
            print "Amount of" , dataName[req1] ,"Required :" , amount * amt
            print "Amount of" , dataName[rst] ,"Smelted :" , amount
            print "Are you sure want to smelt it?(y/n)"
            confirmation = raw_input("Confirm : ")
            if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                data[req1] -= amount * amt
                data[smeltID] -= amount
                data[rst] += amount
                print "You successfully smelt", amount ,"iron ingot."
            elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                print "Ok... Come back if you want to smelt it."
            else :
                print "I'll count it as no..."
                print "Ok... Come back if you want to craft it."
        else :
            print "You have no enough resource."

def resourceListS():
    global data, dataName
    print "\nResource List:"
    print dataName["1"] , ":" , data["1"]
    print dataName["6"] , ":" , data["6"]
    print dataName["7"] , ":" , data["7"]
    print dataName["8"] , ":" , data["8"]
    print dataName["9"] , ":" , data["9"]
    print dataName["19"] , ":" , data["19"]
    print dataName["20"] , ":" , data["20"]
    print dataName["21"] , ":" , data["21"]
    print dataName["22"] , ":" , data["22"]
    print dataName["23"] , ":" , data["23"]
    print dataName["24"] , ":" , data["24"]

def resourceListM():
    print "\nResource List:"
    print dataName["1"] , ":" , data["1"]
    print dataName["2"] , ":" , data["2"]
    print dataName["6"] , ":" , data["6"]
    print dataName["7"] , ":" , data["7"]
    print dataName["19"] , ":" , data["19"]
    print dataName["20"] , ":" , data["20"]
    print dataName["21"] , ":" , data["21"]

#Function when user mine ore
def mine():
    global data, dataName
    prob = random()
    if status2 == "Unavailable":
        print "You are not able to mine."
    elif status2 == "Upgrade : 0":
        amount = randint(1,5)
        print "\nYou mine" , amount , dataName["2"]
        data["2"] += amount
    elif status2 == "Upgrade : 1":
        if prob > 0.8:
            amount = randint(1,3)
            print "\nYou mine" , amount , dataName["7"]
            data["7"] += amount
        elif prob < 0.3 :
            amount = randint(1,3)
            print "\nYou mine" , amount , dataName["6"]
            data["6"] += amount
        else :
            amount = randint(5,10)
            print "\nYou mine" , amount , dataName["2"]
            data["2"] += amount
    elif status2 == "Upgrade : 1 [ Luck++ ]":
        if prob > 0.7:
            amount = randint(3,5)
            print "\nYou mine" , amount , dataName["7"]
            data["7"] += amount
        elif prob < 0.4 :
            amount = randint(3,5)
            print "\nYou mine" , amount , dataName["6"]
            data["6"] += amount
        else :
            amount = randint(10,15)
            print "\nYou mine" , amount , dataName["2"]
            data["2"] += amount
    elif status2 == "Upgrade : 2":
        if prob > 0.9:
            amountRSE = randint(1,3)
            print "\nYou mine" , amountRSE , dataName["19"]
            print "\nYou mine" , amountRSE , dataName["20"]
            print "\nYou mine" , amountRSE , dataName["21"]
            data["19"] += amountRSE
            data["20"] += amountRSE
            data["21"] += amountRSE
        elif prob < 0.3:
            amountIG = randint(5,7)
            print "\nYou mine" , amountIG , dataName["6"]
            print "\nYou mine" , amountIG , dataName["7"]
            data["6"] += amountIG
            data["7"] += amountIG
        else :
            amount = randint(10,13)
            print "\nYou mine" , amount , dataName["2"]
            data["2"] += amount
    elif status2 == "Upgrade : 2 [ Luck++ ]":
        if prob > 0.7:
            amountRSE = randint(3,5)
            print "\nYou mine" , amountRSE , dataName["19"]
            print "\nYou mine" , amountRSE , dataName["20"]
            print "\nYou mine" , amountRSE , dataName["21"]
            data["19"] += amountRSE
            data["20"] += amountRSE
            data["21"] += amountRSE
        elif prob < 0.4:
            amountIG = randint(7,10)
            print "\nYou mine" , amountIG , dataName["6"]
            print "\nYou mine" , amountIG , dataName["7"]
            data["6"] += amountIG
            data["7"] += amountIG
        else :
            amount = randint(13,15)
            print "\nYou mine" , amount , dataName["2"]
            data["2"] += amount

#Function when user want some wood
def chop():
    global data, dataName, status1
    if status1 == "Upgrade : 0":
        amount = randint(3,5)
        print "\nYou chop" , amount , dataName["1"]
        data["1"] += amount
    elif status1 == "Upgrade : 1":
        amount = randint(5,8)
        print "\nYou chop" , amount , dataName["1"]
        data["1"] += amount
    elif status1 == "Upgrade : 1 [ Luck++ ]":
        amount = randint(9,11)
        print "\nYou chop" , amount , dataName["1"]
        data["1"] += amount
    elif status1 == "Upgrade : 2":
        amount = randint(8,11)
        print "\nYou chop" , amount , dataName["1"]
        data["1"] += amount
    elif status1 == "Upgrade : 2 [ Luck++ ]":
        amount = randint(11,13)
        print "\nYou chop" , amount , dataName["1"]
        data["1"] += amount
    else :
        print "Error Occur. Contact creator ASAP."

def craft():
    global data,dataName
    os.system("cls")
    os.system("start Tkinter-Phase3.pyw")
    print "Welcome to workshop. Feel free to look around."
    print "What you want to craft? Type in the ID. Thanks."
    print "If you want to leave workshop, type in 99 in the ID."
    print "If you somehow lost your recipe window, type in 98 to get it back."
    
    resourceListC()

    craftID = raw_input("\nID : ")

    while craftID != "99":
        if craftID == "3":
            w_recipe1(craftID,4,"1")
        elif craftID == "4":
            w_recipe1(craftID,2,"3")
        elif craftID == "5":
            s_recipe1(craftID,4,"2")
        elif craftID == "10":
            a_recipe2(craftID,"Smelting","1","5",2,8)
        elif craftID == "11":
            a_recipe2(craftID,"Chop Wood [ Upgrade - 1 ]","3","4",3,2)
        elif craftID == "12":
            a_recipe2(craftID,"Mine Ore","1","4",3,2)
        elif craftID == "13" :
            a_recipe2(craftID,"Chop Wood [ Upgrade : 2 ]","5","4",3,2)
        elif craftID == "14":
            a_recipe2(craftID,"Mine Ore [ Upgrade : 1 ]","5","4",3,2)
        elif craftID == "15":
            a_recipe2(craftID,"Chop Wood [ Upgrade : 3 ]","8","4",3,2)
        elif craftID == "16":
            a_recipe2(craftID,"Mine Ore [ Upgrade : 2 ]","8","4",3,2)
        elif craftID == "17":
            a_recipe2(craftID,"Chop Wood [ Luck++ ]","9","4",3,2)
        elif craftID == "18":
            a_recipe2(craftID,"Mine Ore [ Luck++ ]","9","4",3,2)
        elif craftID == "25":
            a_recipe2(craftID,"Chop Wood [ Amount++ ]","22","4",3,2)
        elif craftID == "26":
            a_recipe2(craftID,"Mine Ore [ Amount++ ]","22","4",3,2)
        elif craftID == "27":
            a_recipe2(craftID,"Chop Wood [ Fatigue-- ]","23","4",3,2)       
        elif craftID == "28":
            a_recipe2(craftID,"Mine Ore [ Fatigue-- ]","23","4",3,2)
        elif craftID == "29":
            a_recipe2(craftID,"Chop Wood [ Time Consume - ]","24","4",3,2)
        elif craftID == "30":
            a_recipe2(craftID,"Mine Ore [ Time Consume - ]","24","4",3,2)
        elif craftID == "98":
            os.system("start Tkinter-Phase3.pyw")
        else :
            print "Invalid Input. try again."
        
        raw_input("\nPress Enter to Continue.")
        os.system("cls")
        print "Welcome to workshop. Feel free to look around."
        print "What you want to craft? Type in the ID. Thanks."
        print "If you want to leave workshop, type in 99 in the ID."

        resourceListC()

        craftID = raw_input("\nID : ")
    else :
        print "\nThanks for coming."

def smelt():
    os.system("cls")
    os.system("start Tkinter-Phase3.pyw")
    print "Welcome to smelting room... Just called it blacksmith..."
    print "The recipe window have everything cover smelting."
    print "If you don't have one, type in 98 to grab it."
    print "Type 99 to exit the blacksmith."
    print "Welcome. Which item would you like to smelt? Type in the ID."

    resourceListS()

    smeltID = raw_input("\nID : ")

    while smeltID != "99":
        status()
        if smeltID == "6":
            a_smelt2(smeltID,2,"1","8")
        elif smeltID == "7":
            a_smelt2(smeltID,2,"1","9")
        elif smeltID == "19":
            a_smelt2(smeltID,4,"1","22")
        elif smeltID == "20":
            a_smelt2(smeltID,4,"1","23")
        elif smeltID == "21":
            a_smelt2(smeltID,4,"1","24")
        elif smeltID == "98":
            os.system("start Tkinter-Phase3.pyw")
        else :
            print "Invalid input."

        raw_input("Press Enter to Continue.")
        os.system("cls")
        print "Welcome to smelting room... Just called it blacksmith..."
        print "The recipe window have everything cover smelting."
        print "If you don't have one, type in 98 to grab it."
        print "Type 99 to exit the blacksmith."
        print "Welcome. Which item would you like to smelt? Type in the ID."

        resourceListS()
        
        smeltID = raw_input("\nID : ")
    else :
        print "Come again next time."

def status():
    global data, status1, status2, status3, status4
    
    if data["11"] == "True":
        if data["13"] == "True":
            if data["15"] == "True":
                if data["17"] == "True":
                    status1 = "Upgrade : 2 [ Luck++ ]"
                else :
                    status1 = "Upgrade : 2"
            else :
                status1 = "Upgrade : 2"
        elif data["17"] == "True":
            status1 = "Upgrade : 1 [ Luck++ ]"
        else :
            status1 = "Upgrade : 1"
    elif data["13"] == "True":
        if data["15"] == "True":
            if data["17"] == "True":
                    status1 = "Upgrade : 2 [ Luck++ ]"
            else :
                    status1 = "Upgrade : 2"
        elif data["17"] == "True" :
            status1 = "Upgrade : 1 [ Luck++ ]"
        else :
            status1 = "Upgrade : 1"
    else :
        status1 = "Upgrade : 0"

    if data["12"] == "True":
        if data["14"] == "True":
            if data["16"] == "True":
                if data["18"] == "True":
                    status2 = "Upgrade : 2 [ Luck++ ]"
                else :
                    status2 = "Upgrade : 2"
            elif data["18"] == "True":
                status2 = "Upgrade : 1 [ Luck++ ]"
            else :
                status2 = "Upgrade : 1"
        else :
            status2 = "Upgrade : 0"
    else :
        status2 = "Unavailable"

    if data["10"] == "True":
        status3 = "Available"
    else :
        status3 = "Unavailable"
    
    if data["11"] and data["12"] and data["13"] and data["14"] and data["15"] and data["16"] and data["17"] and data["18"] and data["25"] and data["26"] and data["27"] and data["28"] and data["29"] and data["30"] == "True" :
        status4 = "WIN"
    else :
        status4 = "NOT WIN"

#Variable Declaration
status1 = ""
status2 = ""
status3 = ""
status4 = "NOT WIN"

intro()
status()
print "\nAction List :\n1. Chop Wood [" , status1 , "]"
print "2. Mine Ore [" , status2 , "]"
print "3. Drill"
print "4. Crafting"
print "5. Smelting [" , status3 , "]"
print "6. Laboratory"
print "7. Quit"
print "Win Condition : Obtain every tools."
print "Condition :" , status4

resourceListM()

action = raw_input("\nAction : ")

while action != "7" :
    if action == "1":
        chop()
    elif action == "2":
        if data["12"] == "True":
            mine()
        else :
            print "\nYou need" , dataName["12"] , "to mine."
    elif action == "4":
        craft()
    elif action == "5":
        if data["10"] == "True":
            smelt()
        else :
            print "\nYou need" , dataName["10"] , "to smelt ore."
    else :
        print "Invalid Input. Try again."
    
    raw_input("Press Enter to continue.")
    os.system("cls")
    intro()
    status()
    print "\nAction List :\n1. Chop Wood [" , status1 , "]"
    print "2. Mine Ore [" , status2 , "]"
    print "3. Drill"
    print "4. Crafting"
    print "5. Smelting [" , status3 , "]"
    print "6. Laboratory"
    print "7. Quit"
    print "Win Condition : Obtain every tools."
    print "Condition :" , status4

    resourceListM()

    action = raw_input("\nAction : ")
else :
    #Open File , Replace Data , Close File
    file_x = open("resource/resource.txt","w")
    for x in range(len(data)):
        file_x.write(resource[str(x+1)][0] + "=" + str(data[str(x+1)]) + "\n")
    file_x.close()