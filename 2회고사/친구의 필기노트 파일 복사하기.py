inFile, outFile = None, None
inStr = ''

inFile = open('D:/firstpython/myData1.txt','r', encoding='utf-8')
outFile = open('D:/firstpython/myData1_copy.txt','w', encoding='utf-8')

inList = inFile.readlines()
for inStr in inList:
    outFile.writelines(inStr)

inFile.close()
outFile.close()
print('mydata1이 mydata1_copy에 복사되었습니다!!!')
