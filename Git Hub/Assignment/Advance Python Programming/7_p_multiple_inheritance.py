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