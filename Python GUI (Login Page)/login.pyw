from Tkinter import *
import tkMessageBox
import os

fileRead = open("form.txt","r")
fileData = fileRead.readlines()
fileRead.close()

np = [] #Not processed data
username = [] #Username (processed)
password = [] #Password (processed)

for x in range(len(fileData)):
    np.append(fileData[x])

for x in range(len(np)):
    n = np[x].split(" ")
    username.append(n[0])

    m = list(n[1])
    try :
        deleteChar = m.index("\n")
    except :
        pass
    else :
        del(m[deleteChar])
        
    m = "".join(m)
    password.append(m)

var = 1

root = Tk()
root.title("Login Page")

def chg():
    global var
    if var % 2 == 1:
        entry2["show"] = ""
    if var % 2 == 0:
        entry2["show"] = "*"
    var += 1
    print var

def login():
    usrN = entry1.get()
    pwd = entry2.get()

    try :
        n = username.index(usrN)
    except :
        tkMessageBox.showerror("Login Unsuccessfully","This username isn't exist.")
    else :
        if password[n] == pwd:
            tkMessageBox.showinfo("Login Success","Successfully login.")
        else :
            tkMessageBox.showerror("Login Unsuccessfully","Your password or username is wrong.")

def register():
    os.system("start register.pyw")

lgn_title = Label(root,text="Login Page")
lgn_title.grid(columnspan=2)

reg_login = Label(root,text="Username")
reg_pwd = Label(root,text="Password")

entry1 = Entry(root)
entry2 = Entry(root,show="*")

check = Checkbutton(root,text="Show Password",command=chg)

reg_login.grid(row=1,sticky="W")
entry1.grid(row=1,column=1)

reg_pwd.grid(row=2,sticky="W")
entry2.grid(row=2,column=1)

check.grid(row=3,columnspan=2)

loginButton = Button(root,text="Login",command=login)
loginButton.grid(row=4,columnspan=2)

lbl_1 = Label(root,text="Don't have any account yet.")
lbl_1.grid(row=5,columnspan=2)

lbl_2 = Label(root,text="Click the button below.")
lbl_2.grid(row=6,columnspan=2)

reg_button = Button(root,text="Register",command=register)
reg_button.grid(row=7,columnspan=2)

root.mainloop()