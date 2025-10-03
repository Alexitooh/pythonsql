from Carrera import Carrera
import DAO as dao

mydb = None
while mydb == None:
    usuario = input("Pon el nombre de usuario: ")
    contraseña = input("Pon el nombre de contraseña: ")
    print("Usuario o contraseña no correcto: \n")
mydb = dao.myconn(usuario, contraseña)

def init(mydb):
    results = dao.selectAll(mydb)
    carreras = []
    for x in results:
        carrera = Carrera(x[0], x[1], x[2], x[3], x[4], x[5])
        carreras.append(carrera)
    return carreras

def selectAll(carreras):
    for res in carreras: 
        print(res.__str__())
def menu(mydb):
    validacio = True
    carreras = init(mydb)
    while validacio:
        option = int(input("Selecciona una opcion: \n1. Crear Carrera\n2. Mostrar Carrera\n3. Actualizar Carrera\n4. Elminar Carrera\n5. Salir\n    "))
        if option == 1:
            name = input("Pon el nombre de la Carrera: ")
            nota_corte = input("Indica la de nota corte de la carrera: ")
            duracion = input("Indica la duracion de la carrera: ")
            area_conocimiento = input("Indica el area de conocimiento: ")
            modalidad = input("Indica la modalidad: ")
            carrera = Carrera(1,name, duracion, nota_corte, area_conocimiento, modalidad)
            id =dao.insert(mydb,carrera)
            carrera.setId(id[0])
            carreras.append(carrera)
        elif option == 2:
            selectAll(carreras)
        elif option == 3:
            campos = ["nombre", "nota_corte","duracion","area_conocimiento","modalidad "]
            campo = int(input("Que campo quieres cambiar? \n1. Nombre\n2. Duracion\n3. Nota de corte\n4. Area de conocimiento\n5. Modalida\n "))
            selectAll(carreras)
            id= int(input("Indica la id: "))
            newValue = input("Pon el nuevo valor: ")
            carrera = dao.update(mydb,campos[campo-1],newValue, id)
            carreras = selectAll(carreras)
        elif option == 4:
            selectAll(carreras)
            id = int(input("Pon la id del cual quieres eliminar: "))
            dao.delete(mydb,id)
            for x in carreras: 
                if x.getId() == id:
                    carreras.remove(x)

            
        elif option == 5:
            validacio = False
        else:
            print("Valor incorrecto")
menu(mydb)
