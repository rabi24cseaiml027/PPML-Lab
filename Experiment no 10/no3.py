class father:
    def skill1(self):
        print("Inside father's skill method")

class mother:
    def skill2(self):
        print("Inside mother's skill method")

class child(father,mother):
    def skill3(self):
        print("Inside child skill method")

ch = child()
ch.skill1()
ch.skill2()
ch.skill3()