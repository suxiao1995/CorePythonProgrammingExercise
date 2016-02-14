# -*- coding: utf-8 -*-
import pickle as p
import re
__author__ = 'lihui'

# 9-11
def menu():
    global bookmarks_list, bookmarks_file
    bookmarks_file = "booklist.date"
    try:
        f = open(bookmarks_file)
        bookmarks_list = p.load(f)
        f.close()
    except:
        bookmarks_list = {"search": [["google", "www.google.com", "A search website"]]}

    while True:

        print """
        Please enter operate:
        1. Look up
        2. New
        3. Edit
        4. Delete
        Enter the number('.' to quit): """

        choice = raw_input(">")
        if choice == ".":
            break

        if choice == "1":
            look_up()
        elif choice == "2":
            add_new()
        elif choice == "3":
            edit()
        elif choice == "4":
            delete()

        save_file()


def look_up():
    keyword = raw_input("Enter keyword:")
    for key in bookmarks_list.keys():
        for bookmark in bookmarks_list[key]:

            for item in (bookmark[0], bookmark[1]):
                if keyword in item:
                    print bookmark


def add_new():
    name = raw_input("Enter name:")
    url = raw_input("Enter url:")
    description = raw_input("Enter description(optional):")
    folder = raw_input("Choose a folder(optional):")

    if folder == "":
        bookmarks_list["untitled"] = [[name,url,description]]
    elif folder in bookmarks_list:
        bookmarks_list[folder].append([name,url,description])
    else:
        bookmarks_list[folder] = [[name,url,description]]


def edit():
    for key in bookmarks_list:
        print key
        for index, item in enumerate(bookmarks_list[key]):
            print index, item

    folder = raw_input("Enter the folder:")
    index = int(raw_input("Enter the index:"))
    bookmarks_list[folder][index][0] = raw_input("Enter the new name:")
    bookmarks_list[folder][index][1] = raw_input("Enter the new url:")
    bookmarks_list[folder][index][2] = raw_input("Enter the new description (optional):")
    newfolder = raw_input("Choose a new folder: (optional):")
    if newfolder != "":
        bookmarks_list[newfolder] = [bookmarks_list[folder][index]]
        del bookmarks_list[folder][index]


def delete():
    for key in bookmarks_list:
        print key
        for index, bookmark in enumerate(bookmarks_list[key]):
            print index, bookmark
    prompt = """
    What are you want to delete?
    1. folder
    2. bookmark
    Enter the number:"""
    choice = raw_input(prompt)

    folder = raw_input("Enter the folder:")
    if choice == "1":
        for bookmark in bookmarks_list[folder]:
            bookmarks_list["untitled"].append(bookmark)
        del bookmarks_list[folder]
    else:
        index = int(raw_input("Enter the index:"))
        del bookmarks_list[folder][index]


def save_file():
    f = open(bookmarks_file, 'w')
    p.dump(bookmarks_list, f)
    f.close()

    html = "booklist.html"
    f = open(html, 'w')
    for folder in bookmarks_list.keys():
        f.write("""<div><h1 style="color:red"><br>"""+folder+"<br></h1></div>")
        for bookmark in bookmarks_list[folder]:
            f.write("<hr>")
            for item in bookmark:
                f.write(item+"<br>")

    f.close()

    print bookmarks_list

    p = re.compile("[a-z_0-9]+@[a-z0-9]+[.]{1}[a-z]+") # email address
if __name__ == "__main__":
    menu()