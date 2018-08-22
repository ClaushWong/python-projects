def fac(num):
    x = num
    num -= 1

    if num > 1 :
        while num != 1:
            x *= num
            num -= 1
    else :
        pass

    val.append(x)

#Permutation with repetition (pWr)
def pWr(n,r):
    answer = n ** r
    print "Permutation with repetition"
    print str(n)+"P"+str(r)+" =", answer 


#Permutation without repetition (pwr)
# Formular = n! / (n-r)!

def pwr(n,r):
    fac(n)
    d = n - r
    if d != 0:
        fac(d)
    else :
        d = 1
        fac(d)
    
    answer = val[0] / val[1]
    print "Permutation without repetition"
    print str(n)+"P"+str(r)+" =", answer


#Combination with repetition (cWr)
#Formular = (r+n-1)! / r!(n-1)!
def cWr(n,r):
    # u! = val[0]
    u = r + n - 1
    fac(u)

    #r! = val[1]
    fac(r)

    #(n-1)! = val[2]
    fac(n-1)

    d = val[1] * val[2]

    answer = val[0] / d
    print "Combination with repetition"
    print str(n)+"C"+str(r)+" =", answer

#Combination without repetition (cwr)
#Formular = n! / r!(n-r)!
def cwr(n,r):
    # n! = val[0]
    fac(n)

    # r! = val[1]
    fac(r)

    # (n-r)! = val[2]
    d = n - r
    if d != 0:
        fac(d)
    else :
        d = 1
        fac(d)

    answer = val[0] / ( val[1] * val[2] )
    print "Combination without repetition"
    print str(n)+"C"+str(r)+" =", answer

#Opening
val = []
print "What operator you want to use?\n1. Permutation With Repetition\n2. Permutation Without Repetition\n3. Combination With Repetition\n4. Combination Without Repetition\n5. Quit"
oper = raw_input("Operator : ")

while oper != "5":
    x = raw_input("n = ")
    y = raw_input("r = ")
    if oper == "1":
        try :
            x = int(x)
        except :
            print "Your n isn't an integer. Try again."
        else :
            pass
        
        try :
            y = int(y)
        except :
            print "Your r isn't an integer. Try again."
        else :
            pass

        pWr(x,y)

    elif oper == "2":
        try :
            x = int(x)
        except :
            print "Your n isn't an integer. Try again."
        else :
            pass
        
        try :
            y = int(y)
        except :
            print "Your r isn't an integer. Try again."
        else :
            pass

        pwr(x,y)

    elif oper == "3":
        try :
            x = int(x)
        except :
            print "Your n isn't an integer. Try again."
        else :
            pass
        
        try :
            y = int(y)
        except :
            print "Your r isn't an integer. Try again."
        else :
            pass

        cWr(x,y)

    elif oper == "4":
        try :
            x = int(x)
        except :
            print "Your n isn't an integer. Try again."
        else :
            pass
        
        try :
            y = int(y)
        except :
            print "Your r isn't an integer. Try again."
        else :
            pass

        cwr(x,y)

    else :
        print "You're not following the request. Try again."

    print 40*"="
    val = []
    print "What operator you want to use?\n1. Permutation With Repetition\n2. Permutation Without Repetition\n3. Combination With Repetition\n4. Combination Without Repetition\n5. Quit"
    oper = raw_input("Operator : ")

else :
    raw_input("Thanks for using us. Have a nice day.\n")
