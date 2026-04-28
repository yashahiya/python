import re

'''username=input("Enter An Useranme:")

unm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,username)

if x:
    print("Username Is Valid")
else:
    print("Eror!Invalid Username")

'''


email=input("Enter Your Email:")

email_patern="[a-z]+[@]"

x=re.findall(email_patern,email)

if x:
    print("Email Is Valid")

else:
    print("Please Enter Valid Email Id ")