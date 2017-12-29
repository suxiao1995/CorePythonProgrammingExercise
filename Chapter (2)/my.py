# 2-11
# 1、冒号
# 2、函数定义要在引用前
# 3、输入的为string，要转换
print 'add'
def abc():
    nums = raw_input('enter five number\n')
    num = nums.split()
    b = 0
    print num
    for i in num:
        b += int(i)
    c= float(b)/float(len(num))
    print b,c

def aff():
    nums = raw_input('enter five number\n')
    num = nums.split()
    b = 0
    for i in num:
        b += int(i)
    print b

while True:
    a = raw_input()
    if a == '1':
        aff()
    elif a == '2':
        abc()
    elif a == 'X' or a == 'x':
        break
    else:
        print 'wrong'

# 2-15
def sequence():
    num1 = int(raw_input("Number1:"))
    num2 = int(raw_input("Number2:"))
    num3 = int(raw_input("Number3:"))

    # from biggest to smallest
    print max(num1,num2,num3),min(max(num1,num2),max(num1,num2),max(num2,num3)),min(num1,num2,num3)

    # from smallest to biggest
    print min(num1,num2,num3),min(max(num1,num2),max(num1,num2),max(num2,num3)),max(num1,num2,num3)
