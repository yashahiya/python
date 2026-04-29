try:
    num1=float(input("Enter First Number:"))
    operator = input("Enter operator (+, -, *, /): ")
    num2=float(input("Enter Second Number:"))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2   # May raise ZeroDivisionError
    else:
        print("Invalid operator!")

    print("Result:",result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

except Exception as e:
    print("Unexpected error:", e)
