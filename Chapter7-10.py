class Calculator:
    def __init__(self, value):
        self.value = value

    def sum(self):
        result = 0
        for i in self.value:
            result += i
        return result
    
    def avg(self):
        total = self.sum()
        avg = total / int(len(self.value))
        return avg
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())