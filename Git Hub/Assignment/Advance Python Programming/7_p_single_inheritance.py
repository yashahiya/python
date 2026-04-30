class parent:
    def show(self):
        print("This Is Parent Class...")

class child(parent):
    def display(self):
        print("This Is Child Class....")

obj=child()
obj.show()
obj.display()