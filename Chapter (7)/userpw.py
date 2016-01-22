# _*_ coding:utf-8 _*_ 
import time
import os
db = {}
timecheck = {}


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
            except:
                print "\nSomething wrong!"
            print "\nSuccess!"
        
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
                done = True
            elif choice == "s":
                newuser()
            elif choice == "l":
                olduser()
            elif choice == "m":
                management()
    
if __name__ == "__main__":
    showmenu()