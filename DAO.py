import mysql.connector
from Carrera import Carrera

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="universidad"
)   
def wathcOne (nombre):
    mycursor = mydb.cursor()
    sql = "SELECT id FROM carrera WHERE nombre = %s"
    mycursor.execute(sql, (nombre,))
    return mycursor.fetchone()

def selectAll(): 
    mycursor = mydb.cursor()
    sql = "SELECT * FROM carrera"
    mycursor.execute(sql)
    return mycursor.fetchall()

def insert(carrera:Carrera): 
    mycursor = mydb.cursor()
    sql = "INSERT INTO carrera(nombre, nota_corte,duracion, area_conocimiento, modalidad ) VALUES(%s, %s,%s, %s, %s)"
    mycursor.execute(sql, (carrera.getNombre(), carrera.getNotaCorte(), carrera.getDuracion(), carrera.getAreaConocimineto(), carrera.getModalidad()))
    mydb.commit()
    return wathcOne(carrera.getNombre())
def update(campo, newValue, id):
    mycursor = mydb.cursor()
    sql = f"UPDATE carrera SET {campo} = %s WHERE id = %s"
    mycursor.execute(sql, (newValue, id))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def delete(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM carrera WHERE id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

