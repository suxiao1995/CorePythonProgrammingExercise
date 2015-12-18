# Chapter 2

# 2-1
def simple_print():
    name = "lihui"
    age = 20
    color = "green"
    print "My name is %s,I am %d years old,my favourite color is %s." % (name,age,color)


# 2-4
def input_print():
    name = raw_input("Enter your name:")
    age = int(raw_input("Enter your age:"))
    print "Name:%s" % name
    print "Age:%d" % age


# 2-5
def print_num():
    i = 0
    while i < 11:
        print i
        i += 1 

    for i in range(0,11):
        print i
    

# 2-6
# num = 5
def judge_num():
    num = int(raw_input("Enter a number:"))
    if num > 0:
        print "+"
    elif num < 0:
        print "-"
    else:
        print "0"


# 2-7
def print_str():
    string = raw_input("Enter a string:")
    i = 0
    length = len(string)
    while i < length:
        print string[i]
        i += 1  # equal to i = i + 1                              
    
    for word in string:
        print word

        

# 2-8  
def num_sum():      
    nums = [1,2,4,3,5]
    # use while
    i = 0
    sum = 0
    length = len(nums)
    while i < length:
        sum += nums[i]  # equal to i = i + 1                              
        i += 1
    print sum
    
    # use for
    sum2 = 0
    for num in nums:
        sum2 += num
    print sum2

def num_sum2():
    nums = raw_input("Enter five number,split with space:")
    # make the five number into list.
    num = nums.split()
    #use while
    i = 0
    sum = 0
    length = len(num)
    while i < length:
        sum += int(num[i])  # equal to i = i + 1                              
        i += 1
    print sum
    
    # use for
    sum2 = 0
    for i in num:
        sum2 += int(i)
    print sum2
   
    
# 2-9
def average():
    nums = [1,2,3,4,6]
    sum = 0
    # calculate sum
    for i in nums:
        sum += int(i)
    # division
    result = float(sum) / float(len(nums))
    print result
    
    
# 2-10
def judge_input(): 
    while True:
        number = int(raw_input("Enter a number(1~100):"))
        if number in range(1,101):
            print "Done"
            break 
        else:
            print "Wrong number!"

# 2-11
def calculate():
    running = True
    while running:
        print """
        (1)sum
        (2)average
        (x)quit
        Enter the key in the brackets.
        """
        
        choose = raw_input(">")
        if choose == "1":
            nums = raw_input("Enter five number,split with space:")
            num = nums.split()
            i = 0
            sum = 0
            length = len(num)
            while i < length:
                sum += int(num[i])                            
                i += 1
            print "The sum is:",sum
            
        elif choose == "2":
            nums = raw_input("Enter five number,split with space:")
            num = nums.split()
            sum = 0
            for i in num:
                sum += int(i)
            result = float(sum) / float(len(num))
            print "The average is:",result
            
        else:
            print "Bye"
            running = False

# 2-15
def sequence():
    num1 = int(raw_input("Number1:"))
    num2 = int(raw_input("Number2:"))
    num3 = int(raw_input("Number3:"))

    # from biggest to smallest
    print max(num1,num2,num3),min(max(num1,num2),max(num1,num2),max(num2,num3)),min(num1,num2,num3)

    # from smallest to biggest
    print min(num1,num2,num3),min(max(num1,num2),max(num1,num2),max(num2,num3)),max(num1,num2,num3)
                