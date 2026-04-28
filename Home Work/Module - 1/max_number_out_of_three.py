num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
num3=int(input("Enter Third Number : "))

if num1>num2 :
    if num1>num3 :
        print("This Is Max Number : ",num1)
elif num2>num3 :
    if num2>num1 :
        print("This Is Max Number : ",num2)
else :
    print("This Is Max Number : ",num3)