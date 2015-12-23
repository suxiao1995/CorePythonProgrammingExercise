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
    num_list = [int(x) for x in nums.split()]
    
    num_list.sort(reverse=True)
    return num_list

# Lexicographical
def seq2():
    nums = raw_input("Enter some numbers,apart with space.-->")
    num_list = nums.split()
    
    num_list.sort(reverse=True) # equal to new_list = sorted(num_list,reverse=True)
    return num_list
    
    
# 6-4
def rank_grade(mark_list):

    def rank(mark):
       
        if mark in range(90,101):
            return "A"
        elif mark in range(80,90):
            return "B"
        elif mark in range(70,80):
            return "C"
        elif mark in range(60,70):
            return "D"
        elif mark < 60:
            return "F"

    average = sum(mark_list) / float(len(mark_list))
    rank_list = [rank(mark) for mark in mark_list]
    return average,rank_list

    
# 6-5

  
# 6-6
def myStrip(string):
    # use while to clear all the space at the beginning or in the end a string.
    while string[0] == " ":    
        string = string[1:]
        
    while string[-1] == " ":
        string = string[:-1]
        
    return string
    

# 6-9
def tran_time():
    time = int(raw_input("Enter the minutes: "))
    hours,minutes = divmod(time,60)     
    return "%d hours %d minutes. " % (hours,minutes)
    
# 6-10
def tran_string(): 
    string = raw_input("Enter some string: ")
    return string.swapcase()
    
    
# 6-11
def tran_ip():
    numbers = raw_input("Enter a id number: ")
    n = 3
    # split the numbers with 3 length.
    address = [numbers[i:i+n] for i in xrange(0,len(numbers),n)]
    ip = ".".join(address)
    
    return ip
    
    
# 6-12
def findchr(string,char):
    if char in string:
        i = 0
        while i < len(string):
            if string[i] == char:
                return i
            i += 1
    else:
        return -1
        
        
def rfindchr(string,char):   
    if char in string:
        i = -1
        while i < len(string):
            if string[i] == char:
                return i
            i -= 1
    else:
        return -1

def subchr(string,origchar,newchar):
    if origchar in string:
        return string.replace(origchar,newchar)
    else:
        return -1
        
        
# 6-13


# 6-17
def myPop(list):
    leave = list[-1]
    del list[-1]
    return leave

