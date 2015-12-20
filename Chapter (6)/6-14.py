# _*_ coding:utf-8 _*_ 
import random
    
def rochambeau(Userchoice):

    AIchoice = str(random.randint(1,3))
    # 列举可能的结果，
    result_dict = {"11":"Tie!",'22':'Tie!','33':'Tie','12':'You win!','13':'You lose!',
            '21':'You lose!','23':'You win!','31':'You win!','32':'You lose!'}
    menu = {"1":"rock","2":"scissors","3":"paper"}
    # 结果由用户和电脑的选项相结合的数字决定
    result = result_dict[Userchoice + AIchoice]
    user = menu[Userchoice]
    AI = menu[AIchoice]
    
    print "-" * 20
    print "You:",user
    print "AI:",AI
    print "Result:",result
    
def main():
    while True:
        print """
    1.rock
    2.scissors
    3.paper
    4.quit"""
        # get the choice
        Userchoice = raw_input("Enter your choice:")
        
        if Userchoice not in str(range(1,5)):
            print "Wrong choice!"
        elif Userchoice == "4":
            break
        else:
            rochambeau(Userchoice)
        
    
if __name__ == "__main__":
    main()