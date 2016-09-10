#homework_4_2_1
#判断数字能否被2和3整除，输出结果

num=int(input('Please input a number:'))

if num%2==0 and num%3==0:
    print(str(num)+'能被2和3整除')

elif num%2==0:
    print(str(num)+'能被2整除，不能被3整除')
    
elif num%3==0:
    print(str(num)+'能被3整除，不能被2整除')

else:
    print(str(num)+'不能被2或3整除')
