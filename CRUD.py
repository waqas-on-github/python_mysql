
import mysql.connector   # importing db connector    

db= mysql.connector.connect(host="localhost" , user ="root" ,password ="waqasx@#")   # connecting with db 
print(db.connection_id)  # check connection 

cur =db.cursor() # creating cursor object for  opreation  in db 
cur.execute("use db1")

cur.execute("create database IF NOT EXISTS  db1") # executing instrucations  creating db  
students="CREATE TABLE  IF NOT EXISTS  students(name VARCHAR(30) ,email TEXT ,age int)" # creating tabel 
cur.execute(students)

i ="INSERT INTO students (name,email,age) VALUES (%s,%s,%s)"  # inserting data into tabel 
d=("waqas" ,'mrwaqas@gmail.com' ,25)  
cur.execute(i,d)
db.commit()

# inserting multiple recods in tabel 
ix ="INSERT INTO students (name,email,age) VALUES (%s,%s,%s)"  # inserting data into tabel 
dr=[("'usman'" ,"'me@gm'" ,26),("imran","mr@gm",28),("huzaifa","hzu@m",29 )]
cur.executemany(ix,dr)
db.commit() 



# reading data 

rd="select * from students"
cur.execute(rd)
result =cur.fetchall()
for r in result:
    print(r)

# update data 
cmd ="UPDATE students SET age=age+1 WHERE age >20"
cur.execute(cmd)
db.commit()


# delete data 
delete="DELETE FROM  students WHERE age >35"
cur.execute(delete)
db.commit()

