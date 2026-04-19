import datetime
import random

n=int(input("How Many student You Want too add : "))

for i in range(n):
    date=datetime.datetime.now()
    id=(random.randint(00,99))
    name=input("Enter Your Name : ")
    city=input("Enter Your City : ")
    file=open("Data.txt","a")
    file.write(f"date&time={date}\nid = {id}\nname={name}\ncity={city}\n--------------\n")
  

