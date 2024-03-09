#9번
class Car : 
    color=''
    speed=0
    def __init__(self, color):
        self.color=color
        self.speed=0
    def upSpeed(self, up):
        self.speed+=up
    def downSpeed(self, down):
        self.speed-=down

car1=Car('빨강')
car2=Car('파랑')

car1.upSpeed(30)
car2.upSpeed(100)
car2.downSpeed(40)

print('차량1의 색상은',car1.color,'이고, 현재 속도는',car1.speed,'입니다.')
print('차량2의 색상은',car2.color,'이고, 현재 속도는',car2.speed,'입니다.')