class parent:
    def show(self):
        print("This Is Parent Class...")

class child(parent):
    def show(self):
        print("This Is Child Class..(Overriding Method)")


obj=child()
obj.show()