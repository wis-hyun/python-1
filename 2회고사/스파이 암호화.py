secureFile = None
inStr, secure = '',''
secureFile=open("D:/firstpython/secure.txt",'w',encoding='utf-8')

while True:
    inStr = input('스파이에게 전달할 메세지 ==>')
    if inStr == "" :
        break
    for ch in inStr:
        num = ord(ch)
        num += 100
        secure += chr(num)
    secureFile.writelines(secure)

secureFile.close()
print("---secure.txt 암호화완료---")
