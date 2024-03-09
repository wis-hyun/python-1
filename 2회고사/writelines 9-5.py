#1
outFile = None
outStr = ''

outFile = open("D:/firstpython/myData2-1.txt",'w')

outStr = '안녕하세요'
outFile.writelines(outStr + '\n')

outStr = '반갑습니다'
outFile.writelines(outStr + '\n')

outStr = '자주만나요'
outFile.writelines(outStr + '\n')

outFile.close()
print('mydata2.txt파일이 저장됨')

#2
outFile = None
outStr = ''

outFile = open("D:/firstpython/myData2-2.txt",'w')

while True:
    outStr = input('내용입력 ==>')
    if outStr != '':
        outFile.writelines(outStr + '\n')
    else: break

outFile.close()
print('mydata2.txt파일이 써짐')
