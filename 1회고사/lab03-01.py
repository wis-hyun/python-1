pound=int(input("무게를 입력해주세요, 파운드 단위로"))
kg=pound*0.453592
print(pound,'파운드는',('{0:.5f}'.format(kg)),'킬로그램입니다.')

kg=int(input("무게를 입력해주세요, 킬로그램 단위로"))
pound=kg*2.204623
print(kg,'킬로그램은',('{0:.5f}'.format(pound)),'파운드입니다.')
