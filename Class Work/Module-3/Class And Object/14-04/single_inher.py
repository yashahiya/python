class father:
    car:int
    bal:int
    
    def getdata(self):
        self.car=input("Enter Car Details:")
        self.bal=input("Enter Bank Balance:")

class son(father):
    def printdata(self):
        print("car:",self.car)
        print("Bank Balance:",self.bal)


sn=son()
sn.getdata()
sn.printdata()
