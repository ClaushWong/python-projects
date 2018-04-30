from Tkinter import *

root = Tk()
root.title("Crafting Recipes")

def PrevPage():
    if r12_23["text"] == "Page 2":
        #Row 4
        r4_1["text"] = "1"
        r4_1.grid(row=4,column=0,rowspan=1)
        r4_2["text"] = "Log"
        r4_2.grid(row=4,column=1,rowspan=1)
        r4_3["text"] = "Chop Wood"
        r4_3.grid(row=4,column=2,rowspan=1)
        r4_4["text"] = "---"
        r4_4.grid(row=4,column=3,rowspan=1)
        #Row 5
        r5_1["text"] = "2"
        r5_1.grid(row=5,column=0,rowspan=1)
        r5_2["text"] = "Pebble"
        r5_2.grid(row=5,column=1,rowspan=1)
        r5_3["text"] = "Mine Ore"
        r5_3.grid(row=5,column=2,rowspan=1)
        r5_4["text"] = "---"
        r5_4.grid(row=5,column=3,rowspan=1)
        #Row 6
        r6_1["text"] = "3"
        r6_1.grid(row=6,column=0,rowspan=1)
        r6_2["text"] = "Plank"
        r6_2.grid(row=6,column=1,rowspan=1)
        r6_3["text"] = "1 Log"
        r6_3.grid(row=6,column=2,rowspan=1)
        r6_4["text"] = "4"
        r6_4.grid(row=6,column=3,rowspan=1)
        #Row 7
        r7_1["text"] = "4"
        r7_1.grid(row=7,column=0,rowspan=1)
        r7_2["text"] = "Stick"
        r7_2.grid(row=7,column=1,rowspan=1)
        r7_3["text"] = "1 Planks"
        r7_3.grid(row=7,column=2,rowspan=1)
        r7_4["text"] = "2"
        r7_4.grid(row=7,column=3,rowspan=1)
        #Row 8
        r8_1["text"] = "5"
        r8_1.grid(row=8,column=0,rowspan=1)
        r8_2["text"] = "Cobblestone"
        r8_2.grid(row=8,column=1,rowspan=1)
        r8_3["text"] = "4 Pebbles"
        r8_3.grid(row=8,column=2,rowspan=1)
        r8_4["text"] = "1"
        r8_4.grid(row=8,column=3,rowspan=1)
        #Row 9
        r9_1["text"] = "6"
        r9_1.grid(row=9,column=0,rowspan=1)
        r9_2["text"] = "Iron Ore"
        r9_2.grid(row=9,column=1,rowspan=1)
        r9_3["text"] = "Mine Ore [U-1]"
        r9_3.grid(row=9,column=2,rowspan=1)
        r9_4["text"] = "---"
        r9_4.grid(row=9,column=3,rowspan=1)
        #Row 10
        r10_1["text"] = "7"
        r10_1.grid(row=10,column=0,rowspan=1)
        r10_2["text"] = "Gold Ore"
        r10_2.grid(row=10,column=1,rowspan=1)
        r10_3["text"] = "Mine Ore[U-1]"
        r10_3.grid(row=10,column=2,rowspan=1)
        r10_4["text"] = "---"
        r10_4.grid(row=10,column=3,rowspan=1)
        #Row 11
        r11_1["text"] = ""
        r11_1.grid(row=11,column=0,rowspan=1)
        r11_2["text"] = ""
        r11_2.grid(row=11,column=1,rowspan=1)
        r11_3["text"] = ""
        r11_3.grid(row=11,column=2,rowspan=1)
        r11_4["text"] = ""
        r11_4.grid(row=11,column=3,rowspan=1)
        #Row 12
        r12_23["text"] = "Page 1"
    elif r12_23["text"] == "Page 3":
        #Row 4
        r4_1["text"] = "8"
        r4_1.grid(row=4,column=0,rowspan=1)
        r4_2["text"] = "Iron Ingot"
        r4_2.grid(row=4,column=1,rowspan=1)
        r4_3["text"] = "1 Iron Ore[S]"
        r4_3.grid(row=4,column=2,rowspan=1)
        r4_4["text"] = "1"
        r4_4.grid(row=4,column=3,rowspan=1)
        #Row 5
        r5_1["text"] = "9"
        r5_1.grid(row=5,column=0,rowspan=1)
        r5_2["text"] = "Gold Ingot"
        r5_2.grid(row=5,column=1,rowspan=1)
        r5_3["text"] = "1 Gold Ore[S]"
        r5_3.grid(row=5,column=2,rowspan=1)
        r5_4["text"] = "1"
        r5_4.grid(row=5,column=3,rowspan=1)
        #Row 6
        r6_1["text"] = "10"
        r6_1.grid(row=6,column=0,rowspan=2)
        r6_2["text"] = "Furnance"
        r6_2.grid(row=6,column=1,rowspan=2)
        r6_3["text"] = "8 Cobblestone"
        r6_4["text"] = "Only 1"
        r6_4.grid(row=6,column=3,rowspan=2)
        #Row 7
        r7_1["text"] = ""
        r7_1.grid(row=7,column=0,rowspan=2)
        r7_2["text"] = ""
        r7_2.grid(row=7,column=1,rowspan=2)
        r7_3["text"] = "2 Log"
        r7_4["text"] = ""
        r7_4.grid(row=7,column=3,rowspan=2)
        #Row 8
        r8_1["text"] = "11"
        r8_1.grid(row=8,column=0,rowspan=2)
        r8_2["text"] = "Wooden Axe"
        r8_2.grid(row=8,column=1,rowspan=2)
        r8_3["text"] = "3 Planks"
        r8_4["text"] = "Only 1"
        r8_4.grid(row=8,column=3,rowspan=2)
        #Row 9
        r9_1["text"] = ""
        r9_1.grid(row=9,column=0,rowspan=2)
        r9_2["text"] = ""
        r9_2.grid(row=9,column=1,rowspan=2)
        r9_3["text"] = "2 Sticks"
        r9_4["text"] = ""
        r9_4.grid(row=9,column=3,rowspan=2)
        #Row 10
        r10_1["text"] = "12"
        r10_1.grid(row=10,column=0,rowspan=2)
        r10_2["text"] = "Wooden Pickaxe"
        r10_2.grid(row=10,column=1,rowspan=2)
        r10_3["text"] = "3 Log"
        r10_4["text"] = "Only 1"
        r10_4.grid(row=10,column=3,rowspan=2)
        #Row 11
        r11_1["text"] = ""
        r11_1.grid(row=11,column=0,rowspan=2)
        r11_2["text"] = ""
        r11_2.grid(row=11,column=1,rowspan=2)
        r11_3["text"] = "2 Sticks"
        r11_4["text"] = ""
        r11_4.grid(row=11,column=3,rowspan=2)
        #Row 12
        r12_23["text"] = "Page 2"

def NextPage():
    if r12_23["text"] == "Page 1":
        #Row 4
        r4_1["text"] = "8"
        r4_2["text"] = "Iron Ingot"
        r4_3["text"] = "1 Iron Ore[S]"
        r4_4["text"] = "1"
        #Row 5
        r5_1["text"] = "9"
        r5_2["text"] = "Gold Ingot"
        r5_3["text"] = "1 Gold Ore[S]"
        r5_4["text"] = "1"
        #Row 6
        r6_1["text"] = "10"
        r6_1.grid(row=6,column=0,rowspan=2)
        r6_2["text"] = "Furnance"
        r6_2.grid(row=6,column=1,rowspan=2)
        r6_3["text"] = "8 Cobblestone"
        r6_4["text"] = "Only 1"
        r6_4.grid(row=6,column=3,rowspan=2)
        #Row 7
        r7_1["text"] = ""
        r7_1.grid(row=7,column=0,rowspan=2)
        r7_2["text"] = ""
        r7_2.grid(row=7,column=1,rowspan=2)
        r7_3["text"] = "2 Log"
        r7_4["text"] = ""
        r7_4.grid(row=7,column=3,rowspan=2)
        #Row 8
        r8_1["text"] = "11"
        r8_1.grid(row=8,column=0,rowspan=2)
        r8_2["text"] = "Wooden Axe"
        r8_2.grid(row=8,column=1,rowspan=2)
        r8_3["text"] = "3 Planks"
        r8_4["text"] = "Only 1"
        r8_4.grid(row=8,column=3,rowspan=2)
        #Row 9
        r9_1["text"] = ""
        r9_1.grid(row=9,column=0,rowspan=2)
        r9_2["text"] = ""
        r9_2.grid(row=9,column=1,rowspan=2)
        r9_3["text"] = "2 Sticks"
        r9_4["text"] = ""
        r9_4.grid(row=9,column=3,rowspan=2)
        #Row 10
        r10_1["text"] = "12"
        r10_1.grid(row=10,column=0,rowspan=2)
        r10_2["text"] = "Wooden Pickaxe"
        r10_2.grid(row=10,column=1,rowspan=2)
        r10_3["text"] = "3 Log"
        r10_4["text"] = "Only 1"
        r10_4.grid(row=10,column=3,rowspan=2)
        #Row 11
        r11_1["text"] = ""
        r11_1.grid(row=11,column=0,rowspan=2)
        r11_2["text"] = ""
        r11_2.grid(row=11,column=1,rowspan=2)
        r11_3["text"] = "2 Sticks"
        r11_4["text"] = ""
        r11_4.grid(row=11,column=3,rowspan=2)
        #Row 12
        r12_23["text"] = "Page 2"
    elif r12_23["text"] == "Page 2":
        #Row 4
        r4_1["text"] = "13"
        r4_1.grid(row=4,column=0,rowspan=2)
        r4_2["text"] = "Stone Axe"
        r4_2.grid(row=4,column=1,rowspan=2)
        r4_3["text"] = "3 Cobblestone"
        r4_4["text"] = "Only 1"
        r4_4.grid(row=4,column=3,rowspan=2)
        #Row 5
        r5_1["text"] = ""
        r5_1.grid(row=5,column=0,rowspan=2)
        r5_2["text"] = ""
        r5_2.grid(row=5,column=1,rowspan=2)
        r5_3["text"] = "2 Sticks"
        r5_4["text"] = ""
        r5_4.grid(row=5,column=3,rowspan=2)
        #Row 6
        r6_1["text"] = "14"
        r6_1.grid(row=6,column=0,rowspan=2)
        r6_2["text"] = "Stone Pickaxe"
        r6_2.grid(row=6,column=1,rowspan=2)
        r6_3["text"] = "3 Cobblestone"
        r6_4["text"] = "Only 1"
        r6_4.grid(row=6,column=3,rowspan=2)
        #Row 7
        r7_1["text"] = ""
        r7_1.grid(row=7,column=0,rowspan=2)
        r7_2["text"] = ""
        r7_2.grid(row=7,column=1,rowspan=2)
        r7_3["text"] = "2 Sticks"
        r7_4["text"] = ""
        r7_4.grid(row=7,column=3,rowspan=2)
        #Row 8
        r8_1["text"] = ""
        r8_1.grid(row=8,column=0,rowspan=1)
        r8_2["text"] = ""
        r8_2.grid(row=8,column=1,rowspan=1)
        r8_3["text"] = ""
        r8_4["text"] = ""
        r8_4.grid(row=8,column=3,rowspan=1)
        #Row 9
        r9_1["text"] = ""
        r9_1.grid(row=9,column=0,rowspan=1)
        r9_2["text"] = ""
        r9_2.grid(row=9,column=1,rowspan=1)
        r9_3["text"] = ""
        r9_4["text"] = ""
        r9_4.grid(row=9,column=3,rowspan=1)
        #Row 10
        r10_1["text"] = ""
        r10_1.grid(row=10,column=0,rowspan=1)
        r10_2["text"] = ""
        r10_2.grid(row=10,column=1,rowspan=1)
        r10_3["text"] = ""
        r10_4["text"] = ""
        r10_4.grid(row=10,column=3,rowspan=1)
        #Row 11
        r11_1["text"] = ""
        r11_1.grid(row=11,column=0,rowspan=1)
        r11_2["text"] = ""
        r11_2.grid(row=11,column=1,rowspan=1)
        r11_3["text"] = ""
        r11_4["text"] = ""
        r11_4.grid(row=11,column=3,rowspan=1)
        #Row 12
        r12_23["text"] = "Page 3"
    

title = Label(root,text="Crafting Recipes")
title.grid(row=0,column=0,columnspan=4)

version = Label(root,text="Version : 0.0.1")
version.grid(row=1,column=0,columnspan=4)

nullLine = Label(root,text="[U-1] = Upgrade-1 , [S] = Smelting")
nullLine.grid(row=2,column=0,columnspan=4)

#Row 3
r3_1 = Label(root,text="Item ID")
r3_1.grid(row=3,column=0)

r3_2 = Label(root,text="Item Name")
r3_2.grid(row=3,column=1)

r3_3 = Label(root,text="Recipe")
r3_3.grid(row=3,column=2)

r3_4 = Label(root,text="Amount")
r3_4.grid(row=3,column=3)

#Row 4
r4_1 = Label(root,text="1")
r4_1.grid(row=4,column=0)

r4_2 = Label(root,text="Log")
r4_2.grid(row=4,column=1)

r4_3 = Label(root,text="---")
r4_3.grid(row=4,column=2)

r4_4 = Label(root,text="---")
r4_4.grid(row=4,column=3)

#Row 5
r5_1 = Label(root,text="2")
r5_1.grid(row=5,column=0)

r5_2 = Label(root,text="Pebble")
r5_2.grid(row=5,column=1)

r5_3 = Label(root,text="---")
r5_3.grid(row=5,column=2)

r5_4 = Label(root,text="---")
r5_4.grid(row=5,column=3)

#Row 6
r6_1 = Label(root,text="3")
r6_1.grid(row=6,column=0)

r6_2 = Label(root,text="Plank")
r6_2.grid(row=6,column=1)

r6_3 = Label(root,text="1 Log")
r6_3.grid(row=6,column=2)

r6_4 = Label(root,text="4")
r6_4.grid(row=6,column=3)

#Row 7
r7_1 = Label(root,text="4")
r7_1.grid(row=7,column=0)

r7_2 = Label(root,text="Stick")
r7_2.grid(row=7,column=1)

r7_3 = Label(root,text="1 Planks")
r7_3.grid(row=7,column=2)

r7_4 = Label(root,text="2")
r7_4.grid(row=7,column=3)

#Row 8
r8_1 = Label(root,text="5")
r8_1.grid(row=8,column=0)

r8_2 = Label(root,text="Cobblestone")
r8_2.grid(row=8,column=1)

r8_3 = Label(root,text="4 Pebbles")
r8_3.grid(row=8,column=2)

r8_4 = Label(root,text="1")
r8_4.grid(row=8,column=3)

#Row 9
r9_1 = Label(root,text="6")
r9_1.grid(row=9,column=0)

r9_2 = Label(root,text="Iron Ore")
r9_2.grid(row=9,column=1)

r9_3 = Label(root,text="---")
r9_3.grid(row=9,column=2)

r9_4 = Label(root,text="---")
r9_4.grid(row=9,column=3)

#Row 10
r10_1 = Label(root,text="7")
r10_1.grid(row=10,column=0)

r10_2 = Label(root,text="Gold Ore")
r10_2.grid(row=10,column=1)

r10_3 = Label(root,text="---")
r10_3.grid(row=10,column=2)

r10_4 = Label(root,text="---")
r10_4.grid(row=10,column=3)

#Row 11
r11_1 = Label(root,text="")
r11_1.grid(row=11,column=0)

r11_2 = Label(root,text="")
r11_2.grid(row=11,column=1)

r11_3 = Label(root,text="")
r11_3.grid(row=11,column=2)

r11_4 = Label(root,text="")
r11_4.grid(row=11,column=3)

#Row 12
r12_1 = Button(root,text="<",command=PrevPage)
r12_1.grid(row=12,column=0)

r12_23 = Label(root,text="Page 1")
r12_23.grid(row=12,column=1,columnspan=2)

r12_4 = Button(root,text=">",command=NextPage)
r12_4.grid(row=12,column=3)

root.mainloop()