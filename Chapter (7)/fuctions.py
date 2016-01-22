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
def reverse_dict(dict1):
    dict2 = {}
    for eachkey in dict1:
        dict2[dict1[eachkey]] = eachkey
    return dict2

