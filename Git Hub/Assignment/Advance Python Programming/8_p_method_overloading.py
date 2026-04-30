class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    
obj=calculator()

print("Sum Of 2 Numbers:",obj.add(5,10))
print("Sum Of 3 Numbers:",obj.add(5,10,15))
