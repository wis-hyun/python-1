class Rabbit:
    shape=''
    xPos=0
    yPos=0

    def __init__(self, value):
        self.shape=value
    def goto(self, x, y):
        self.xPos=x
        self.yPos=y

rabbit1 = Rabbit('원')
print('rabbit의 모양 : ', rabbit1.shape)
rabbit2 = Rabbit('삼각형')
print('rabbit의 모양 : ', rabbit2.shape)
rabbit3 = Rabbit('토끼')
print('rabbit의 모양 : ', rabbit3.shape)