num = ["0","1","2","3","4","5","6","7","8","9"]
char1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
char2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sym1 = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+"]
sym2 = ["[","{","]","}","\\","|",";",":","'",'"',",","<",".",">","/","?"]
prime = [2,3,5,7]
idx = {}

#NUMERIC
for x in num:
    if int(x) in prime:
        y = "2"
    else :
        y = "1"
    
    if y == "1":
        z = "2"
    else :
        z = "1"
    
    idx[x] = "a" + x + "b" + y + "c" + z

#SMALL CAPS
for x in range(len(char1)):
    if x % 2 == 1:
        y1 = "6"
        y2 = "8"
        y3 = "0"
    else :
        y1 = "5"
        y2 = "7"
        y3 = "9"

    if x < 10:
        x1 = x + 1
        if x1 == 10 :
            x1 = 0
        z1 = x1 + int(y1)
        if z1 >= 10:
           z1 -= 9
        idx[char1[x]] = "a" + str(x1) + "b" + y1  + "c" + str(z1)
 
    elif x > 9 and x < 20:
        x1 = x - 9
        if x1 == 10 :
            x1 = 0
        z1 = x1 + int(y2)
        if z1 >= 10:
            if z1 >= 20:
                z1 -= 19
            else :
                z1 -= 9
        idx[char1[x]] = "a" + str(x1) + "b" + y2  + "c" + str(z1)

    else :
        x1 = x - 19
        if x1 == 10 :
            x1 = 0
        z1 = x1 + int(y3)
        if z1 >= 10:
            if z1 >= 20:
                if z1 >= 30:
                    z1 -= 29
                else :
                    z1 -= 19
            else :
                z1 -= 9
        idx[char1[x]] = "a" + str(x1) + "b" + y3  + "c" + str(z1)

#BIG CAPS
for x in range(len(char2)):
    if x % 2 == 1:
        y1 = "6"
        y2 = "8"
        y3 = "0"
    else :
        y1 = "5"
        y2 = "7"
        y3 = "9"

    if x < 10:
        x1 = x + 1
        if x1 == 10 :
            x1 = 0
        z1 = x1 * int(y1)
        if z1 > 9:
           z1 = str(z1)
           m = list(z1)
           m[0] = int(m[0])
           m[1] = int(m[1])
           m.sort()
           z1 = m[1] - m[0]
        idx[char2[x]] = "a" + str(x1) + "b" + y1  + "c" + str(z1)
 
    elif x > 9 and x < 20:
        x1 = x - 9
        if x1 == 10 :
            x1 = 0
        z1 = x1 * int(y2)
        if z1 > 9:
           z1 = str(z1)
           m = list(z1)
           m[0] = int(m[0])
           m[1] = int(m[1])
           m.sort()
           z1 = m[1] - m[0]
        if x1 == 3 and y2 == "7":
            z1 = 2
        idx[char2[x]] = "a" + str(x1) + "b" + y2  + "c" + str(z1)

    else :
        x1 = x - 19
        if x1 == 10 :
            x1 = 0
        z1 = x1 * int(y3)
        if z1 > 9:
           z1 = str(z1)
           m = list(z1)
           m[0] = int(m[0])
           m[1] = int(m[1])
           m.sort()
           z1 = m[1] - m[0]
        idx[char2[x]] = "a" + str(x1) + "b" + y3  + "c" + str(z1)

#SYMBOL CAT 1
for x in range(len(sym1)):
    y = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
    z = ["f","e","d","c","b","a",9,8,7,6,5,4,3,2,1,0]
    if x < 10:
        x1 = x
        if x1 == 10:
            x = 0
    elif x > 9 and x < 20:
        x1 = x - 9
        if x1 == 10 :
            x1 = 0
    else :
        x1 = x - 19
        if x1 == 10 :
            x1 = 0
    idx[sym1[x]] = "d" + str(x1) + "e" + str(y[x]) + "f" + str(z[x])

#SYMBOL CAT 2
for x in range(len(sym2)):
    y = [5,"b","f",9,"a",3,"e",1,4,"d",0,"c",2,6,8,7]
    z = [8,7,"c",1,9,5,"a","d",6,"f","e",0,2,"b",3,4]
    if x < 10:
        x1 = x
        if x1 == 10:
            x = 0
    elif x > 9 and x < 20:
        x1 = x - 9
        if x1 == 10 :
            x1 = 0
    else :
        x1 = x - 19
        if x1 == 10 :
            x1 = 0
    idx[sym2[x]] = "d" + str(x1) + "e" + str(y[x]) + "f" + str(z[x])

idx[" "] = "daefff"

requestFile = raw_input("Please type in the file name. (Without .txt)\n")
requestFile = requestFile + ".txt"
file_open = open(requestFile,"r")
data = file_open.readlines()
file_open.close()

newdata = []

for x in range(len(data)):
    n = list(data[x])
    try :
        delChar = n.index("\n")
    except :
        pass
    else :
        del(n[delChar])
        n = "".join(n)

    o = []

    for y in n:
        o.append(idx[y])

    p = "".join(o)
    
    newdata.append(p)

resultFile = "encrypt_" + requestFile
newfile = open(resultFile,"a+")
for x in newdata:
    newfile.write(x + "\n")
newfile.close()
raw_input("Done")

