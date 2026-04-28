n=int(input("How many key you wants : "))
data=[]

for i in range(n) :
    id=input("enter your id : ")
    name=input("enter Your name : ")
    

    student={
        'key':id,
        'value':name,
    }
    data.append(student) 
   
        
print(data)