#8번
outFile = None
inFile = None
outStr = ""
inStr = ""
num = 1

inFile = open("D:/FirstPython/normal.txt", "r", encoding="UTF-8")
outFile = open("D:/FirstPython/normal_line.txt", "w")

while True :
    inStr = inFile.readline()
    if inStr == "" :
        break
    outFile.writelines(str(num) + " 행 : " + str(inStr))
    num += 1

inFile.close()
outFile.close()