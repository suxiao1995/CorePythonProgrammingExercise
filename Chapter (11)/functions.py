# -*- coding: utf-8 -*-
__author__ = 'lihui'


# 11-3(a)
def max2(x, y):
    if x > y:
        return x
    else:
        return y

def min2(x, y):
    if x > y:
        return  y
    else:
        return  x


# 11-3(b)
def my_max(*args):
    return max(*args)


def my_min(*args):
    return min(*args)


# 11-4
def change_time():
    hour = int(raw_input("Enter hours amount: "))
    minute = int(raw_input("Enter minutes amount: "))
    minutes = hour * 60 + minute
    hours = hour + minute / 60.
    return minutes, hours


# 11-5
def tax_pro(tax_rate=0.7):
    import random
    price = random.randrange(0,100)
    return price * tax_rate


# 11-6
def printf(s, f):
    pass


# 11-7
def match_list(list1, list2):
    return map(None, list1, list2)  # equal to: return zip(list1, list2)


# 11-8
def judge_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def leap_year(years):

    return filter(judge_year, years)
    # return [year for year in years if judge_year(year)]


# 11-9
def average(numbers):
    return reduce((lambda x, y: x + y), numbers) / float(len(numbers))


# 11-11
def clear_file():
    filename = raw_input("Enter the filename:")
    choice = """
    1. New file
    2. Re-write
    Enter the number: """
    choice = raw_input("Enter the number:")

    def del_blank(line):
        return line.strip()
    all_lines = open(filename).readlines()
    # new_lines = map(del_blank, all_lines)
    new_lines = [line.strip() for line in all_lines]

    if choice == "1":
        open(filename, 'w').writelines(new_lines)
    elif choice == "2":
        new_filename = raw_input("Enter the new filename:")
        open(new_filename, 'w').writelines(new_lines)


# 11-12
def timeit(func, arg):
    import time
    start = time.clock()
    return_value = func(arg)
    end = time.clock()
    pass_time = end - start

    return pass_time, return_value


# 11-13(a)
def mult(x ,y):
    return x * y


# 11-13(b)
def factorial(n):
    return reduce(mult, range(1, n + 1))


# 11-13(c)
def factorial_pro(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

# 11-13(d)
def fac_timeit():
    def fac_recursion(n):
        if n == 1:
            return 1
        else:
            return n * fac_recursion(n-1)

    def fac_iter(n):
        i = 1
        for num in range(1, n + 1): # 1~n
            i *= num
        return i

    def fac_reduce(n):
        return reduce(lambda x, y: x * y, range(1, n + 1))

    print timeit(fac_recursion, 10)
    print timeit(fac_iter, 10)
    print timeit(fac_reduce, 10)


# 11-14
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 11-15
def print_str_pro():
    import time

    s = raw_input("Enter a string:")
    length = len(s)

    if length % 2 == 0:
        s_center = length / 2
    else:
        s_center = (length / 2) + 1

    i = 1
    print " " * 20 + s[s_center]
    def print_s(i):
        #time.sleep(1)
        j = i
        print "%20s%-20s " % (s[s_center - j: s_center], s[s_center: s_center + i])
        if s_center + i < length:
            if j == s_center:
                j -= 1
            return print_s(i + 1)

    print_s(i)

