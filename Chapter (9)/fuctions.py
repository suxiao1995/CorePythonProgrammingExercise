# -*- coding: utf-8 -*-
__author__ = 'lihui'


# 9-1
def filter_print():
    f = open("filter.txt", 'r')
    for line in f:

        if "#" in line:
            if line[0] == "#":
                pass
            else:
                i = line.index("#")
                print line[:i]
        else:
            print line,

    f.close()


# 9-2
def file_get():
    n = int(raw_input("Enter line number:"))
    filename = raw_input("Enter filename:")
    f = open(filename, 'r')
    i = 0
    while i < n:
        for line in f.readlines():
            print line,
            i += 1
    f.close()


# 9-3
def file_info():
    filename = raw_input("Enter filename:")
    f = open(filename, 'r')
    print len(f.readlines())


# 9-4
def file_get2():
    filename = raw_input("Enter filename:")
    f = open(filename, 'r')
    all_lines = f.readlines()
    i = 0
    while i < len(all_lines):
        for line in all_lines[i: i + 25]:
            print line,
        raw_input("Enter any key to continue:")
        i += 25
