class grandparent:
    def show_grandparent(self):
        print("This Is Grandparent Class...")

class parent(grandparent):
    def show_parent(self):
        print("This Is parent Class...")


class child(grandparent):
    def show_child(self):
        print("This Is Child Class...")

obj1=child()
obj2=parent()


obj1.show_grandparent()
obj2.show_grandparent()

obj2.show_parent()
obj1.show_child()