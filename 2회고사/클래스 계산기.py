class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second= second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result =self.fist+self.secornd
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

a = Fourcal(4,2)
b= Fourcal(5,10)
a.add()
b.div()

