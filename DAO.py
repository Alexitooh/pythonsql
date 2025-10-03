import mysql.connector
from mysql.connector import Error
from Carrera import Carrera

def myconn(usuario, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=usuario,
            password=password,
            database="universidad"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return None  

def wathcOne (mydb, nombre):
    mycursor = mydb.cursor()
    sql = "SELECT id FROM carrera WHERE nombre = %s"
    mycursor.execute(sql, (nombre,))
    return mycursor.fetchone()

def selectAll(mydb): 
    mycursor = mydb.cursor()
    sql = "SELECT * FROM carrera"
    mycursor.execute(sql)
    return mycursor.fetchall()

def insert(mydb, carrera:Carrera): 
    mycursor = mydb.cursor()
    sql = "INSERT INTO carrera(nombre, nota_corte,duracion, area_conocimiento, modalidad ) VALUES(%s, %s,%s, %s, %s)"
    mycursor.execute(sql, (carrera.getNombre(), carrera.getNotaCorte(), carrera.getDuracion(), carrera.getAreaConocimineto(), carrera.getModalidad()))
    mydb.commit()
    return wathcOne(mydb,carrera.getNombre())
def update(mydb, campo, newValue, id):
    mycursor = mydb.cursor()
    sql = f"UPDATE carrera SET {campo} = %s WHERE id = %s"
    mycursor.execute(sql, (newValue, id))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def delete(mydb, id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM carrera WHERE id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

