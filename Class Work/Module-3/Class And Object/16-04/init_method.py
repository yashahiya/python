import random

class bank():
    def __init__(self):
        print("This Is Defult Init Method")
        otp=random.randint(1111,9999)
        print("Your Otp Is:",otp)


st=bank()