'''#1
a=int(input('입력'))
i=0
result=1
for i in range(a):
    result+=result*i
print(result)

#2
i, hap=0,0
for i in range(1000,2001,2):
    hap+=i
print(hap)

#3
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')

#4
hap,num1,num2=0,0,0
while True:
    num1= int(input('숫자1'))
    if num1==0: break
    num2=int(input('숫자2'))
    
    hap=num1+num2
    print(hap)
#5
import random
count=0
dic1, dic2, dic3=0,0,0
while True:
    count+=1
    dic1=random.randint(1,6)
    dic2=random.randint(1,6)
    dic3=random.randint(1,6)
    if (dic1==dic2)and(dic2==dic3): break

print(dic1,dic2,dic3, f'같은 숫자가 나오기까지 {count}번 던졌습니다.')
'''
#6
import random
success=0
for i in range(1, 11):
    computer=random.randint(1,20)
    person=int(input('1~20중 한가지 숫자를 입력하세요=>'))
    if computer==person:
        success=1
        print('통과')
        break
    else:
        if i<10:
            print('다시 도전하세요') 
        continue
if success==0:
    print('실패')


