'''
inFile = None
inStr = ''
'''
inFile = open("D:/firstpython/myData1.txt",'r', encoding='utf-8')
while True:
    inStr = inFile.readline()
    if inStr == '':
        break
    print(inStr, end='')

inFile.close()
