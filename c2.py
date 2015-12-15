#Chapter 2

#2-1
def simple_print():
    name = "lihui"
    age = 20
    color = "green"
    print "My name is %s,I am %d years old,my favourite color is %s." % (name,age,color)


#2-4
def input_print():
    name = raw_input("Enter your name:")
    age = int(raw_input("Enter your age:"))
    print "Name:%s" % name
    print "Age:%d" % age


#2-5
def print_num():
    i = 0
    while i < 11:
        print i
        i += 1 

    for i in range(0,11):
        print i
    

#2-6
#num = 5
def judge_num():
    num = int(raw_input("Enter a number:"))
    if num > 0:
        print "+"
    elif num < 0:
        print "-"
    else:
        print "0"


#2-7
def print_str():
    string = raw_input("Enter a string:")
    i = 0
    while i < len(string):
        print string[i]
        i += 1  #equal to i = i + 1                              
    
    for word in string:
        print word


#2-8  
def num_sum():      
    nums = [1,2,4,3,5]
    i = 0
    sum = 0
    while i < len(nums):
        sum += nums[i]  #equal to i = i + 1                              
        i += 1
        return sum
    
    sum2 = 0
    for num in nums:
        sum2 += num
        return sum2 
        
print num_sum()