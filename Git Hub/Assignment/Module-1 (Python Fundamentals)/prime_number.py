number=int(input("Enter Number : "))

if number > 1:
    for i in range(2,number):
        if number % i ==0:
            print("Not A Prime Number")
            break
    else:
        print("Number Is Prime.")
else:
    print("Not A Prime Number.")