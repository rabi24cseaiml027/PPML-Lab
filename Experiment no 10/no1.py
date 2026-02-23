class parent:
    def parent_method(self):
        print("Properties of parent")

class child(parent):
    pass

ch = child()
ch.parent_method()
