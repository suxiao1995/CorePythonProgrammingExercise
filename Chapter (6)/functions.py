# _*_ coding:utf-8 _*_ 

# Chapter 6
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
                    

# 6-3
def seq():
    nums = raw_input("Enter some numbers,apart with space.-->")
    nums = nums.split()
    index = []
    
    for num in nums:
        index.append(int(num))
    
    result = sorted(index,reverse=True)
    return result

# 字典序？
def seq2():
    pass
    
    
# 6-4
def rank():
    points = [33,99,65,77,85,46,66]
    sum = 0
    # calculate sum
    for i in points:
        sum += int(i)
    # division
    average_point = sum / len(points)
    
    if average_point in range(90,101):
        return "A"
    elif average_point in range(80,90):
        return "B"
    elif average_point in range(70,80):
        return "C"
    elif average_point in range(60,70):
        return "D"
    elif average_point < 60:
        return "F"
    print sum,average_point

 
# 6-5

        

# 6-9
def tran_time():
    time = int(raw_input("Enter the minutes:"))
    hours,minutes = divmod(time,60)     
    return "%d hours %d minutes." % (hours,minutes)
    
# 6-10
def tran_string(): 
    string = raw_input("Enter some string:")
    return string.swapcase()
    
    
# 6-11
def tran_ip():
    numbers = raw_input("Enter a id number:")
    n = 3
    # split the numbers with 3 length.
    address = [numbers[i:i+n] for i in xrange(0,len(numbers),n)]
    ip = ".".join(address)
    
    return ip
    
    
# 6-12
def findchr(string,char):
    
# 6-15

    
    