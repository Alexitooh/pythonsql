from Carrera import Carrera

def menu():
    option = int(input("Selecciona una opcion: \n1. Crear Carrera\n2. Mostrar Carrera\n3. Actualizar Carrera\n4. Elminar Carrera\n5. Salir"))
    while option != 5:
        if option == 1:
            name = input("Pon el nombre de la Carrera: ")
            duracion = input("Indica la duracion de la carrera:")
            nota_corte = input("Indica la de nota corte de la carrera")
            area_conocimiento = input("Indica el area de conocimiento")
            modalidad = input("Indica la modalidad")
            carrera = Carrera(name, duracion, nota_corte, area_conocimiento, modalidad)
        elif option == 2:
            delete(input("Ingrese el nombre de la materia a eliminar: "))
        elif option == 3:
            campo = int(input("Que campo quieres cambiar? \n1. Nombre\n2. Duracion\n3. Nota de corte\n4. Area de conocimiento\n5. Modalidad"))
                

        elif option == 4:
            name = input("Ingrese el nombre de la materia a buscar: ")
            selectOne(name)
        elif option == 5:
            name = input("Ingrese el nombre de la materia a actualizar: ")
            newName = input("Ingrese el nuevo nombre de la materia: ")
            update(name, newName)