#1
inFile=None
inStr = ''

inFile=open("D:/FirstPython/2회고사/myDatal.txt","r", encoding="UTF-8")

inStr=inFile.readline()
print(inStr, end='')
inStr=inFile.readline()
print(inStr, end='')
inStr=inFile.readline()
print(inStr, end='')

#2
inFile = None
inStr = ''

inFile = open("D:/firstpython/myData1.txt",'r', encoding='utf-8')
while True:
    inStr = inFile.readline()
    if inStr == '':
        break
    print(inStr, end='')

inFile.close()
