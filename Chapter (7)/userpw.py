# _*_ coding:utf-8 _*_ 
import time
import sys
import Tkinter
import tkMessageBox
from PIL import Image, ImageTk


db = {}
timecheck = {}
file = open("data.dat", 'a+')
file.read()

def newuser():
    prompt = "login desired: "
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = "Name taken, try another: "
            continue
        else:
            break
    
    prompt = "Enter your password: "
    while True:
        pwd = raw_input(prompt)
        if len(pwd) < 6:
            print "Too short!"
        else:
            break
    db[name] = pwd
    print "Sign up success! Please sign in!"
    timecheck["time"] = ""
    timecheck["timeStr"] = ""


def olduser():
    while True:
        name = raw_input('login: ')
        pwd = raw_input('password: ')
        
        if len(name) == 0:
            print "Invalid name!"
        elif len(pwd)== 0:
            print  "Invalid password!"
        else:
            break

    passwd = db.get(name)
    
    if passwd == pwd:
        print "Welcome back, %s" % name
        try:
            last = timecheck.get("time")
            now = time.time()
            passtime = int(now - last)

            if passtime in range(1, 3600 * 4):
                print "You already logged in at: %s" % timecheck.get("timeStr")
        except:
            print "First time!"
        timecheck["time"] = time.time()
        timecheck["timeStr"] = time.asctime()

    else:
        print "Login incorrect. "
        

def management():
    prompt = """
    (1) Delete a user.
    (2) Show the user list.
    (3) Back main menu
    Enter your choice:"""
    while True:
        choice = raw_input(prompt)
        if choice == "1":
            name = raw_input("Enter user name: ")
            try:    
                del db[name]
                print "\nSuccess!"
            except:
                print "\nSomething wrong!"

        
        elif choice == "2":
            for eachkey in db.keys():
                    print "\nname:%s password:%s" % (eachkey,db[eachkey])
                
        elif choice == "3":
            showmenu()
            
        else:
            print "Invalid choice!"


def showmenu():
    prompt = """
    (S)ign up
    (L)ogin
    (M)anage
    (Q)uit
    Enter your choice: """
    
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = "q"
            print "\nYou picked: [%s]" % choice
            if choice not in "qslm":
                print "Invalid option, try again!"
            else: 
                chosen = True

            if choice == "q":
                print "GoodBye!"
                sys.exit()
            elif choice == "s":
                newuser()
            elif choice == "l":
                olduser()
            elif choice == "m":
                management()


root = Tkinter.Tk()
root.geometry('400x300+300+100')
root.title('QQ')

root.columnconfigure(0, pad=5)
root.columnconfigure(1, pad=5)
root.columnconfigure(2, pad=5)
root.columnconfigure(3, pad=5)
root.columnconfigure(4, pad=5)
root.columnconfigure(5, pad=5)
root.columnconfigure(6, pad=5)
root.columnconfigure(7, pad=5)
root.rowconfigure(0, pad=5)
root.rowconfigure(1, pad=5)
root.rowconfigure(2, pad=5)
root.rowconfigure(3, pad=5)
root.rowconfigure(4, pad=5)
root.rowconfigure(5, pad=5)
root.rowconfigure(6, pad=5)
root.rowconfigure(7, pad=5)

img = Image.open(r'C:\Users\Administrator\Desktop\qq.jpg')
qq = ImageTk.PhotoImage(img)
head = Tkinter.Label(root, image=qq)
head.image = qq
head.grid(rowspan=3, columnspan=5)

img = Image.open(r'C:\Users\Administrator\Desktop\qe.jpg')
e = ImageTk.PhotoImage(img)
head = Tkinter.Label(root, image=e)
head.image = e
head.grid(row=4, rowspan=2, columnspan=1)

name_entry = Tkinter.Entry(root)
name_entry.grid(row=4, column=0, columnspan=5, ipadx=15, ipady=3)
name_entry.focus_get()

lb1 = Tkinter.Label(root, text="注册帐号", fg="#33a0ff", width=6)
lb1.grid(row=4, column=2)

pwd_entry = Tkinter.Entry(root,show="•")
pwd_entry.grid(row=5, columnspan=5,  ipadx=15, ipady=3)

lb2 = Tkinter.Label(root, text="找回密码", fg="#33a0ff", width=6)
lb2.grid(row=5, column=2)

bt = Tkinter.Button(root, text="登 录", command=None, bg="#33a0ff", fg="white")
bt.grid(row=7, column=1, columnspan=1, ipadx=60, ipady=2, pady=5)


root.mainloop()
# if __name__ == "__main__":
#    showmenu()