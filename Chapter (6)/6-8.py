# _*_ coding:utf-8 _*_ 

def englishNum(number):
    
    units = {'0':'','1':'one','2':'two','3':'three','4':'four',
            '5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten'}
    UtoT = {'11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
            '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen',}
            
    tens = {'0':'','2':'twenty','3':'thirty','4':'forty','5':'fifty',
        '6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
    
    # 单独处理大于20的整数
    if number % 10 == 0:

        if 100 > number > 10:
            number = str(number)
            ten = number[0]
            unit = number[1]
            return tens[ten]
            
        elif 1000 > number >= 100:
            number = str(number)
            hundred = number[0]
            ten = number[1]
            unit = number[2]
            return units[hundred]+" hundred"+" "+tens[ten]
    
    elif 10 < number < 20:
        number = str(number)
        return UtoT[number]
        
    elif 20 < number < 100:
        number = str(number)
        ten = number[0]
        unit = number[1]
        return tens[ten] + "" + units[unit]
        
    elif 100 < number < 1000:
        number = str(number)
        hundred = number[0]
        ten = number[1]
        unit = number[2]
        ten_unit = number[1:3]
        
        # 处理十位部分是十到二十之间的数
        if int(ten_unit) < 20:
            return units[hundred]+" hundred"+" "+UtoT[ten_unit]
            
        else:
            return units[hundred]+" hundred"+" "+tens[ten]+" "+units[unit]
        
def main():
    while True:
        number = int(raw_input("Enter a number(1~1000)"))
        # 判断输入是否正确为正确的范围
        if number > 1000:
            print "The number must in 1~1000!"           
        else:
            break
            
    print englishNum(number)
        
if __name__ == "__main__":
    main()
    