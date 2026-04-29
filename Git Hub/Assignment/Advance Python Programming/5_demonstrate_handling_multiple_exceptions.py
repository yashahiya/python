try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))

    result=a/b

    print("Result Is:",result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print("Some Other Error Occurred:",e)
    
finally:
    print("Program Finished.")