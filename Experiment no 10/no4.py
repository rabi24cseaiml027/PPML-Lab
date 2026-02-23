class parent:
    def show(self):
        print("Inside parent show mehtod.")

class child(parent):
    def show(self):
        print("Inside child show method.")

ch = child()
ch.show()