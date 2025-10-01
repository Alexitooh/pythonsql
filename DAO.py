import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="carrera"
)
class carreradao:

    def selectAll(): 
        mycursor = mydb.cursor()
        sql = "SELECT * FROM carrera"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for x in result:
            print(x)

    def insert(name): 
        mycursor = mydb.cursor()
        sql = "INSERT INTO carrera (nombre) VALUES(%s)"
        mycursor.execute(sql, (name))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def update(name, newName):
        mycursor = mydb.cursor()
        sql = "UPDATE carrera set nombre = %s WHERE nombre = %s"
        mycursor.execute(sql, (newName, name))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

    def delete(name):
        mycursor = mydb.cursor()
        sql = "DELETE FROM carrera WHERE nombre = %s"
        mycursor.execute(sql, (name,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

car = carreradao ()

car.insert ()
car.update()
car.delete()