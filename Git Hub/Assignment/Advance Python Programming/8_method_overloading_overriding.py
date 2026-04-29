#Method Overloading

class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    
obj=calculator()

print("Sum Of 2 Numbers:",obj.add(5,10))
print("Sum Of 3 Numbers:",obj.add(5,10,15))


#Method Overriding

class parent:
    def show(self):
        print("This Is Parent Class...")

class child(parent):
    def show(self):
        print("This Is Child Class..(Overriding Method)")


obj=child()
obj.show()