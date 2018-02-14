#5-1
def a(x,y):
    return x*y

print a(10,2)

#5-17
import random
def check():
    a=random.randint(2,100)
    i=0
    num1=[]
    while i<a:
        num=random.randint(0,2**31-1)
        num1.append(num)
        i=i+1
    b=random.randint(1,100)
    j=0
    num2=[]
    while j<b:
        num=random.choice(num1)
        num2.append(num)
        j=j+1
    num3=sorted(num2)
    return num3
a=check()
print a
