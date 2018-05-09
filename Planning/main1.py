import Tkinter as t
import ttk
from random import *

username = "ClaushWong"
userID = "C0001"

day = 1
timeInt = 8
maxFatigue = 80
fatigue = maxFatigue
fatigueBar = str(fatigue) + " / " + str(maxFatigue)
level = 1
exp = 0
condition = (" AM" , " PM")
timeStr = str(timeInt).zfill(2) + ":00" + condition[0]
arr = []

amount = "Null"
display_amount = "Status : " + str(amount)

list_1 = ["Log","Pebble","Plank","Stick","Cobblestone","Iron Ore","Gold Ore","Iron Ingot","Gold Ingot","Furnance","Wooden Axe","Wooden Pickaxe","Stone Axe","Stone Pickaxe","Ruby Ore","Sapphire Ore","Emerald Ore","Ruby Gem","Sapphire Gem","Emerald Gem"]
amount_1 = [5,6,8,9,10,6,8,9,4,"False","False","False","False","False",9,5,1,0,0,0]

equip_axe = "Hand"
equip_pick = "Wooden Pickaxe"

username_text = "Username : " + username
userID_text = "UserID : " + userID + ""

root = t.Tk()
root.title("GUI")

def mine():
    global level, maxFatigue , fatigue, exp, timeInt, day, condition , day , amount_1 , list_1 , equip_pick
    ratio = 17
    if fatigue >= ratio:
        time = 3
        status = True
        if equip_pick == list_1[11]:
            #If user equip WOODEN PICKAXE
            amount = randint(1,5)
            #PEBBLES MINED
            print "You mine" , amount , list_1[1]
            #Print at GUI
            textValue = "You mine " + str(amount) + " " + list_1[1]
            check(textValue)
            amount_1[1] += amount
            
        elif equip_pick == list_1[13]:
            #If user equip STONE PICKAXE
            prob1 = random()
            prob2 = random()
            if prob1 > 0.7:
                #If random-generated number is greater than 0.7
                if prob2 > 0.6:
                    #If another random-generated number is greater than 0.6
                    amount = randint(1,3)
                    #GOLD ORE MINED
                    print "You mine" , amount , list_1[6]
                    amount_1[6] += amount
                else :
                    #If another random-generated number is less than 0.6
                    amount = randint(1,3)
                    #IRON ORE MINED
                    print "You mine" , amount , list_1[5]
                    amount_1[5] += amount
            else :
                #If random-generated number is less than 0.7 
                amount = randint(5,10)
                #PEBBLES MINE
                print "You mine" , amount , list_1[1]
                amount_1[1] += amount

        elif equip_pick == list_1[15]:
            #If user equip IRON PICKAXE
            prob1 = random()
            prob2 = random()
            if prob1 > 0.6:
                #If random-generated number is greater than 0.6
                if prob2 > 0.4:
                    #If another random-generated number is greater than 0.4
                    amount = randint(3,5)
                    #GOLD ORE MINED
                    print "You mine" , amount , list_1[6]
                    amount_1[6] += amount
                else :
                    #If another random-generated number is less than 0.4
                    amount = randint(5,7)
                    #IRON ORE MINED
                    print "You mine" , amount , list_1[5]
                    amount_1[5] += amount
            else :
                #If random-generated number is less than 0.6
                amount = randint(10,15)
                #PEBBLES MINED
                print "You mine" , amount , list_1[1]
                amount_1[1] += amount

        elif equip_pick == list_1[17]:
            #If user equip GOLD PICKAXE ( LUCK ++ )
            prob1 = random()
            prob2 = random()
            if prob1 > 0.4:
                #If random-generated number is greater than 0.4
                if prob2 > 0.4:
                    #If another random-generated number is greater than 0.4
                    amount = randint(5,8)
                    #GOLD ORE MINED
                    print "You mine" , amount , list_1[6]
                    amount_1[6] += amount
                else :
                    #If another random-generated number is less than 0.4
                    amount = randint(7,10)
                    #IRON ORE MINED
                    print "You mine" , amount , list_1[5]
                    amount_1[5] += amount
            else :
                #If random-generated number is less than 0.4
                amount = randint(15,20)
                #PEBBLES MINED
                print "You mine" , amount , list_1[1]
                amount_1[1] += amount

        elif equip_pick == list_1[24]:
            #If user equip RUBY PICKAXE ( AMOUNT ++ )
            prob1 = random()
            prob2 = random()
            if prob1 > 0.6:
                #If random-generated number is greater than 0.6
                if prob2 > 0.4:
                    #If another random-generated number is greater than 0.4
                    amount = randint(8,10)
                    #GOLD ORE MINED
                    print "You mine" , amount , list_1[6]
                    amount_1[6] += amount
                else :
                    #If another random-generated number is less than 0.4
                    amount = randint(10,15)
                    #IRON ORE MINED
                    print "You mine" , amount , list_1[5]
                    amount_1[5] += amount
            else :
                #If random-generated number is less than 0.6
                amount = randint(20,25)
                #PEBBLES MINED
                print "You mine" , amount , list_1[1]
                amount_1[1] += amount

        elif equip_pick == list_1[26]:
            #If user equip SAPPHIRE PICKAXE ( FATIGUE -- )
            prob1 = random()
            prob2 = random()
            if prob1 > 0.6:
                #If random-generated number is greater than 0.6
                if prob2 > 0.4:
                    #If another random-generated number is greater than 0.4
                    amount = randint(3,5)
                    #GOLD ORE MINED
                    print "You mine" , amount , list_1[6]
                    amount_1[6] += amount
                else :
                    #If another random-generated number is less than 0.4
                    amount = randint(5,7)
                    #IRON ORE MINED
                    print "You mine" , amount , list_1[5]
                    amount_1[5] += amount
            else :
                #If random-generated number is less than 0.6
                amount = randint(10,15)
                #PEBBLES MINED
                print "You mine" , amount , list_1[1]
                amount_1[1] += amount
            #Ratio decrease calculation
            ratio_drop = ratio * 0.6
            ratio = abs(ratio_drop)

        elif equip_pick == list_1[28]:
            #If user equip EMERALD PICKAXE ( Time used -- )
            prob1 = random()
            prob2 = random()
            if prob1 > 0.6:
                #If random-generated number is greater than 0.6
                if prob2 > 0.4:
                    #If another random-generated number is greater than 0.4
                    amount = randint(3,5)
                    #GOLD ORE MINED
                    print "You mine" , amount , list_1[6]
                    amount_1[6] += amount
                else :
                    #If another random-generated number is less than 0.4
                    amount = randint(5,7)
                    #IRON ORE MINED
                    print "You mine" , amount , list_1[5]
                    amount_1[5] += amount
            else :
                #If random-generated number is less than 0.6
                amount = randint(10,15)
                #PEBBLES MINED
                print "You mine" , amount , list_1[1]
                amount_1[1] += amount
            time = 2

        else :
            #If user didn't have a pickaxe
            print "You don't have a pickaxe"
            status = False

        for x in range(len(arr)):
            tk_textAll[x]["text"] = arr[x] 

        if status == True:
            # IF LEVEL UP == TRUE
            if p_bar["value"] == p_bar["maximum"] - 1:
                #Exp bar reset
                p_bar.step()
                exp += 1
                lbl_12["text"] = str(exp)
                p_bar["maximum"] = p_bar["maximum"] + 10
                p_bar["value"] = 0

                #Level up
                level += 1
                if level % 2 == 0:
                    maxFatigue += 2
                else :
                    maxFatigue += 3
                lbl_10["text"] = str(level)
                #Fatigue Reset
                fatigue = maxFatigue
                fatigueBar = str(fatigue) + " / " + str(maxFatigue)
                lbl_8["text"] = fatigueBar

            else :
                #Exp bar increase
                p_bar.step()
                #Fatigue drop
                fatigue -= ratio
                fatigueBar = str(fatigue) + " / " + str(maxFatigue)
                lbl_8["text"] = fatigueBar
                #Increase Exp
                exp += 1
                lbl_12["text"] = str(exp)
                #Time increse
                timeInt += time
                if timeInt > 12:
                    if timeInt >= 24:
                        x = 0
                        timeInt -= 24
                        day += 1
                        timeStr = str(timeInt).zfill(2) + ":00" + condition[x]
                    else :
                        x = 1
                        timeStr = str(timeInt-12).zfill(2) + ":00" + condition[x]
                else :
                    x = 0
                    timeStr = str(timeInt).zfill(2) + ":00" + condition[x]
                lbl_6["text"] = timeStr
        else :
            pass
                
    else :
        print "No enough fatigue"
        
def sleep():
    global timeInt , day , condition , maxFatigue , fatigue
    if timeInt >= 8:
        day += 1
        timeInt = 8
        x = 0
        timeStr = str(timeInt).zfill(2) + ":00" + condition[x]
    else :
        timeInt = 8
        x = 0
        timeStr = str(timeInt).zfill(2) + ":00" + condition[x]
    fatigue = maxFatigue
    fatigueBar = str(fatigue) + " / " + str(maxFatigue)
    lbl_6["text"] = timeStr
    lbl_4["text"] = day
    lbl_8["text"] = fatigueBar


def amount_find():
    global amount, list_1
    get_item = listbox1.get("active")
    index_list = list_1.index(get_item)
    amount = amount_1[index_list]
    if index_list in [9,10,11,12,13]:
        display_amount = "Status : " + str(amount)
    else :
        display_amount = "Amount : " + str(amount)
    lbl_14["text"] = display_amount

def check(textValue):
    global arr
    for x in range(len(arr)):
        if arr[x] == None:
            arr[x] = textValue
            break
        else :
            pass

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

aw = ws / 4
ah = hs / 4

#root.geometry('{}x{}'.format(640, 360))
root.geometry("640x480+" + str(aw) + "+" + str(ah))
root.resizable(False,False)

lbl_main = t.Label(root,text="Main Page")
lbl_main.config(font=("MS Serif",24,"bold"))
lbl_main.pack()

f1 = t.Frame(root)
f1.pack(side="top",fill="x")

f2 = t.Frame(root,borderwidth=25)
f2.pack(side="left")

f2_1 = t.Frame(f2, borderwidth=5,highlightbackground="black", highlightcolor="black", highlightthickness=1)
f2_1.pack(side="top")

nullLine2 = t.Label(f2,text="")
nullLine2.pack(side="top")

f2_2 = t.Frame(f2)
f2_2.pack(side="top")

f3 = t.Frame(root,borderwidth=50)
f3.pack(side="left")

f3_1 = t.Frame(f3,highlightbackground="black", highlightcolor="black", highlightthickness=1)
f3_1.grid(row=0,column=0)

f4 = t.Frame(root,borderwidth=25)
f4.pack(side="left")

lbl_1 = t.Label(f1,text=username_text)
lbl_1.pack(side="left",padx=100)

lbl_2 = t.Label(f1,text=userID_text)
lbl_2.pack(side="right",padx=100)

nullLine = t.Label(f1,text="")
nullLine.pack(side="top")

nullSpace1 = t.Label(f2_1,text="  ")
nullSpace1.grid(row=0,column=0)

nullSpace2 = t.Label(f2_1,text="  ")
nullSpace2.grid(row=0,column=3)

# lbl_5 and lbl_6 is output for current day in game
lbl_3 = t.Label(f2_1,text="Day :")
lbl_3.grid(row=0,column=1,sticky="w")

lbl_4 = t.Label(f2_1,text=day)
lbl_4.grid(row=0,column=2)

# lbl_5 and lbl_6 is output for current time in game
lbl_5 = t.Label(f2_1,text="Time :")
lbl_5.grid(row=1,column=1,sticky="w")

lbl_6 = t.Label(f2_1,text=timeStr)
lbl_6.grid(row=1,column=2)

# lbl_7 and lbl_8 is output for player's fatigue
lbl_7 = t.Label(f2_1,text="Fatigue :")
lbl_7.grid(row=2,column=1,sticky="w")

lbl_8 = t.Label(f2_1,text=fatigueBar)
lbl_8.grid(row=2,column=2)

# lbl_9 and lbl_10 is output for player's level
lbl_9 = t.Label(f2_1,text="Level :")
lbl_9.grid(row=3,column=1,sticky="w")

lbl_10 = t.Label(f2_1,text=str(level))
lbl_10.grid(row=3,column=2)

#lbl_11, lbl_12 and p_bar shows output for player's exp
lbl_11 = t.Label(f2_1,text="EXP :")
lbl_11.grid(row=4,column=1,sticky="w")

lbl_12 = t.Label(f2_1,text=exp)
lbl_12.grid(row=4,column=2)

p_bar = ttk.Progressbar(f2_1,maximum=10,value=str(exp))
p_bar.grid(row=4,column=3)

#lbl_13 show opening for frame 2.2
lbl_13 = t.Label(f2_2,text="Resource List")
lbl_13.pack()

scr_bar = ttk.Scrollbar(f2_2)
scr_bar.pack(side="left",fill="y")

#This listbox comes after user data
listbox1 = t.Listbox(f2_2,yscrollcommand=scr_bar.set)
listbox1.pack()

for x in list_1:
    listbox1.insert("end",x)

scr_bar.config(command=listbox1.yview)

button1 = ttk.Button(f2,text="Get Amount",command=amount_find)
button1.pack(side="top")

lbl_14 = t.Label(f2,text=display_amount)
lbl_14.pack(side="top")

#Frame 3
lbl_15 = t.Label(f3_1,text="Action",width=10,height=2)
lbl_15.grid(row=0,column=0)

nullLine3 = t.Label(f3,text="")
nullLine3.grid(row=1,column=0)

button_mine = ttk.Button(f3,text="Mine",command=mine)
button_mine.grid(row=2,column=0)

nullLine4 = t.Label(f3,text="")
nullLine4.grid(row=3,column=0)

button_chop = ttk.Button(f3,text="Chop")
button_chop.grid(row=4,column=0)

nullLine5 = t.Label(f3,text="")
nullLine5.grid(row=5,column=0)

button_craft = ttk.Button(f3,text="Craft")
button_craft.grid(row=6,column=0)

nullLine6 = t.Label(f3,text="")
nullLine6.grid(row=7,column=0)

button_smelt = ttk.Button(f3,text="Smelt")
button_smelt.grid(row=8,column=0)

nullLine7 = t.Label(f3,text="")
nullLine7.grid(row=9,column=0)

button_sleep = ttk.Button(f3,text="Sleep",command=sleep)
button_sleep.grid(row=10,column=0)

nullLine8 = t.Label(f3,text="")
nullLine8.grid(row=11,column=0)

button_save = ttk.Button(f3,text="Save")
button_save.grid(row=12,column=0)

#Frame 4
"""
for(int a=0;a<length.arr[];a++){
    arr[a]=text;
    }
"""
for x in range(10):
    arr.append(None)

tk_log = t.Label(f4,text="Log")
tk_log.pack(side="top")

tk_text1 = t.Label(f4,text=arr[0])
tk_text1.pack(side="top")

tk_text2 = t.Label(f4,text=arr[1])
tk_text2.pack(side="top")

tk_text3 = t.Label(f4,text=arr[2])
tk_text3.pack(side="top")

tk_text4= t.Label(f4,text=arr[3])
tk_text4.pack(side="top")

tk_text5 = t.Label(f4,text=arr[4])
tk_text5.pack(side="top")

tk_text6 = t.Label(f4,text=arr[5])
tk_text6.pack(side="top")

tk_text7 = t.Label(f4,text=arr[6])
tk_text7.pack(side="top")

tk_text8= t.Label(f4,text=arr[7])
tk_text8.pack(side="top")

tk_text9 = t.Label(f4,text=arr[8])
tk_text9.pack(side="top")

tk_text10 = t.Label(f4,text=arr[9])
tk_text10.pack(side="top")

tk_textAll = [tk_text1,tk_text2,tk_text3,tk_text4,tk_text5,tk_text6,tk_text7,tk_text8,tk_text9,tk_text10]
root.mainloop()
