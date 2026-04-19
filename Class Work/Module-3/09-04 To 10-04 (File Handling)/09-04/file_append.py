
id=input("Enter an Id : ")
name=input("Enter Your Name : ")
city=input("ENter Your City : ")
file=open("new.txt","a")
file.write(f"Id:{id}\nName:{name}\ncity:{city}\n")