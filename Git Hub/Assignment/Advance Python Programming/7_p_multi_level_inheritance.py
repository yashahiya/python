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