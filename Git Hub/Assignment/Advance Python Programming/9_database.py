import sqlite3

try:
    db=sqlite3.connect("Testdb.db")
    print("Database Connected")
except Exception as e:
    print(e)

#table create
"""create_table="create table studinfo(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(create_table)
    print("Table Created....")
except Exception as e:
    print(e)"""

#insert data
"""insert_data="insert into studinfo(name,city)values('yash','Rajkot'),('Mohit','Rajkot')"

try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted")
except Exception as e:
    print(e)"""

#insert data through user input

"""n=int(input("Enter Number Of Students:"))
for i in range(n):
    name=input("Enter Your Name:")
    city=input("Enter Your City:")
    insert_data=f"insert into studinfo(name,city)values('{name}','{city}')"

    try:
        db.execute(insert_data)
        db.commit()
        print("Record Inserted....")
    except Exception as e:
        print(e)"""

#update data
"""update_data="update studinfo set name='ahiya',city='Ahemdabad' where id=3"

try:
    db.execute(update_data)
    db.commit()
    print("Record Updated...")
except Exception as e:
    print(e)"""

#delete data
"""delete_data="delete from studinfo where id=3"

try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted....")
except Exception as e:
    print(e)"""

#show data
cr=db.cursor()
show_data="select * from studinfo"

try:
    cr.execute(show_data)
    data=cr.fetchall()      #fetch all record
    for i in data:
        print(i)
except Exception as e:
    print(e)