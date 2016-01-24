# _*_ coding:utf-8 _*_ 



# 7-1
dict1 = {"name":"lihui","age":"21"}
dict2 = {"hobby":"reading"}
dict1.update(dict2)


# 7-4
num = [1,2,3,4,5]
english = ["one","two","three","four","five"]
result = dict(zip(num,english))


# 7-7
def revervse_dict(dict1):
    dict2 = {}
    for eachkey in dict1:
        dict2[dict1[eachkey]] = eachkey
    return dict2


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


