class t1:
    def fun1(self):
        print("Inside t1 class")
        
class t2(t1):
    obj = t1()
    obj.fun1()