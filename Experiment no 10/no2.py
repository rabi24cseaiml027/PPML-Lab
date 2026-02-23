class grandparent:
    def gp_property(self):
        print("Inside grantparent method.")

class parent(grandparent):
    def business(self):
        print("Inside Parent business method.")

class child(parent):
    def education(self):
        print("Inside child education method.")

ch = child()
ch.gp_property()
ch.business()
ch.education()