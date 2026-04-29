try:
    filename=input("Enter File Name:")
    file=open(filename,"r")
    content=file.read()
    print("File Content:\n",content)
    file.close()

    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))

    result=num1/num2

    print("Result Is:",result)

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program execution completed.")