num = ["0","1","2","3","4","5","6","7","8","9"]
char1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
char2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
prime = [2,3,5,7]
idx = {}

file_open = open("password.txt","a+")

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

name = raw_input("Username : ")
pwd = raw_input("Password : ")

n = list(pwd)
o = []

for x in n:
    if x in idx:
       o.append(idx[x])

pwd = "".join(o)
file_open.write(name + "|"+ pwd + "\n")
file_open.close()
