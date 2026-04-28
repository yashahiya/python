def add(a,b):
    print("Sum Is : ",a+b)

def sub(a,b):
    print("Sub Is : ",a-b)

def multi(a,b):
    print("multi Is : ",a*b)

def div(a,b):
    print("Div Is : ",a/b)


x=int(input("Enter First Number : "))
y=int(input("Enter Second Number : "))

choice=int(input("Press 1 For Addition , Press 2 For Substraction , Press 3 For Multiplication , Press 4 For Division : ")
)
if choice == 1 :
    add(x,y)
elif choice == 2:
    sub(x,y)
elif choice ==3:
    multi(x,y)
elif choice==4:
    div(x,y)

else:
    print("Invalid Choice.")