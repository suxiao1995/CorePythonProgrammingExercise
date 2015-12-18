# _*_ coding:utf-8 _*_ 
# Chapter 5
from __future__ import division
import math
import random

#If you want to show the result,you have to use "print func()".

# 5.2
def multi(Num1,Num2):
    return "Result is:",Num1 * Num2

#   print multi(3,5)


# 5-4
def judge_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return "leap year"
    elif (year % 4 == 0) and (year % 100 == 0):
        return "leap year"
    else:
        return"Wrong"
        

# 5-5
def change():
    moneyamount = random.randrange(1,100) # import random
    a,money = divmod(moneyamount,25)
    b,money = divmod(money,10)
    c,money = divmod(money,5)
    d,money = divmod(money,1)
    
    return """
    We have %s dollars in all.
    %d 25cents,%d 10cents,%d 5cents,%d 1cents.
    """ % (round((moneyamount / 100),2),a,b,c,d)
    

# 5-6    
def calculate(expression):
    expression = raw_input("Please enter the expression(example:1+2):")
    elements = expression.split()
    N1 = float(elements[0])
    N2 = float(elements[2])
    operate = elements[1]
    if operate == "+":
        return N1 + N2
    elif operate == "-":
        return N1 - N2
    elif operate == "*":
        return N1 * N2
    elif operate == "/":
        return N1 / N2
    elif operate == "**":
        return N1 ** N2
    elif operate == "%":
        return N1 % N2
    else:
        print "Unknown expression!"
     
 
# 5-7
def tax():
    price = random.randrange(0,100)
    tax = 0.05
    return price*tax
    
    
# 5-8
def geometry_calculate():
    length = int(raw_input("Enter the length:"))
    width = int(raw_input("Enter the width:"))
    height = int(raw_input("Enter the height:"))
    radius = int(raw_input("Enter the radius:"))
    square_area = length * width
    cube_area = length * width * 6
    circle_area = math.pi * (radius ** 2)
    cube_volume =  length * width * height
    circle_volume = 3.0 / 4.0 * math.pi * (radius ** 3)
    return """
    square_area = % d
    cube_area = % d
    circle_area = % d
    cube_volume =  % d
    circle_volume = % d""" % (square_area,cube_area,circle_area,cube_volume,circle_volume)


# 5-10
def f_to_c(f):
    c = (f - 32) * (5. / 9.)
    return c
def c_to_f(c):
    f = c / (5. / 9.) + 32
    return f
    

# 5-11    
def resides():
    for i in range(0,21):
        if i % 2 != 0:
            print "Odd number:",i
        elif i % 2 == 0:
            print "Even number:",i
            
def residues_two():
    N1 = int(raw_input("the first number:"))
    N2 = int(raw_input("the second number:"))
    if (N1 % N2 == 0) or (N2 % N1 == 0):
        return True
    else:
        return False

        
# 5-12
def check():
    i = 99999999999
    while True:
        i *= 1567354236548567574345
        print i

# 5-13
def change_time():
    hour = int(raw_input("Enter hours amount:"))
    minute = int(raw_input("Enter minutes amount:"))
    minutes = hour * 60 + minute
    return minutes
    
    
# 5-14
def bank_tax(money):
    money = int(money)
    rate = 0.3
    FV = money*(1 + rate) ** 1
    return FV
    

# 5-15
def divisor_and_multiple():
    N1 = int(raw_input("the first number:"))
    N2 = int(raw_input("the second number:"))
    divisor = []
    for num in range(1,N1) and range(1,N2):
        if N1 % num == 0 and N2 % num == 0:
            divisor.append(num)
            
    # calculate the multiple of bigger one,then find the common multiple.     
    big = max(N1,N2)
    N3 = (big * n for n in range(1,min(N1,N2)+1))
    multiple = []
    for num in N3:
        if num % min(N1,N2) == 0:
            multiple.append(num)
    
    return """
    Maximum divisor is:%d
    Minimum multiple is:%d""" % (max(divisor),min(multiple))
    
    
# 5-16
def house_finance():
    open = float(raw_input("Enter opening balance:"))
    monthly = float(raw_input("Enter monthly payment:"))
    Pymt = 0
    remain = open
    print "\t\tAmount\tRemaining"
    print "Pymt# \tPaid \t\tBalance"
    print "------\t-------\t----------"
    while remain >= 0:
        remain = open - Pymt * monthly
        print "%d \t $%f \t $%f" % (Pymt,monthly,remain)
        Pymt += 1
    # Still a bit of problem...

# 5-17       
def random_number():
    randomNum = random.randint(2,101)
    Num = 0
    numbers = []
    
    while Num < randomNum:
        num = random.randint(0,2**31)
        numbers.append(num)
        Num += 1
    
    length = random.randint(1,101)
    NewNum = []
    
    a = 0
    while a < length:
        num = random.choice(numbers) # get random number
        NewNum.append(num)
        a += 1
        
    finalNum = sorted(NewNum)
    return finalNum





