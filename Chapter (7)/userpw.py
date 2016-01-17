# _*_ coding:utf-8 _*_ 

db = {}

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
        if name or pwd == " ":
            print "Invalid name or password."
        else:
            break
            
    passwd = db.get(name)
    
    if passwd == pwd:
        print "Welcome back, %s" % name
    else:
        print "Login incorrect. "
    
def showmenu():
    prompt = """
    (S)ign up
    (L)ogin
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
            if choice not in "qsl":
                print "Invalid option, try again!"
            else: 
                chosen = True
            
            if choice == "q":
                done = True
            elif choice == "s":
                newuser()
            elif choice == "l":
                olduser()
    
if __name__ == "__main__":
    showmenu()