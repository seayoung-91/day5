class FourCal:
   def __init__(self, first, second):
       self.first = first
       self.second = second
   def setdata(self, first, second):
       self.first = first
       self.second = second
   def add(self):
       result = self.first + self.second
       return result
   def mul(self):
       result = self.first * self.second
       return result
   def sub(self):
       result = self.first - self.second
       return result
   def div(self):
       result = self.first / self.second
       return result

class MoreFourCal(FourCal):
    def expr(self, first, second):
        self.first = first
        self.second = second
        return self.first ** self.second

    def add(self):
        result = self.first + self.second + 10000
        return result

c1=FourCal(1,2)
mfc=MoreFourCal(1,2)
print(c1.add())
print(mfc.add())