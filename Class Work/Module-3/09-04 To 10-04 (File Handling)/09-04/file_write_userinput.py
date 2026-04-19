file=open("test.txt","w")

id=input("Enter An Id : ")
name=input("Enter Your Name : ")
city=input("Enter Your City : ")

"""file.write(id)
file.write(name)
file.write(city)"""

file.write(f"Id : {id}\nName:{name}\nCity:{city}\n")
