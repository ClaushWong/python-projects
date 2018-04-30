from Tkinter import *
import tkMessageBox

root = Tk()
root.title("Registeration Page")

var = 1

def submit():
    name = entry1.get()
    pwd = entry2.get()
    c_pwd = entry3.get()

    if pwd == c_pwd:
        form = open("form.txt","a+")
        form.write(name+" "+pwd+"\n")
        form.close()
        tkMessageBox.showinfo("Register Successfully","You successfully create an account.")
        root.destroy()
    else :
        tkMessageBox.showerror("Error", "Your Password did not match. Try again.")
    
def cancel():
    root.destroy()

def chg():
    global var
    if var % 2 == 1:
        entry2["show"] = ""
        entry3["show"] = ""
    if var % 2 == 0:
        entry2["show"] = "*"
        entry3["show"] = "*"
    var += 1
    print var

reg_title = Label(root,text="User Registeration")
reg_title.grid(columnspan=2)

reg_login = Label(root,text="Username")
reg_pwd = Label(root,text="Password")
reg_confirmPWD = Label(root,text="Confirm Password")

entry1 = Entry(root)
entry2 = Entry(root,show="*")
entry3 = Entry(root,show="*")

check = Checkbutton(root,text="Show Password",command=chg)

reg_login.grid(row=1,sticky="W")
entry1.grid(row=1,column=1)

reg_pwd.grid(row=2,sticky="W")
entry2.grid(row=2,column=1)

reg_confirmPWD.grid(row=3,sticky="W")
entry3.grid(row=3,column=1)

check.grid(row=4,columnspan=2)

submitButton = Button(root,text="Submit",command=submit)
submitButton.grid(row=5,columnspan=2)

cancelButton = Button(root,text="Cancel",command=cancel)
cancelButton.grid(row=6,columnspan=2)

root.mainloop()