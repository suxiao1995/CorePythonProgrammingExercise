#chapter 5
from __future__ import division
import math
import random

#5.2











def judge_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        print "leap year"
    elif (year % 4 == 0) and (year % 100 == 0):
        print "leap year"
    else:
        print"Wrong"
        
def change():
    moneyamount = random.randrange(1,100)
    a,money = divmod(moneyamount,25)
    b,money = divmod(money,10)
    c,money = divmod(money,5)
    d,money = divmod(money,1)
    print "We have %s dollars in all." % round((moneyamount / 100),2)
    print a,"25cents,",b,"10cents,",c,"5cents,",d,"1cents."
    return a,b,c,d
    
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
        
def tax():
    price = random.randrange(0,100)
    tax = 0.08
    return price*tax
    
def geometry_calculate():
    length = int(raw_input("Enter the length:"))
    width = int(raw_input("Enter the width:"))
    height = int(raw_input("Enter the height:"))
    radius = int(raw_input("Enter the radius:"))
    square_area = length * width
    cube_area = length * width * 6
    circle_area = math.pi * (radius ** 2)
    cube_volume =  length * width * height
    circle_volume = 3.0/4.0 * math.pi * (radius ** 3)
    return """
    square_area = % d
    cube_area = % d
    circle_area = % d
    cube_volume =  % d
    circle_volume = % d""" % (square_area,cube_area,circle_area,cube_volume,circle_volume)

def f_to_c(f):
    c = (f - 32) * (5. / 9.)
    return c
def c_to_f(c):
    f = c / (5. / 9.) + 32
    return f
    
def residues():
    for i in range(0,21):
        if i % 2 != 0:
            print i
def residues_two():
    N1 = int(raw_input("the first number:"))
    N2 = int(raw_input("the second number:"))
    if (N1 % N2 == 0) or (N2 % N1 == 0):
        return True
    else:
        return False

        
def check():
    i = 99999999999
    while True:
        i *= 1567354236548567574345
        print i

def change_time():
    hour = int(raw_input("Enter hours amount:"))
    minute = int(raw_input("Enter minutes amount:"))
    minutes = hour * 60 + minute
    return minutes
    
def bank_tax():
    pass
    
def divisor_and_multiple():
    N1 = int(raw_input("the first number:"))
    N2 = int(raw_input("the second number:"))
    divisor = []
    for num in range(1,N1) and range(1,N2):
        if N1 % num == 0 and N2 % num == 0:
            divisor.append(num)
            
    #calculate the multiple of bigger one,then find the common multiple.     
    big = max(N1,N2)
    N3 = (big * n for n in range(1,min(N1,N2)+1))
    multiple = []
    for num in N3:
        if num % min(N1,N2) == 0:
            multiple.append(num)
    
    print "Maximum divisor is:",max(divisor)
    print "Minimum multiple is:",min(multiple)
    

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
        num = random.choice(numbers)
        NewNum.append(num)
        a += 1
        
    finalNum = sorted(NewNum)
    print finalNum

random_number()









