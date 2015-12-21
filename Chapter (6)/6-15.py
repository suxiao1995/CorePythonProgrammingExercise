# _*_ coding:utf-8 _*_ 
import time

# 6-15

def calculate(date1,date2):

    days = int(date2[0:2]) - int(date1[0:2])
    months = int(date2[3:5]) - int(date1[3:5])
    years = int(date2[6:]) - int(date1[6:])

    total_days = years * 365 + months * 30 + days

    # leap year
    for year in range(int(date1[6:]), int(date2[6:])+1):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            total_days += 1

    # leap year in incomplete year
    if years > 1 and int(date2[3:5]) > 2:
        total_days += 1
        
    return total_days
    
def date_days():
    
    date1 = raw_input("Enter a start date (DD/MM/YYYY) : ")
    date2 = raw_input("Enter a end date (DD/MM/YYYY) : ")

    calculate(date1,date2)
    
def birth_days():
    now = time.localtime()
    date1 = raw_input("Enter your birth date (DD/MM/YYYY) : ")
    date2 = str(now.tm_mday) + "/" + str(now.tm_mon) + "/" + str(now.tm_year)
    
    calculate(date1,date2)
    
def next_birthday():
    now = time.localtime()
    birthdate = raw_input("Enter your birth date (DD/MM/YYYY) : ")
    date1 = str(now.tm_mday) + "/" + str(now.tm_mon) + "/" + str(now.tm_year)
    date2 = birthdate[0:6] + str(now.tm_year + 1)
    
    calculate(date1,date2)
    
def showmenu():
    pr = """
    1. Calculate days between two date.
    2. Calculate days sum from birth date to today.
    3. Calculate days from today to next birthday.
    Format: DD/MM/YYYY 
    Enter the choice: """
    
    choice = raw_input(pr)

    CMDs = {'1':date_days,'2':birth_days,'3':next_birthday}
    
    CMDs[choice]()
    
if __name__ == "__main__":
    showmenu()