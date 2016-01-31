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
    return [x for x in range(1,num+1) if num % x == 0]


# 8-6
def prime_factors(num): # unsolved #_#

    result = []
    def get_prime(f_list):
        print "wa",f_list
        if f_list == None:
            return 1
        for i in f_list:
            print i
            print is_prime(i)
            if is_prime(i) == True:
                return i
            else:
                f_list = prime_factors(i)
                get_prime(f_list)

    factors = get_factors(num)[1: -1]
    while True:
        if len(factors) > 1:
            half = len(factors)/2
            f_list = factors[half-1: half+1]
            print f_list
            prime = get_prime(f_list)
            if prime == 1:
                break
            result.append(prime)
            break
        else:
            result.append(factors[0])
            result.append(factors[0])
            break

    print result
    return result

# print prime_factors(20)

# 8-7
def is_perfect(num):
    if num == sum(get_factors(num)[:-1]):
        return 1
    else:
        return 0


# 8-8
def factorial(N):
    if N == 1:
        return 1
    return N * factorial(N - 1)

# 8-9
def fibonacci(N):
    fib_list = [1, 1]
    i = 0
    while i < N - 1:
        last = fib_list[-1] + fib_list[-2]
        fib_list.append(last)
        i += 1
    return fib_list[N - 1]

# 8-10