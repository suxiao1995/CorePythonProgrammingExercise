# 3-11 
 
 #!/usr/bin/env python
 
import os
ls = os.linesep
fname = raw_input()
fobj = open(fname,'r')
for i in fobj:
  print i.sprit(ls)
fobj.close()

# 3-12
#!/usr/bin/env python
#coding=utf-8

import os

ls = os.linesep

while True:
    choice = raw_input('''
    1、write
    2、read
    ''')
    if choice == '1':
        all = []
        while True:
            fname = raw_input("enter filename\n")
            if not os.path.exists(fname):
                fobj = open(fname, 'w')
                while True:
                    line = raw_input()
                    if line == '.':
                        break
                    else:
                        all.append(line)
                break
            else:
                print 'already exist!'
    elif choice == '2':
        while True:
            fname = raw_input("enter filename\n")
            if os.path.exists(fname):
                fobj = open(fname, 'r')
                for i in fobj:
                    print i.strip(ls)
                fobj.close()
                break
            else:
                print 'no file'
    else:
        print 'wrong choice'
