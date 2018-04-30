import os
from random import *
import sys

#Opening function
def intro():
    print "Welcome to Crafting Simulator Phase 1."
    print "Objective : Obtain either one Iron Ingot or one Gold Ingot."
    print "Have fun."

#Function when user mine ore
def mine():
    global resource
    if resource["14"][1] == "True":
        prob = random()
        if prob > 0.8:
            amount = randint(1,3)
            print "\nYou mine" , amount , resource["7"][0]
            resource["7"][1] += amount
        elif prob < 0.3 :
            amount = randint(1,3)
            print "\nYou mine" , amount , resource["6"][0]
            resource["6"][1] += amount
        else :
            amount = randint(5,10)
            print "\nYou mine" , amount , resource["2"][0]
            resource["2"][1] += amount
    else :
        amount = randint(1,5)
        print "\nYou mine" , amount , resource["2"][0]
        resource["2"][1] += amount

#Function when user want some wood
def chop():
    global resource
    if resource["11"][1] == "True":
        if resource["13"][1] == "True":
            amount = randint(5,8)
            print "\nYou chop" , amount , resource["1"][0]
            resource["1"][1] += amount
        else :
            amount = randint(3,5)
            print "\nYou chop" , amount , resource["1"][0]
            resource["1"][1] += amount
    else :
        amount = randint(1,3)
        print "\nYou chop" , amount , resource["1"][0]
        resource["1"][1] += amount

def craft():
    global resource
    os.system("cls")
    os.system("start Tkinter-Phase1.pyw")
    print "Welcome to workshop. Feel free to look around."
    print "What you want to craft? Type in the ID. Thanks."
    print "If you want to leave workshop, type in 99 in the ID."
    print "If you somehow lost your recipe window, type in 98 to get it back."

    print "\nResource List :"
    print resource["1"][0] , ":" , resource["1"][1]
    print resource["2"][0] , ":" , resource["2"][1]
    print resource["3"][0] , ":" , resource["3"][1]
    print resource["4"][0] , ":" , resource["4"][1]
    print resource["5"][0] , ":" , resource["5"][1]
    print resource["10"][0] , ":" , resource["10"][1]
    print resource["11"][0] , ":" , resource["11"][1]
    print resource["12"][0] , ":" , resource["12"][1]
    print resource["13"][0] , ":" , resource["13"][1]
    print resource["14"][0] , ":" , resource["14"][1]

    craftID = raw_input("\nID : ")
    while craftID != "99" :
        if craftID == "3":
            amount = input("\nHow many planks you want to craft?\n")
            if amount % 4 == 0:
                real_amount = amount / 4
                if resource["1"][1] >= real_amount:
                    resource["1"][1] -= real_amount
                    resource[craftID][1] += amount
                    print "You successfully craft", amount , resource[craftID][0] , "." 
                else :
                    print "You lack resource."
            else :
                print "Your input is not valid. Try again."
        elif craftID == "4":
            amount = input("\nHow many sticks you want to craft?\n")
            if amount % 2 == 0:
                real_amount = amount / 2
                if resource["3"][1] >= real_amount:
                    resource["3"][1] -= real_amount
                    resource[craftID][1] += amount 
                    print "You successfully craft" , amount , resource[craftID][0] ,"."
                else :
                    print "You lack resource."
            else :
                print "Your input is not valid. Try again."
        elif craftID == "5":
            amount = input("\nHow many cobblestone you want to craft?\n")
            if resource["2"][1] >= amount * 4:
                resource["2"][1] -= amount * 4
                resource[craftID][1] += amount
                print "You successfully craft" , amount , resource[craftID][0] ,"."
            else :
                print "You lack of resource."
        elif craftID == "10":
            if resource["5"][1] >= 8 and resource["1"][1] >= 2:
                print "Item : Furnance"
                print "Unlock : Smelting"
                confirmation = raw_input("Are you confirm want to craft furnance? (y/n)\nAction :")
                if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                    resource["5"][1] -= 8
                    resource["1"][1] -= 2
                    resource["10"][1] = "True"
                    print "You successfully craft a furnance."
                    print "[ Unlocked Smelting ]"
                elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                    print "Ok... Come back if you want to craft it."
                else :
                    print "I'll count it as no..."
                    print "Ok... Come back if you want to craft it."
            else :
                print "Lack of resource."
        elif craftID == "11":
            if resource["3"][1] >= 3 and resource["4"][1] >= 2:
                print "Item : Wooden Axe"
                print "Unlock : Chop wood [ Upgrade - 1 ]"
                confirmation = raw_input("Are you confirm want to craft wooden axe? (y/n)\nAction :")
                if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                    resource["3"][1] -= 3
                    resource["4"][1] -= 2
                    resource["11"][1] = "True"
                    print "You successfully craft a wooden axe."
                    print "{ Unlocked : Chop Wood [ Upgrade - 1 ] }"
                elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                    print "Ok... Come back if you want to craft it."
                else :
                    print "I'll count it as no..."
                    print "Ok... Come back if you want to craft it."
            else :
                print "Lack of resource."
        elif craftID == "12":
            if resource["1"][1] >= 3 and resource["4"][1] >= 2:
                print "Item : Wooden Pickaxe"
                print "Unlock : Mine Ore"
                confirmation = raw_input("Are you confirm want to craft wooden pickaxe? (y/n)\nAction :")
                if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                    resource["1"][1] -= 3
                    resource["4"][1] -= 2
                    resource["12"][1] = "True"
                    print "You successfully craft a wooden pickaxe."
                    print "[ Unlocked : Mine Ore ]"
                elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                    print "Ok... Come back if you want to craft it."
                else :
                    print "I'll count it as no..."
                    print "Ok... Come back if you want to craft it."
            else :
                print "You lack resource."
        elif craftID == "13" :
            if resource["5"][1] >= 3 and resource["4"][1] >= 2:
                print "Item : Stone Axe"
                print "Unlock : Chop Wood [ Upgrade : 2 ]"
                confirmation = raw_input("Are you confirm want to craft stone axe? (y/n)\nAction :")
                if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                    resource["5"][1] -= 3
                    resource["4"][1] -= 2
                    resource["13"][1] = "True"
                    print "You successfully craft a stone axe."
                    print "{ Unlocked : Chop Wood [ Upgrade : 2 ] }"
                elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                    print "Ok... Come back if you want to craft it."
                else :
                    print "I'll count it as no..."
                    print "Ok... Come back if you want to craft it."
            else :
                print "You lack resource."
        elif craftID == "14":
            if resource["5"][1] >= 3 and resource["4"][1] >= 2:
                print "Item : Stone Pickaxe"
                print "Unlock : Mine Ore [ Upgrade : 1 ]"
                confirmation = raw_input("Are you confirm want to craft stone pickaxe? (y/n)\nAction :")
                if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                    resource["5"][1] -= 3
                    resource["4"][1] -= 2
                    resource["14"][1] = "True"
                    print "You successfully craft a stone pickaxe."
                    print "{ Unlocked : Mine Ore [ Upgrade : 1 ] }"
                elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                    print "Ok... Come back if you want to craft it."
                else :
                    print "I'll count it as no..."
                    print "Ok... Come back if you want to craft it."
            else :
                print "You lack resource."
        elif craftID == "98":
            os.system("start Tkinter-Phase1.pyw")
        else :
            print "Invalid Input. try again."
        
        raw_input("\nPress Enter to Continue.")
        os.system("cls")
        print "Welcome to workshop. Feel free to look around."
        print "What you want to craft? Type in the ID. Thanks."
        print "If you want to leave workshop, type in 99 in the ID."

        print "\nResource List :"
        print resource["1"][0] , ":" , resource["1"][1]
        print resource["2"][0] , ":" , resource["2"][1]
        print resource["3"][0] , ":" , resource["3"][1]
        print resource["4"][0] , ":" , resource["4"][1]
        print resource["5"][0] , ":" , resource["5"][1]
        print resource["10"][0] , ":" , resource["10"][1]
        print resource["11"][0] , ":" , resource["11"][1]
        print resource["12"][0] , ":" , resource["12"][1]
        print resource["13"][0] , ":" , resource["13"][1]
        print resource["14"][0] , ":" , resource["14"][1]

        craftID = raw_input("\nID : ")
    else :
        print "\nThanks for coming."


def smelt():
    os.system("cls")
    os.system("start Tkinter-Phase1.pyw")
    print "Welcome to smelting room... Just called it blacksmith..."
    print "The recipe window have everything cover smelting."
    print "If you don't have one, type in 98 to grab it."
    print "Type 99 to exit the blacksmith."
    print "Welcome. Which item would you like to smelt? Type in the ID."

    print "\nResource List:"
    print resource["6"][0] , ":" , resource["6"][1]
    print resource["7"][0] , ":" , resource["7"][1]
    print resource["8"][0] , ":" , resource["8"][1]
    print resource["9"][0] , ":" , resource["9"][1]

    smeltID = raw_input("\nID : ")
    while smeltID != "99":
        status()
        if smeltID == "6":
            print "\nOhh... You want to smelt the" , resource[smeltID][0] ,"hmm.."
            print "For every one of your" , resource[smeltID][0] , ", you need to offer 2 log."
            print "How many" , resource[smeltID][0] , "you want to smelt?"
            amount = input("Amount :")
            if resource["1"][1] >= amount * 2:
                print "Amount of Iron Ore :" , amount
                print "Amount of Log Required :" , amount * 2
                print "Amount of Iron Ingot Smelted :" , amount
                print "Are you sure want to smelt it?(y/n)"
                confirmation = raw_input("Confirm : ")
                if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                    resource["1"][1] -= amount * 2
                    resource["6"][1] -= amount
                    resource["8"][1] += amount
                    print "You successfully smelt", amount ,"iron ingot."
                elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                    print "Ok... Come back if you want to smelt it."
                else :
                    print "I'll count it as no..."
                    print "Ok... Come back if you want to craft it."
            else :
                print "You have no enough resource."
        elif smeltID == "7":
            print "\nOhh... You want to smelt the" , resource[smeltID][0] ,"hmm.."
            print "For every one of your" , resource[smeltID][0] , ", you need to offer 2 log."
            print "How many" , resource[smeltID][0] , "you want to smelt?"
            amount = raw_input("Amount :")
            if resource["1"][1] >= amount * 2:
                print "Amount of Iron Ore :" , amount
                print "Amount of Log Required :" , amount * 2
                print "Amount of Iron Ingot Smelted :" , amount
                print "Are you sure want to smelt it?(y/n)"
                confirmation = raw_input("Confirm : ")
                if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation =="yes":
                    resource["1"][1] -= amount * 2
                    resource["7"][1] -= amount
                    resource["9"][1] += amount
                    print "You successfully smelt", amount ,"iron ingot."
                elif confirmation == "n" or confirmation == "N" or confirmation == "No" or confirmation == "no" :
                    print "Ok... Come back if you want to smelt it."
                else :
                    print "I'll count it as no..."
                    print "Ok... Come back if you want to craft it."
            else :
                print "You have no enough resource."
        elif smeltID == "98":
            os.system("start Tkinter-Phase1.pyw")
        else :
            print "Invalid input."
        
        raw_input("Press Enter to Continue.")
        os.system("cls")
        print "Welcome to smelting room... Just called it blacksmith..."
        print "The recipe window have everything cover smelting."
        print "If you don't have one, type in 98 to grab it."
        print "Type 99 to exit the blacksmith."
        print "Welcome. Which item would you like to smelt? Type in the ID."

        print "\nResource List:"
        print resource["6"][0] , ":" , resource["6"][1]
        print resource["7"][0] , ":" , resource["7"][1]
        print resource["8"][0] , ":" , resource["8"][1]
        print resource["9"][0] , ":" , resource["9"][1]

        smeltID = raw_input("\nID : ")
    else :
        print "Come again next time."

#Variable Declaration
status1 = ""
status2 = ""
status3 = ""
status4 = "NOT WIN"

#Open File Session
id1 = open("resource/log.txt","r")
id2 = open("resource/pebble.txt","r")
id3 = open("resource/plank.txt","r")
id4 = open("resource/stick.txt","r")
id5 = open("resource/cobblestone.txt","r")
id6 = open("resource/iron_ore.txt","r")
id7 = open("resource/gold_ore.txt","r")
id8 = open("resource/iron_ingot.txt","r")
id9 = open("resource/gold_ingot.txt","r")
id10 = open("resource/furnance.txt","r")
id11 = open("resource/w_axe.txt","r")
id12 = open("resource/w_pickaxe.txt","r")
id13 = open("resource/s_axe.txt","r")
id14 = open("resource/s_pickaxe.txt","r")

#Read File Session
id1_r = int(id1.read())
id2_r = int(id2.read())
id3_r = int(id3.read())
id4_r = int(id4.read())
id5_r = int(id5.read())
id6_r = int(id6.read())
id7_r = int(id7.read())
id8_r = int(id8.read())
id9_r = int(id9.read())
id10_r = id10.read()
id11_r = id11.read()
id12_r = id12.read()
id13_r = id13.read()
id14_r = id14.read()

#Close File Session
id1.close()
id2.close()
id3.close()
id4.close()
id5.close()
id6.close()
id7.close()
id8.close()
id9.close()
id10.close()
id11.close()
id12.close()
id13.close()
id14.close()

#Data Stored Session
resource = {}
resource["1"] = ["Log",id1_r]
resource["2"] = ["Pebble",id2_r]
resource["3"] = ["Plank",id3_r]
resource["4"] = ["Stick",id4_r]
resource["5"] = ["Cobblestone",id5_r]
resource["6"] = ["Iron Ore",id6_r]
resource["7"] = ["Gold Ore",id7_r]
resource["8"] = ["Iron Ingot",id8_r]
resource["9"] = ["Gold Ingot",id9_r]
resource["10"] = ["Furnance",id10_r]
resource["11"] = ["Wooden Axe",id11_r]
resource["12"] = ["Wooden Pickaxe",id12_r]
resource["13"] = ["Stone Axe",id13_r]
resource["14"] = ["Stone Pickaxe",id14_r]

#Status For Action
def status():
    global resource, status1, status2, status3
    
    if resource["11"][1] == "True":
        if resource["13"][1] == "True":
            status1 = "Upgrade : 2"
        else :
            status1 = "Upgrade : 1"
    else :
        status1 = "Upgrade : 0"

    if resource["12"][1] == "True":
        if resource["14"][1] == "True":
            status2 = "Upgrade : 1"
        else :
            status2 = "Upgrade : 0"
    else :
        status2 = "Unavailable"

    if resource["10"][1] == "True":
        status3 = "Available"
    else :
        status3 = "Unavailable"
    
    if resource["8"][1] >= 1 or resource["9"][1] >= 1 :
        status4 = "WIN"
    else :
        status4 = "NOT WIN"

intro()
status()
print "\nAction List :\n1. Chop Wood [" , status1 , "]"
print "2. Mine Ore [" , status2 , "]"
print "3. Crafting"
print "4. Smelting [" , status3 , "]"
print "5. Quit"
print "Win Condition : Obtain either 1 Iron Ingot or 1 Gold Ingot."
print "Condition :" , status4

print "\nResource List:"
print resource["1"][0] , ":" , resource["1"][1]
print resource["2"][0] , ":" , resource["2"][1]
print resource["6"][0] , ":" , resource["6"][1]
print resource["7"][0] , ":" , resource["7"][1]

action = raw_input("\nAction : ")

while action != "5" :
    if action == "1":
        chop()
    elif action == "2":
        if resource["12"][1] == "True":
            mine()
        else :
            print "\nYou need" , resource["12"][0] , "to mine."
    elif action == "3":
        craft()
    elif action == "4":
        if resource["10"][1] == "True":
            smelt()
        else :
            print "\nYou need" , resource["10"][0] , "to smelt ore."
    else :
        print "Invalid Input. Try again."
    raw_input("Press Enter to continue.")
    os.system("cls")
    intro()
    status()
    print "\nAction List :\n1. Chop Wood [" , status1 , "]"
    print "2. Mine Ore [" , status2 , "]"
    print "3. Crafting"
    print "4. Smelting"
    print "5. Quit"

    print "\nResource List:"
    print resource["1"][0] , ":" , resource["1"][1]
    print resource["2"][0] , ":" , resource["2"][1]
    print resource["6"][0] , ":" , resource["6"][1]
    print resource["7"][0] , ":" , resource["7"][1]

    action = raw_input("\nAction : ")
else :
    #Open File Session
    id1 = open("resource/log.txt","w")
    id2 = open("resource/pebble.txt","w")
    id3 = open("resource/plank.txt","w")
    id4 = open("resource/stick.txt","w")
    id5 = open("resource/cobblestone.txt","w")
    id6 = open("resource/iron_ore.txt","w")
    id7 = open("resource/gold_ore.txt","w")
    id8 = open("resource/iron_ingot.txt","w")
    id9 = open("resource/gold_ingot.txt","w")
    id10 = open("resource/furnance.txt","w")
    id11 = open("resource/w_axe.txt","w")
    id12 = open("resource/w_pickaxe.txt","w")
    id13 = open("resource/s_axe.txt","w")
    id14 = open("resource/s_pickaxe.txt","w")

    #Insert 'NEW' Data Session
    id1.write(str(resource["1"][1]))
    id2.write(str(resource["2"][1]))
    id3.write(str(resource["3"][1]))
    id4.write(str(resource["4"][1]))
    id5.write(str(resource["5"][1]))
    id6.write(str(resource["6"][1]))
    id7.write(str(resource["7"][1]))
    id8.write(str(resource["8"][1]))
    id9.write(str(resource["9"][1]))
    id10.write(resource["10"][1])
    id11.write(resource["11"][1])
    id12.write(resource["12"][1])
    id13.write(resource["13"][1])
    id14.write(resource["14"][1])

    #Close File Session
    id1.close()
    id2.close()
    id3.close()
    id4.close()
    id5.close()
    id6.close()
    id7.close()
    id8.close()
    id9.close()
    id10.close()
    id11.close()
    id12.close()
    id13.close()
    id14.close()

    sys.exit()
