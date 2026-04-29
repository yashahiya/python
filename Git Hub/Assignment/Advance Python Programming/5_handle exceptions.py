try:
    num1=float(input("Enter First Number:"))
    num2=float(input("Enter Second Number:"))

    result=num1/num2

    print("Result Is:",result)

except ZeroDivisionError:
    print("Error: Cannot Divide By Zero.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

finally:
    print("Program Ended.")