# _*_ coding:utf-8 _*_ 

# Chapter 6

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

    
# 6-5(a)
def print_str():
    from time import sleep
    string = raw_input("Enter a string:")
    i = 0
    length = len(string)
    
    if length % 2 == 0:
        s_center = length / 2
    else:
        s_center = (length / 2) + 1
    
    s_back = string[s_center:]
    s_fore = string[:s_center]
    
    i = 0
    while i < (s_center + 1):
        # %20s%s%-20s: the number between '%' and 's' means to fill up 20 spaces.
        print "%20s%s%-20s" % (string[s_center - i:s_center],string[s_center],
                            string[s_center + 1:s_center + i])
        i += 1                           
        sleep(1)


# 6-5(b)
def comStrings():
    str1 = str1.lower()
    str2 = str2.lower()
   
    j = 0
    for i in str1:
        if i == str2[j]:
            pass
        else:
            return "Wrong!"
        j += 1
        
    return "The same!"

# 6-5(c)
def is_palindrome(str):
    import string
    s_list = [char.lower() for char in str if char in string.ascii_lowercase]
    
    if len(s_list) <= 1:
        return True
    else:
        return s_list[0] == s_list[-1] and is_palindrome(s_list[1:-1])  # recursion
        
# 6-5(d)    
def to_palindrome(str):
    
    return str + str[::-1] # Reverse stepping sliced
    
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
# by soulforever
def atoc(c_str):
    # judge pure real number
    if 'j' not in c_str:
        return complex(float(c_str), 0)
        
    index = 0
    for i, c in enumerate(c_str):
        if c in ('+', '-') and i != 0 and c_str[i-1] not in ('e', 'E'):
                index = i
                break
    # judge pure imaginary number
    if index == 0:
        real = 0 
    else:
        real = float(c_str[:index])
        
    imag = float(c_str[index:-1])
    return complex(real, imag)

    
# 6-17
def myPop(list):
    leave = list[-1]
    del list[-1]
    return leave

    
# 6-16


# 6-19
def multi_print(data):
    
    lines = int(raw_input('Lines:'))
    index = raw_input("col/row:")
    length = len(data)
    line_length = int(round(float(length) / float(lines)))
    
    s_list = []
    if index == "col":
        for i in range(0,lines):
            s_list.append(data[i])
            j = lines
            while j < len(data):
                s_list.append(data[i+j])
                j += lines
    else:
        s_list = data

    i = 0
    while i < len(data):
        print s_list[i:line_length + i]
        i += line_length
