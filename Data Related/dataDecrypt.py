text = open("FB.txt","r")
info = text.readlines()
text.close()

for x in range(len(info)):
    bn = list(info[x])
    delChar = bn.index("\n")
    del(bn[delChar])

    bn = "".join(bn)
    splitInfo = bn.split(">")

    x = 0
    y = 6
    r_pwd = []

    while y != len(splitInfo[2]) + 6 :
        ec = splitInfo[2][x:y]
        #NUMERIC DECRYPT
        if ec == "a1b1c2":
            r_pwd.append("1")
        elif ec == "a2b2c1":
            r_pwd.append("2")
        elif ec == "a3b2c1":
            r_pwd.append("3")
        elif ec == "a4b1c2":
            r_pwd.append("4")
        elif ec == "a5b2c1":
            r_pwd.append("5")
        elif ec == "a6b1c2":
            r_pwd.append("6")
        elif ec == "a7b2c1":
            r_pwd.append("7")
        elif ec == "a8b1c2":
            r_pwd.append("8")
        elif ec == "a9b1c2":
            r_pwd.append("9")
        elif ec == "a0b1c2":
            r_pwd.append("0")

        #SMALL CAP CHAR DECRYPT
        elif ec == "a1b5c6":
            r_pwd.append("a")
        elif ec == "a2b6c8":
            r_pwd.append("b")
        elif ec == "a3b5c8":
            r_pwd.append("c")
        elif ec == "a4b6c1":
            r_pwd.append("d")
        elif ec == "a5b5c1":
            r_pwd.append("e")
        elif ec == "a6b6c3":
            r_pwd.append("f")
        elif ec == "a7b5c3":
            r_pwd.append("g")
        elif ec == "a8b6c5":
            r_pwd.append("h")
        elif ec == "a9b5c5":
            r_pwd.append("i")
        elif ec == "a0b6c6":
            r_pwd.append("j")
        elif ec == "a1b7c8":
            r_pwd.append("k")
        elif ec == "a2b8c1":
            r_pwd.append("l")
        elif ec == "a3b7c1":
            r_pwd.append("m")
        elif ec == "a4b8c3":
            r_pwd.append("n")
        elif ec == "a5b7c3":
            r_pwd.append("o")
        elif ec == "a6b8c5":
            r_pwd.append("p")
        elif ec == "a7b7c5":
            r_pwd.append("q")
        elif ec == "a8b8c7":
            r_pwd.append("r")
        elif ec == "a9b7c7":
            r_pwd.append("s")
        elif ec == "a0b8c8":
            r_pwd.append("t")
        elif ec == "a1b9c1":
            r_pwd.append("u")
        elif ec == "a2b0c2":
            r_pwd.append("v")
        elif ec == "a3b9c3":
            r_pwd.append("w")
        elif ec == "a4b0c4":
            r_pwd.append("x")
        elif ec == "a5b9c5":
            r_pwd.append("y")
        elif ec == "a6b0c6":
            r_pwd.append("z")

        #BIG CAP CHAR DECRYPT
        elif ec == "a1b5c5":
            r_pwd.append("A")
        elif ec == "a2b6c1":
            r_pwd.append("B")
        elif ec == "a3b5c4":
            r_pwd.append("C")
        elif ec == "a4b6c2":
            r_pwd.append("D")
        elif ec == "a5b5c3":
            r_pwd.append("E")
        elif ec == "a6b6c2":
            r_pwd.append("F")
        elif ec == "a7b5c2":
            r_pwd.append("G")
        elif ec == "a8b6c4":
            r_pwd.append("H")
        elif ec == "a9b5c1":
            r_pwd.append("I")
        elif ec == "a0b6c0":
            r_pwd.append("J")
        elif ec == "a1b7c7":
            r_pwd.append("K")
        elif ec == "a2b8c5":
            r_pwd.append("L")
        elif ec == "a3b7c2":
            r_pwd.append("M")
        elif ec == "a4b8c1":
            r_pwd.append("N")
        elif ec == "a5b7c2":
            r_pwd.append("O")
        elif ec == "a6b8c4":
            r_pwd.append("P")
        elif ec == "a7b7c4":
            r_pwd.append("Q")
        elif ec == "a8b8c1":
            r_pwd.append("R")
        elif ec == "a9b7c3":
            r_pwd.append("S")
        elif ec == "a0b8c0":
            r_pwd.append("T")
        elif ec == "a1b9c9":
            r_pwd.append("U")
        elif ec == "a2b0c0":
            r_pwd.append("V")
        elif ec == "a3b9c5":
            r_pwd.append("W")
        elif ec == "a4b0c0":
            r_pwd.append("X")
        elif ec == "a5b9c1":
            r_pwd.append("Y")
        elif ec == "a6b0c0":
            r_pwd.append("Z")
        else :
            pass
        x += 6
        y += 6

    r_pwd = "".join(r_pwd)
    print splitInfo[0] + ":" + r_pwd

raw_input("")
