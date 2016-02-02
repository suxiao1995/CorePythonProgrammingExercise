# -*- coding: utf-8 -*-
__author__ = 'lihui'


# 8-2
def a_range(f, t, i):
    return range(f, t, i)


# 8-4
def is_prime(num):

    count = num / 2
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True


# 8-5
def get_factors(num):
    return [x for x in range(1, num+1) if num % x == 0]


# 8-6
def prime_factors(num):     # finally solved... #_#

    result = []

    def get_prime(f_list):

        for i in f_list:
            if is_prime(i) == 1:    # 1 equals True
                result.append(i)
            else:
                get_half_factors(i)

    def get_half_factors(number):

        factors = get_factors(number)[1: -1]   # 8-5
        if len(factors) == 1:
            f_list = [factors[0], factors[0]]

        elif len(factors) % 2 == 0:
            half = len(factors)/2
            f_list = factors[half-1: half+1]

        else:
            half = len(factors)/2
            f_list = [factors[half], factors[half]]

        get_prime(f_list)

    get_half_factors(num)
    return result


# 8-7
def is_perfect(num):
    if num == sum(get_factors(num)[:-1]):
        return 1
    else:
        return 0


# 8-8
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# 8-9
def fibonacci(n):
    fib_list = [1, 1]
    i = 0
    while i < n - 1:
        last = fib_list[-1] + fib_list[-2]
        fib_list.append(last)
        i += 1
    return fib_list[n - 1]


# 8-10
def count_text(words):
    result = {"vowel": 0, "consonant": 0, "words": 0}
    for i in words.strip():

        if i in "aeiou":
            result["vowel"] += 1
        elif i in "bcdfghjklmnpqrstvwxyz":
            result["consonant"] += 1

    result["words"] = len(words.split())

    return result


# 8-11
def input_name():
    names = []
    total = int(raw_input("Enter total number of names:"))

    wrong_time = 0
    i = 0
    while i < total:
        name = raw_input("Please enter name %d:" % i)
        name = name.split()
        if len(name) == 2 and name[0][-1] == ",":
            names.append(name)
        else:
            wrong_time += 1
            print "Wrong format... should be Last, First"
            print "You have done this %d time(s) already" % wrong_time

            if "," not in name[0]:
                name[0] += ","
            if name[1] == ",":
                del name[1]
            if name[1][0] == ",":
                name[1] = name[1][1:]
            if name[1][-1] == ",":
                name[1] = name[1][:-1]

            names.append(name)

        i += 1
    print "The sorted names list (by last name) is:"
    names = sorted(names, key=lambda last_name: last_name[1])
    for name in names:
        print "%s %s" % (name[0], name[1])


# 8-12
def print_sth():
    print "-" * 10
    start = int(raw_input("Enter start value:"))
    end = int(raw_input("Enter end value:"))
    if end > 33:
        print "DEC\t\tBIN\t\tOCT\t\tHEX\t\tASCII"
        print "-" * 40

        for i in range(start, end+1):
            print "{:d}\t\t{:b}\t\t{:o}\t\t{:x}\t\t{:c}".format(i, i, i, i, i)

    else:
        print "DEC\t\tBIN\t\tOCT\t\tHEX"
        print "-" * 30

        for i in range(start, end+1):
            print "{:d}\t\t{:b}\t\t{:o}\t\t{:x}".format(i, i, i, i)
