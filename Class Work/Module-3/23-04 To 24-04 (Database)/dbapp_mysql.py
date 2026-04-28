import pymysql

try:
    db=pymysql.connect(host="localhost",user="root",password="",database="Python")
    print("Database Connected!")
except Exception as e:
    print(e)

cr=db.cursor()

#Table Create
"""create_table="create table studinfo(id integer primary key auto_increment,name text,city text)"

try:
    cr.execute(create_table)
    print("Table Created")
except Exception as e:
    print(e)"""

#Insert Data
"""insert_data="insert into studinfo(name,city)values('Yash','rajkot'),('Mohit','Suart')," \
"('Dhara','Ahemdabad'),('Vandna','Baroda')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Record Insrted..")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set name='yaaaa',city='rajjjj' where id=4"

try:
    cr.execute(update_data)
    db.commit()
    print("Recored Updated Successfull...")
except Exception as e:
    print(e)"""


#delete data

"""delete_data="delete from studinfo where id=4"

try:
    cr.execute(delete_data)
    db.commit()
    print("Record Deleted....")
except Exception as e:
    print(e)"""


#show data
show_data="select * from studinfo"

try:
    cr.execute(show_data)
    data=cr.fetchall()
    
    for i in data:
        print(i)
except Exception as e:
    print(e)
