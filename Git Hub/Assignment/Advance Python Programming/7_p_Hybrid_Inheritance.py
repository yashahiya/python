class a:
    def showA(self):
        print("Class A")

class b(a):
    def showB(self):
        print("Class B")

class c(a):
    def showC(self):
        print("Class C")

class d(b,c):
    def showD(self):
        print("Class D")

obj=d()

obj.showA()
obj.showB()
obj.showC()
obj.showD()