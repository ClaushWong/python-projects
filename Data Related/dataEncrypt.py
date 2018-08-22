text = open("text.txt","a+")

name = raw_input("Username : ")
pwd = raw_input("Password : ")

idx = list(pwd)

#ENCRYPR
for x in range(len(idx)):
    #NUMERIC ENCRYPT ( if b % 2 == 0 , then c = 1 ; if b % 2 == 1 , then c = 2 )
    if idx[x] == "1":
        idx[x] = "a1b1c2"
    elif idx[x] == "2":
        idx[x] = "a2b2c1"
    elif idx[x] == "3":
        idx[x] = "a3b2c1"
    elif idx[x] == "4":
        idx[x] = "a4b1c2"
    elif idx[x] == "5":
        idx[x] = "a5b2c1"
    elif idx[x] == "6":
        idx[x] = "a6b1c2"
    elif idx[x] == "7":
        idx[x] = "a7b2c1"
    elif idx[x] == "8":
        idx[x] = "a8b1c2"
    elif idx[x] == "9":
        idx[x] = "a9b1c2"
    elif idx[x] == "0":
        idx[x] = "a0b1c2"
    #SMALL CAP CHAR ENCRYPT ( c = a + b ; if a + b > 10 ,then c = a + b - 10 + 1 )
    elif idx[x] == "a": #OK
        idx[x] = "a1b5c6"
    elif idx[x] == "b": #OK
        idx[x] = "a2b6c8"
    elif idx[x] == "c": #OK
        idx[x] = "a3b5c8"
    elif idx[x] == "d": #OK
        idx[x] = "a4b6c1"
    elif idx[x] == "e": #OK
        idx[x] = "a5b5c1"
    elif idx[x] == "f": #OK
        idx[x] = "a6b6c3"
    elif idx[x] == "g": #OK
        idx[x] = "a7b5c3"
    elif idx[x] == "h": #OK
        idx[x] = "a8b6c5"
    elif idx[x] == "i": #OK
        idx[x] = "a9b5c5"
    elif idx[x] == "j": #OK
        idx[x] = "a0b6c6"
    elif idx[x] == "k": #OK
        idx[x] = "a1b7c8"
    elif idx[x] == "l": #OK
        idx[x] = "a2b8c1"
    elif idx[x] == "m": #OK
        idx[x] = "a3b7c1"
    elif idx[x] == "n": #OK
        idx[x] = "a4b8c3"
    elif idx[x] == "o": #OK
        idx[x] = "a5b7c3"
    elif idx[x] == "p": #OK
        idx[x] = "a6b8c5"
    elif idx[x] == "q": #OK
        idx[x] = "a7b7c5"
    elif idx[x] == "r": #OK
        idx[x] = "a8b8c7"
    elif idx[x] == "s": #OK
        idx[x] = "a9b7c7"
    elif idx[x] == "t": #OK
        idx[x] = "a0b8c8"
    elif idx[x] == "u": #OK
        idx[x] = "a1b9c1"
    elif idx[x] == "v": #OK
        idx[x] = "a2b0c2"
    elif idx[x] == "w": #OK
        idx[x] = "a3b9c3"
    elif idx[x] == "x": #OK
        idx[x] = "a4b0c4"
    elif idx[x] == "y": #OK
        idx[x] = "a5b9c5"
    elif idx[x] == "z": #OK
        idx[x] = "a6b0c6"

    #BIG CAP CHAR ENCRYPT ( c = a * b ; if a * b > 9 , then c = biggest digit - smallest digit ; if a = b and a * b > 9 , then c = biggest digit - smallest digit - 1)
    #IF a == 3 && b == 7 , c = 2

    elif idx[x] == "A": #OK
        idx[x] = "a1b5c5"
    elif idx[x] == "B": #OK
        idx[x] = "a2b6c1"
    elif idx[x] == "C": #OK
        idx[x] = "a3b5c4"
    elif idx[x] == "D": #OK
        idx[x] = "a4b6c2"
    elif idx[x] == "E": #OK
        idx[x] = "a5b5c3"
    elif idx[x] == "F": #OK
        idx[x] = "a6b6c2"
    elif idx[x] == "G": #OK
        idx[x] = "a7b5c2"
    elif idx[x] == "H": #OK
        idx[x] = "a8b6c4"
    elif idx[x] == "I": #OK
        idx[x] = "a9b5c1"
    elif idx[x] == "J": #OK
        idx[x] = "a0b6c0"
    elif idx[x] == "K": #OK
        idx[x] = "a1b7c7"
    elif idx[x] == "L": #OK
        idx[x] = "a2b8c5"
    elif idx[x] == "M": #OK
        idx[x] = "a3b7c2"
    elif idx[x] == "N": #OK
        idx[x] = "a4b8c1"
    elif idx[x] == "O": #OK
        idx[x] = "a5b7c2"
    elif idx[x] == "P": #OK
        idx[x] = "a6b8c4"
    elif idx[x] == "Q": #OK
        idx[x] = "a7b7c4"
    elif idx[x] == "R": #OK
        idx[x] = "a8b8c1"
    elif idx[x] == "S": #OK
        idx[x] = "a9b7c3"
    elif idx[x] == "T": #OK
        idx[x] = "a0b8c0"
    elif idx[x] == "U": #OK
        idx[x] = "a1b9c9"
    elif idx[x] == "V": #OK
        idx[x] = "a2b0c0"
    elif idx[x] == "W": #OK
        idx[x] = "a3b9c5"
    elif idx[x] == "X": #OK
        idx[x] = "a4b0c0"
    elif idx[x] == "Y": #OK
        idx[x] = "a5b9c1"
    elif idx[x] == "Z": #OK
        idx[x] = "a6b0c0"
    else :
        pass

#SALT
l_pwd = []
for x in range(len(idx)):
    if x == 0 :
        l_pwd.append(idx[x])
    else :
        if x % 3 == 0:
            l_pwd.append("&"+idx[x])
        elif x == (len(idx) - 1):
            l_pwd.append(idx[x]+"&")
        else :
            l_pwd.append(idx[x])

#ENCRYPTED PASSWORD
r_pwd = "".join(idx)

text.write(name + ">" + pwd + ">" + r_pwd + "\n")
text.close()

raw_input("All Done. Thanks.")
