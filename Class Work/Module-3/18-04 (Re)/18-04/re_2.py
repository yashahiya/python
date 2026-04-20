import re

mystr="This Is Python!"

x=re.match("This",mystr)
print(x)

if x:
    print("Match done")

else:
    print("Eror")