"""import re

#student Registration System

stnm=input("Enter Your Name:")
stnm_pattern="[A-Z]+[a-z]"

name=re.findall(stnm_pattern,stnm)
print(name)

if name:
    stemail=input("Enter An Email ID:")
    stemail_pattern="[a-z]+[.]"
    email=re.findall(stemail_pattern,stemail)
    if email:
        stnumber:int
        stnumber=input("Enter Mobile Number:")
        stmobilenumber_pattern="[0-9]"
        mo_no=re.findall(stmobilenumber_pattern,stnumber)
        if mo_no:
            stpass=input("Enter Your Password:")
            stpass_pattern="[A-Z]+[a-z]+[0-9]"
        else:
            print("Enter valid Mobile Number........")
    else :
        print("Enter Valid EmailID........")
else:
    print("Enter Valid Name........")"""

import re
stpass=input("Enter Your Password:")
stpass_pattern="[A-Z]+[a-z]+[0-9]+[/W]"

pas=re.match(stpass_pattern,stpass)
print(pas)

if pas:
    print("Valid")
else:
    print("not Valid")











