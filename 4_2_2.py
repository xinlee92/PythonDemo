#homework_4_2_2
#从1加到end的for循环。变量end的值由键盘输入

s=0
end=int(input('Please input the value of end:'))

for i in range(1,end+1):
    s+=i
print('The result is '+str(s))
    
