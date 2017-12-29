# 3-11 
 
 #!/usr/bin/env python
 
import os
ls = os.linesep
fname = raw_input()
fobj = open(fname,'r')
for i in fobj:
  print i.sprit(ls)
fobj.close()
