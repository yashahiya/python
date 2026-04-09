file=open("new.txt","a")

number=int(input("Enter Number Of Students: "))

for i in range(number): 
    id=input("Enter Yout Id : ")
    name=input("Enter Your Name : ")
    city=input("ENter Your City : ")
    file.write(f"\nid:{id}\n name:{name}\ncity:{city}")

"""file.write(id)
file.write(name)
file.write(city)"""


