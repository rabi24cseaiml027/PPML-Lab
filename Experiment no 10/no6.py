class obj:
    def __init__(self,a):
        self.a = a
    def __add__(self, other):
        return obj (self.a + other.a)
    def display(self):
        print("Sum is :",self.a)

a = obj(10)
b = obj(20)
c = a + b
c.display()