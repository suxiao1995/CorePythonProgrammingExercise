# -*- coding: utf-8 -*-
__author__ = 'lihui'
# 9-17


def new():
    global filename
    filename = raw_input("Enter the filename:")
    content = []

    while True:
        line = raw_input("Enter a line('.' to quit):")
        if line == ".":
            break
        content.append(line + "\n")

    f = open(filename, 'w')
    f.writelines(content)
    f.close()


def show():
    f = open(filename)
    for line in f.readlines():
        print line,
    f.close()


def edit():
    f = open(filename, 'r+')
    all_lines = f.readlines()
    for index, line in enumerate(all_lines):
        print index, line,

    line_number = raw_input("Enter the line number:")
    new_line = raw_input("Enter the content:")
    all_lines[int(line_number)] = new_line + "\n"

    f = open(filename, 'w') # clear the file
    f.writelines(all_lines) # re-write the content
    f.close()


def save(): # useless...
    print "Success!"


def show_menu():
    prompt = """
    (1) New File
    (2) Show File
    (3) Edit
    (4) Save
    (5) Quit
    Enter the number:"""

    while True:
        choice = raw_input(prompt)
        choice_menu = {"1": new, "2": show, "3": edit, "4": save, "5": quit}
        choice_menu[choice]()


if __name__ == "__main__":
    show_menu()
