import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="universidad"
)
def selectAll(): 
    mycursor = mydb.cursor()
    sql = "SELECT * FROM materias"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        print(x)
def insert(name): 
    if name == "":
        name = input("Has de ingresar el nombre de la materia: ")
        return
    mycursor = mydb.cursor()
    sql = "INSERT INTO materias (nombre) VALUES(%s)"
    mycursor.execute(sql, (name,))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
def update(name, newName):
    mycursor = mydb.cursor()
    sql = "UPDATE materias set nombre = %s WHERE nombre = %s"
    mycursor.execute(sql, (newName, name))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def delete(name):
    mycursor = mydb.cursor()
    sql = "DELETE FROM materias WHERE nombre = %s"
    mycursor.execute(sql, (name,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")