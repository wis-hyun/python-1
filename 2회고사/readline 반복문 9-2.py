#1
inFile = None
inList = []

inFile = open("D:/firstpython/myData1.txt",'r', encoding='utf-8')

inList = inFile.readlines()
print(inList)

inFile.close()

#2
inFile = None
inList = []

inFile = open("D:/firstpython/myData1.txt",'r', encoding='utf-8')

inList = inFile.readlines()
for inStr in inList:
    print(inStr, end='')

inFile.close()
