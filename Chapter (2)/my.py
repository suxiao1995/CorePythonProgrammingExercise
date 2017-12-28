#2-11
#1、冒号
#2、函数定义要在引用前
#3、输入的为string，要转换
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


