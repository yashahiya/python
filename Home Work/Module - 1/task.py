name=input("enter your name : ")
if name.isalpha():
    email=input("Enter Your Email : ")
else :
    print("Name should be in alphabet only...")

if email.islower() :
    password=input("Enter Your Password : ")
else :
        print("Enter Valid Email...")

if len(password) <8 :
     print("Enter Valid Password")
else :
     c_password=input("Enter Confirm Password : ")
if password == c_password :
     mobile_num=input("Enter Your Mobile Number : ")
else : 
     print("Password Does Not Match")
if len(mobile_num) ==10 and mobile_num.isdigit() :
     print("Login Successfully....")
else : 
     print("Enter Valid Mobile Number")