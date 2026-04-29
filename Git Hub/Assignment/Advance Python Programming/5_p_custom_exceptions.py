class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_number(num):
    if num < 0:
        # Raise custom exception
        raise MyCustomError("Number should not be negative!")
    else:
        print("Valid number:", num)

try:
    n = int(input("Enter a number: "))
    check_number(n)

except MyCustomError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Invalid input! Please enter an integer.")