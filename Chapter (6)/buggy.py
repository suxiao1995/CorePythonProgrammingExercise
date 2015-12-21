# _*_ coding:utf-8 _*_ 

# get a number(string)
num_str = raw_input("Enter a number: ")

# turn the string into integer
num_num = int(num_str)

# create and print a list that from 1 to num_num
fac_list = range(1,num_num+1)
print "BEFORE: ",fac_list

i = 0

# deal with every items in fac_list
while i < len(fac_list):
    
    # del the num_num's divisor in fac_list
    if num_num % fac_list[i] == 0:
        del fac_list[i]
   
    i = i + 1
    
# print the remaining items in fac_list
print "AFTER: ",fac_list