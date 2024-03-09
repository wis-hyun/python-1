#클래스 선언
class Line:
    length = 0

    def __init__(self, length):
        self.length = length
        print(self.length,'길이의 선이 생성되었습니다')
    def __del__(self):
        print(self.length,'길이의 선이 제거되었습니다.')
    def __add__(self, other):
        return self.length + other.length
    def __lt__(self, other):
        return self.length < other.length
    def __eq__(self, other):
        return self.length == other.length
    
#메인코드부분
line1=Line(10)
line2=Line(5)
print('두선의 합 : ', line1 + line2)
if line1 < line2:
    print("선2가 더 깁니다.")
    del(line1)
elif line1 == line2:
    print("두선의 길이가 같습니다.")
else: 
    print("선1이 더 깁니다.")
    del(line2)
