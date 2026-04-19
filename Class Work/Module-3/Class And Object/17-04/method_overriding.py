class master:
    def login(self,unm,pas):
        if unm=="admin"and pas==1234:
            print("Login Successfull")
        else:
            print("Eror")

class home(master):
    def login(self, unm, pas):
        return super().login(unm, pas)
    
class about(master):
    def login(self, unm, pas):
        return super().login(unm, pas)
