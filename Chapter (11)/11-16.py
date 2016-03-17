# -*- coding: utf-8 -*-
from operator import add, sub, mul
from random import randint, choice
__author__ = 'lihui'

# 11-16


ops = {'+': add, '-': sub, '*': mul}
max_tries = 2

def doprob():
    op = choice('+-*')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print "Correct!"
                break
            if oops == max_tries:
                print "Answer\n%s%d" % (pr, ans)
            else:
                print "Incorrect... try again!"
                oops += 1
        except (KeyboardInterrupt,
                EOFError, ValueError):
            print "Invalid input... try again!"


def main():
    while True:
        doprob()
        try:
            opt = raw_input("Again? Enter to continue, or 'n' to quit.").lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == "__main__":
    main()