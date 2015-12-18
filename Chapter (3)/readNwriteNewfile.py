# _*_ coding:utf-8 _*_ 
# Chapter 3
import os 
import sys
ls = os.linesep

def make_read_changeFile():

    """Make a file and get the input from user or read a file."""
    while True:
        # choose function
        choice = int(raw_input("1.Make a file\n 2.Read a file\n3.modify a file\n 4.quit\n -->"))
        if choice == 1:
            # get filename

            fname = raw_input("Enter a filename:")
            # print "ERROR: '%s' alredy exists" % fname
            if os.path.exists(fname):
                print "ERROR: '%s' already exists." % fname
            else:
                break
                
            # get the content.
            all = []
            print "\nEnter lines ('.' by itself to quit).\n"

            # loop until user terminates input
            while True:
                entry = raw_input('>')
                if entry == '.':
                    break
                else:
                    all.append(entry)

            # write the content
            fobj = open(fname,'w')
            fobj.writelines(['%s%s' %(x,ls) for x in all])
            fobj.close()

            print"Done"

        elif choice == 2:
            # get filename
            fname = raw_input('Enter filename:')
            print 
            
            # attempt to open a file for reading.
            try:
                fobj = open(fname,'r')
            except IOError,e:
                print "***file open error:",e
                
            # if not os.path.exists(fname):
                # print "ERROR,no such file."
                # break
                
            else:
                # display the content of the file
                for line in fobj.readlines():
                    line = line.strip() #clear the space in a line
                    print line
                fobj.close()
                print"Done"


        elif choice == 3:
            # get filename
            fname = raw_input("Enter a filename:")
            # print "ERROR: '%s' doesn't exists" % fname
            if not os.path.exists(fname):
                print "ERROR: '%s' doesn't exists." % fname
                break
            
            print "Want to clear the file content?(Y/N)"
            choose = raw_input("-->")
            if choose == "Y":
                f = open(fname,'w')
                f.truncate() # clear the content of file
                f.close()
            else:
                pass
                
            all = []
            print "\nEnter lines ('.' by itself to quit).\n"    
            # get the content.
            while True:
                entry = raw_input('>')
                if entry == '.':
                    break
                else:
                    all.append(entry)

            # write the content
            fobj = open(fname,'a')
            fobj.writelines(['%s%s' %(x,ls) for x in all])
            fobj.close()

            print"Done"
        
        else:
            sys.exit()
make_read_changeFile()