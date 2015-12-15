'Make a file and get the input from user or read a file.'
import os 
ls = os.linesep

#choose function
choice = int(raw_input("1.Read a file \n2.Make a file \n3.modify a file-->"))
if choice == 2:
    #get filename

    fname = raw_input("Enter a filename:")
        #print "ERROR: '%s' alredy exists" % fname
       
    
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"

    #get the content.
    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            all.append(entry)

    #write the content
    fobj = open(fname,'w')
    fobj.writelines(['%s%s' %(x,ls) for x in all])
    fobj.close()

    print"Done"

elif choice == 1:
    #get filename
    fname = raw_input('Enter filename:')
    print 
    
    #attempt to open a file for reading.
    try:
        fobj = open(fname,'r')
    except IOError,e:
        print "***file open error:",e
    else:
        #display the content of the file
        for line in fobj.readlines():
            line = line.strip()
            print line
        fobj.close()
        print"Done"


elif choice == 3:
    #get filename

    fname = raw_input("Enter a filename:")
        #print "ERROR: '%s' alredy exists" % fname
       
    
    
    print "Want to clear the file content?(Y/N)"
    choose = raw_input("-->")
    if choose == "Y":
        f = open(fname,'w')
        f.truncate()
        f.close()
    else:
        pass
        
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"    
    #get the content.
    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            all.append(entry)

    #write the content
    fobj = open(fname,'a')
    fobj.writelines(['%s%s' %(x,ls) for x in all])
    fobj.close()

    print"Done"

# import os
# "makeAndReadTextFile.py--create text file"



# choice = int(raw_input("1.Read a file \n2.Make a file \n-->"))
# if choice == 1:
    # filename = raw_input("Enter a filename:")
    # f = open(filename,'r')

    # for line in f.readlines():
        # print line
            
    # f.close()


# elif choice == 2:
    # filename = raw_input("Enter a filename:")
    # f = open(filename,'w')

    # running = True
    # while running:
        # content = raw_input("Enter a line:")
        # f.write(content + "\n")
        # choice = raw_input("Press 'Enter' to continue,input 'q' to quit.")
        # if choice == "":
            # pass
        # else:
            # running = False
            
    # f.close()
