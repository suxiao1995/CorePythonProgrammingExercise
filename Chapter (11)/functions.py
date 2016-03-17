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
def printf():
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


# 11-14
def print_str():
    from time import sleep
    string = raw_input("Enter a string:")
    i = 0
    length = len(string)

    if length % 2 == 0:
        s_center = length / 2
    else:
        s_center = (length / 2) + 1

    i = 0
    while i < (s_center + 1):
        # %20s%s%-20s: the number between '%' and 's' means to fill up 20 spaces.
        print "%20s%s%-20s" % (string[s_center - i:s_center], string[s_center],
                            string[s_center + 1:s_center + i])
        i += 1
        sleep(1)

def print_str_pro():
    s = raw_input("Enter a string:")
    length = len(s)

    print length
    if length % 2 == 0:
        s_center = length / 2
    else:
        s_center = (length / 2) + 1

    print s_center
    print "-----------"
    print s[s_center]
    print "-----------"

    i = 1

    def print_s(i):
        print s[s_center - i], s[s_center + i]
        if i < s_center + 1:
            print i
            return print_s(i + 1)

    print_s(i)

print_str_pro()
