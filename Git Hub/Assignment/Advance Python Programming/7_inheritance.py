#Single Inheritance

class parent:
    def show(self):
        print("This Is Parent Class...")

class child(parent):
    def display(self):
        print("This Is Child Class....")

obj=child()
obj.show()
obj.display()
print("--------------------------------------------")



#Multiple Inheritance

class father:
    def show_father(self):
        print("This Is Father Class....")

class mother:
    def show_mother(self):
        print("This Is Mother Class....")

class child(father,mother):
    def show_child(self):
        print("This is Child Class....")


ob=child()
ob.show_father()
ob.show_mother()
ob.show_child
print("--------------------------------------------")



#Multilevel Inheritance
class grandparent:
    def show_grandparent(self):
        print("This Is Grandparent Class...")

class parent(grandparent):
    def show_parent(self):
        print("This Is parent Class...")


class child(parent):
    def show_child(self):
        print("This Is Child Class...")

obj1=child()
obj1.show_grandparent()
obj1.show_parent()
obj1.show_child()