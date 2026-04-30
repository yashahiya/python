class studinfo:
    def information(self):
        self.st_id=int(input("Enter Student Id:"))
        self.st_name=input("Enter Student Name:")
        
    def printdata(self):
        print("Student Id Is:",self.st_id)
        print("Student Name Is:",self.st_name)

print("Subit Details.....")
obj=studinfo()
obj.information()
obj.printdata()