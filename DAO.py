import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="carrera"
)   
def selectAll(): 
    mycursor = mydb.cursor()
    sql = "SELECT * FROM carrera"
    mycursor.execute(sql)
    return mycursor.fetchall()

def insert(carrera:Carrera): 
    mycursor = mydb.cursor()
    sql = "INSERT INTO carrera(nombre,duracion, nota_corte, area_conocimineto, modalidad ) VALUES(%s, %s,%s, %s, %s)"
    mycursor.execute(sql, (carrera.getNombre(), carrera.getDuracion(), carrera.getNotaCorte(), carrera.getAreaConocimineto(), carrera.getModalidad()))
    mydb.commit()
    mycursor2 = mydb.cursor("SELECT id from carrera where nombre = %s", (carrera.getNombre(),))
    return mycursor2.fetchone()

def update(name, campo, newName):
    mycursor = mydb.cursor()
    sql = "UPDATE carrera set %s = %s WHERE nombre = %s"
    mycursor.execute(sql, (campo, newName, name))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def delete(name):
    mycursor = mydb.cursor()
    sql = "DELETE FROM carrera WHERE nombre = %s"
    mycursor.execute(sql, (name,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def wathcOne (nombre):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM carrera"
    mycursor.execute(sql)
    return mycursor.fetchall()