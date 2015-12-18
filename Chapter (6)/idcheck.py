# _*_ coding:utf-8 _*_ 
import string

from keyword import *


# 6-2
def idcheck():
    alphas = string.letters + '_'
    nums = string.digits

    print "Welcome to the Identifier Checker v2.0."
    print "Testees must be at least 1 chars long."
    myInput = raw_input("Identifier to check?")
    
    if len(myInput) > 0:
        
        if myInput[0] not in alphas:
            print "Invalid:first symbol must be alphabetic!"
        
        # check if the identifier in the keyword list-->(kwlist)
        elif myInput in kwlist:
            print "Invalid:Identifier shouldn't be keyword!"
            
        else:
        
            for otherChar in myInput[1:]:
            
                if otherChar not in alphas + nums:
                    print "Invalid:remaining symbols must be alphanumeric"
                    break
                
            else:
                print "okay as an identifier!"
                    
if __name__ == "__main__":
    idcheck()