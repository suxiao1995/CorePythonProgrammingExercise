# _*_ coding:utf-8 _*_ 



# 7-1
dict1 = {"name":"lihui","age":"21"}
dict2 = {"hobby":"reading"}
dict1.update(dict2)


# 7-3
def dict_index():
    s = {"b":2, "c":3, "a":4}
    keys = sorted(s.keys())
    values = sorted(s.values())
    print keys # (a)

    for key in keys:
        print s[key]    # (b)

    for value in values:
        print s[value]  #(c)


# 7-4
num = [1,2,3,4,5]
english = ["one","two","three","four","five"]
result = dict(zip(num,english))


# 7-6
def invest_db():
    prompt = """
    Please input the stock, purchase price, current price, minimum index:
    (separate with space, enter a dot to quit.)
    >:"""
    db_list = []
    while True:
        date = raw_input(prompt)
        if date == ".":
            break
        db_list.append(date.split())

    print """Please choose a item to index
          (0)stock
          (1)purchase price
          (2)current price
          (3)minimum index
          (4)price chage
          Enter the number:"""

    choice = int(raw_input(">"))
    new_list = sorted(db_list, key=lambda item:item[choice])
    db_dict = {}

    for item in new_list:
        change = int(item[2]) - int(item[1])
        item.append(str(change))
        db_dict[item[choice]] = item

    return db_dict


# 7-7
def revervse_dict(dict1):
    dict2 = {}
    for eachkey in dict1:
        dict2[dict1[eachkey]] = eachkey
    return dict2


# 7-8
def sort_data():
    from operator import itemgetter
    name_list = []
    while True:
        name = raw_input("Enter the name and number(Jack 34), enter a dot to quit:")
        if name == ".":
            break
        name = name.split()
        name[1] = int(name[1])
        name_list.append(name)

    print """
    Select output index:
    (1) By Name
    (2) By number"""

    choice = int(raw_input(">"))
    if choice == 1:
        print sorted(name_list, key=itemgetter(0))
    elif choice == 2:
        print sorted(name_list, key=itemgetter(1))


# 7-9
def tr(srcstr, dststr, string, lowercase=False):
    if lowercase == True:
        srcstr = srcstr.lower()
        dststr = dststr.lower()

    if len(srcstr) == len(dststr):
        result = string.replace(srcstr,dststr)
    elif len(srcstr) > len(dststr):
        n = len(dststr)
        new_string = string.replace(srcstr[:n],dststr)
        result = new_string.replace(srcstr[n:],"")

    return  result


# 7-10
def rot13():
    import string
    lower = string.lowercase
    upper = string.uppercase

    string1 = raw_input("Enter the string to rot13:")
    string2 = ""
    for i in string1:
        if i in lower:
            n = lower.find(i)
            case = lower
        elif i in upper:
            n = upper.find(i)
            case = upper
        else:   # ignore digits or symbol
            n = 28

        if n < 13:
            string2 += case[n+13]
        elif n in range(13, 27):
            string2 += case[n-13]
        else:   # digits or symbol
            string2 += i

    return """
    Your string to en/decrypt was: %s
    The rot13 string is:%s
    """ % (string1, string2)


# 7-13
def random_set():
    import random

    i = 0
    set_A = set()
    set_B = set()

    while i < 10:
        set_A.add(random.randrange(0,10))
        set_B.add(random.randrange(0,10))
        i += 1

    return set_A | set_B, set_A & set_B


# 7-14
def test_set():
    import random

    i = 0
    set_A = set()
    set_B = set()

    while i < 11:
        set_A.add(random.randrange(0,10))
        set_B.add(random.randrange(0,10))
        i += 1

    print "set A is:",set_A
    print "set B is:",set_B

    or_set = set_A | set_B
    and_set = set_A & set_B

    prompt1 = "set_A | set_B:"
    prompt2 = "set_A & set_B:"

    answer_or = False
    answer_and = False
    i = 0
    while i < 3:
        answer1 = raw_input(prompt1)
        answer2 = raw_input(prompt2)
        if answer1 == or_set:
            answer_or = True
        if answer2 == and_set:
            answer_and = True
        if (answer_and == True) and (answer_or == True):
            break
        i += 1
    else:
        print "set_A | set_B:", or_set
        print "set_A & set_B:", and_set

def sub_set():
    import random

    i = 0
    set_A = set()
    set_B = set()

    while i < 11:
        set_A.add(random.randrange(0,10))
        i += 1

    while i < random.randrange(0, 10):
        

    print "set A is:",set_A
    print "set B is:",set_B
