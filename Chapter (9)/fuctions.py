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
    f.close()


# 9-5
def exam_grade():
    score_list = []

    while True:
        filename = raw_input("Enter the filename('.' to quit):")
        if filename == ".":
            break
        f1 = open(filename, 'r')
        score_lines = f1.readlines()

        for i in score_lines:
            for j in i.split():
                score_list.append(int(j))

    def rank(score):

        if score in range(90,101):
          return "A"
        elif score in range(80,90):
          return "B"
        elif score in range(70,80):
          return "C"
        elif score in range(60,70):
          return "D"
        elif score < 60:
          return "F"

    average = sum(score_list) / float(len(score_list))
    rank_list = [rank(score) for score in score_list]
    return average, rank_list


# 9-6
def file_cmp(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()
    smaller = min(f1_lines, f2_lines)
    for i in range(len(smaller)):
        if f1_lines[i] != f2_lines[i]:
            for j in range(len(smaller[i])):
                if f1_lines[i][j] != f2_lines[i][j]:
                    return i, j

    return len(smaller), 0      # line start at 0


# 9-7
def ini_file():
    f1 = open("file.ini", 'r')
    for line in f1.readlines():
        print line,


# 9-8
def module_info():
    modulename = raw_input("Enter module name:")
    print help(eval(modulename))