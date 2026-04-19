class AccDetails:
    ac_num:int
    ac_name:str
    ac_type:str
    ac_balance:0

    def getdata(self):
        self.ac_num=input("Enter ACC Number: ")
        self.ac_name=input("Enter ACC Name:")
        self.ac_type=input("Enter Acc Type: ")

class Deposit(AccDetails):
    Dep_amt:int

    def depositdata(self):
        self.Dep_amt=input("Enter Deposite Amount: ")
       
        
    

class Withdrawal(Deposit):
    with_amt:int

    def withdrawdata(self):
        self.with_amt=input("Enter Withdral Amount:")
        """if(self.ac_balance<self.with_amt):
            print("Balance Not Available....")
        else:
            print("Withdrawal Successfull..")
            self.ac_balance-=self.withdrawdata
"""
class Statement(Withdrawal):

    def statementdata(self):
        print("Your acc Number Is : ",self.ac_num)
        print("Acc Holder Name Is : ",self.ac_name)
        print("Your Acc Type Is : ",self.ac_type)
        print("Your Balance Is : ",self.ac_balance)


bnk=Statement()
bnk.getdata()
bnk.depositdata()
bnk.withdrawdata()
bnk.statementdata()


