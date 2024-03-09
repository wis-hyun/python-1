#함수 정의 부분
def checkPassword(pwd):
    if len(pwd) < 8:
        return False
    if pwd.isalnum():
        return True
    else:
        return False

#전역변수 선언 부분
password = ''

#메인코드 부분
password = input("새로운 비밀번호를 입력하세요 (8자리 이상으로)==>")
if checkPassword(password):
    print("올바른 비밀번호가 생성되었어요!")
else: print("오류! 비밀번호가 맞지 않습니다.")
