
'''
#1
print('홍길동 선수 경기가 끝났습니다. 짝')

list=[]
a=0
for i in range(5):
    score=int(input('점수'))
    list.append(score)
    
for j in range(5):
    a+=list[j]
result=int(a)/len(list)
print(result)

#2
import random
list=[]
for i in range(10000):
    coma=random.choice(['가위','바위','보'])
    comb=random.choice(['가위','바위','보'])
    if coma =='가위':
        if comb=='가위':
            list.append('없음')
        if comb=='바위':
            list.append('b')
        if comb=='보':
            list.append('a')
    elif coma =='바위':
        if comb=='가위':
            list.append('a')
        if comb=='바위':
            list.append('없음')
        if comb=='보':
            list.append('b')
    elif coma =='보':
        if comb=='가위':
            list.append('b')
        if comb=='바위':
            list.append('a')
        if comb=='보':
            list.append('없음')

counta=list.count('a')
countb=list.count('b')
print('a가 이긴횟수:', counta,'b가 이긴횟수:', countb)

if counta>countb:print('a가 이김')
elif counta<countb:print('b가 이김')
else: ('비김')

#3
import random
list=[]
say=['삶이 있는 한 희마은 있다.','피할 수 없음 즐겨라']
today= random.randint
'''
#4
    #1
i=0
num=0
while i<1000:
    i+=1 #애초에 i+=3으로 하기
    if i%3==0:
        num+=i
print(num)

    #2
    #거꾸로 나오게도 해보기
i=0
while i<5:
    i+=1
    print('*'*i)
    
    #3
list =[70, 60, 55, 75, 95, 80, 80, 85, 100]
num=0
for i in range(len(list)-1): #그냥 list로 해도 됨
    num+=list[i] #i로 해도됨
print(num/len(list))
    
