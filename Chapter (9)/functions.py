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

        if score in range(90, 101):
            return "A"
        elif score in range(80, 90):
            return "B"
        elif score in range(70, 80):
            return "C"
        elif score in range(60, 70):
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


# 9-7 ?
def ini_file():
    f1 = open("file.ini", 'r')
    for line in f1.readlines():
        print line,


# 9-8
def module_info():
    modulename = raw_input("Enter module name:")
    print help(modulename)


# 9-9
def check_doc():
    import os
    from os.path import splitext, basename

    lib_path = "C:\Python27\Lib"
    os.chdir(lib_path)
    py_file = []
    no_doc_file = []
    result_file = open("module_doc.txt", 'a')
    doc_mark = "\"\"\""

    for root, dirs, files in os.walk(lib_path):
        for file in files:
            if splitext(file)[1] == ".py":
                py_file.append(root + "\\" + file) # find the py file

    for file in py_file:
        f = open(file)
        all_lines = f.readlines()
        all_string = " ".join(all_lines)
        three_line = " ".join(all_lines[:3])
        filename = basename(file)
        if doc_mark in three_line:
            start = all_string.find(doc_mark) # find the beginning of the doc
            new_string = all_string[start + 3:]
            doc_string = new_string.partition(doc_mark)[0] # get the doc
            result_file.write("\n" + filename + "\n")
            result_file.write(doc_string)
        else:
            no_doc_file.append("\n" + filename + "\n")

        f.close()

    result_file.write("\nNo doc file:\n")
    result_file.writelines(no_doc_file)
    result_file.close()

def check_doc_pro():
    pass


# 9-10
def finance():
    import pickle as p

    account_file = "account_balance.data"
    try:
        f = open(account_file)
        account_dict = p.load(f)
    except:
        account_dict = {"save": 0, "cheque": 0, "market": 0, "regular save": 0}

    account_choice = {1: "save", 2: "cheque", 3: "market", 4: "regular save"}
    while True:
        print """
            Please choose a account:
            1. save
            2. cheque
            3. market
            4. regular save
            Enter the number ('.' to quit) :"""

        account = raw_input(">")
        if account == ".":
            break
        account = account_choice[int(account)]

        while True:
            print """
                Please choose operate:
                1. save
                2. withdraw
                3. borrow
                4. loan
                Enter the number ('.' to quit) :"""

            operate = raw_input(">")
            if operate == ".":
                break
            money = raw_input("Enter the sum:")

            if operate == "1":
                account_dict[account] += int(money)
            elif operate in "234":
                account_dict[account] -= int(money)

            f = open(account_file, 'w')
            p.dump(account_dict, f)
            f.close()

    for key in account_dict.keys():
        print "%s: %s" % (key, account_dict[key])

    return account_dict


# import re
# while True:
#     p = re.compile("(www.)[a-z0-9_]+[.]{1}[a-z]+[.]?[a-z]+")
#     # p = re.compile("[a-z_0-9]+@[a-z0-9]+[.]{1}[a-z]+[.]?[a-z]*")
#     t = raw_input(">")
#     m = p.match(t)
#     if m:
#         print m.group()
#     else:
#         print "No Match"

# 9-13
def print_argv():
    import sys

    for i in sys.argv:
        print i



# 9-14
def calculate():
    import sys

    filename = "date.txt"
    comment = None

    if sys.argv[1] == "print":
        f = open(filename, 'r+')
        for line in f.readlines():
            print line,
        f.truncate(0) # clear the content
        f.close()
        return None

    for i in range(len(sys.argv)):
        if "#" == sys.argv[i]:
            comment = " ".join(sys.argv[i:])

    n1 = float(sys.argv[1])
    n2 = float(sys.argv[3])
    operate = sys.argv[2]

    if operate == "+":
        result = n1 + n2
    elif operate == "-":
        result = n1 - n2
    elif operate == "*":
        result = n1 * n2
    elif operate == "/":
        result = n1 / n2
    elif operate == "**":
        result = n1 ** n2
    elif operate == "%":
        result = n1 % n2
    else:
        result = None

    f = open(filename, 'a')
    expression = sys.argv[1] + sys.argv[2] + sys.argv[3]
    f.write(expression + comment + "\n")
    f.write(str(result) + "\n")
    f.close()

    return result


# 9-15
def transfer():
    import sys

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    f1 = open(filename1, 'r')
    f2 = open(filename2, 'a')
    for line in f1.readlines():
        f2.write(line)
    f1.close()
    f2.close()



# 9-16
def line_adjust():
    filename = raw_input("Enter the filename:")
    f = open(filename)
    all_lines = f.readlines()
    f = open(filename, 'w')
    for line in all_lines:
        if len(line) > 80:
            i = len(line) / 80
            while i > 0:
                line = line[:80 * i] + "\n" + line[80 * i:]
                i -= 1
        f.write(line)
    f.close()


# 9-18
def count_file():
    byte = raw_input("Enter the byte value:")
    filename = raw_input("Enter the filename:")

    f = open(filename)
    all_string = " ".join(f.readlines())

    return all_string.count(chr(int(byte)))


# 9-19
def random_bin(byte_value, times, size):
    import random

    byte_value = int(byte_value)
    times = int(times)
    size = int(size)

    filename = "date.bin"
    content = []

    while len(content) < (size - times):
        random_byte = random.randint(0, 255)
        content.append(chr(random_byte))

    while len(content) < size:
        content.append(chr(byte_value))

    random.shuffle(content) # shuffle the list

    f = open(filename, 'w')
    f.writelines(content)
    f.close()


# 9-20
def de_or_compress():
    import gzip
    import shutil

    prompt = """
    1. Compress
    2. Decompress
    Enter the number:"""
    mode = raw_input(prompt)
    filename =raw_input("Enter the filename:")

    if mode == "1":
        with open(filename, 'rb+') as f_in, gzip.open(filename+'.gz', 'wb', 9) as f_out:
            shutil.copyfileobj(f_in, f_out)
    elif mode == "2":
        with gzip.open(filename) as f_in, open(filename[:-3], 'w') as f_out:
            f_out.write(f_in.read())


# 9-21
def zip_file():
    import zipfile

    zip_filename = raw_input("Enter the zip filename:")
    prompt = """
    1. Add file
    2. Extract file
    Enter the number:"""
    choice = raw_input(prompt)

    with zipfile.ZipFile(zip_filename, 'a') as zfile:
        if choice == "1":
            filename = raw_input("Enter the filename:")
            zfile.write(filename)
        elif choice == "2":
            for name in zfile.namelist():
                print name
            filename = raw_input("Enter the filename:")
            zfile.extract(filename)


# 9-23
def lstar():
    import time
    import tarfile
    import lszip

    filename = raw_input("Enter the filename:")
    if filename.split(".")[1] == "zip":
        return lszip.show_zip_info(filename)

    f = tarfile.open(filename)
    for file in f.getnames():
        info = f.getmember(file)
        print "Name: %s" % info.name
        print "Size: %s" % info.size
        print "Time: %s\n" % time.ctime(info.mtime)


# 9-24
def transfer_file():
    import tarfile
    import zipfile

    filename = raw_input("Enter the filename you want to move:")
    object_file = raw_input("Enter the object filename:")

    if filename.split(".")[1] == "zip":
        with zipfile.ZipFile(filename) as f_from:
            file_list = f_from.namelist()
    else:
        with tarfile.open(filename) as f_from:
            file_list = f_from.getnames()

    if object_file.split(".")[1] == "zip":
        with zipfile.ZipFile(filename, 'a') as f_to:
            for file in file_list:
                f_to.write(file)
    else:
        with tarfile.open(object_file, 'w') as f_to:
            for file in file_list:
                f_to.add(file)


transfer_file()

