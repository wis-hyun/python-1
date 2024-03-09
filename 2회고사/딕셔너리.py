#1
'''
singer={}
singer['이름']='트와이스'
singer['구성원 수']=9
singer['데뷰']='서바이벌 식스틴'
singer['대표곡']='cry for me'

for i in singer.keys():
    print(i,'==>', singer[i])

'''
#2
'''
store={}
while True:
    obj=input('입력물품 :')
    if obj=='z': break
    number=input('재고량 :')
    store[obj]=number
print('====재고량 확인=====')

while True:
    find=input('찾을 물품 : ')
    if find in store:
        print(find, store[find])
    else: print('없습니다.')
    if find=='': break
'''
#
def fac(n):
    result=1
    for i in range(1,n+1,1):
        result*=n
    return result
    if n==0: return 1

    
