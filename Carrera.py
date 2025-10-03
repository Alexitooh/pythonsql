class Carrera:
    def __init__(self, id, nombre, duracion, nota_corte, area_conocimiento, modalidad): 
        self.id = id
        self.nombre = nombre
        self.duracion = duracion
        self.nota_corte = nota_corte
        self.area_conocimiento = area_conocimiento
        self.modalidad = modalidad
    
    def getId(self): 
        return self.id
    def getNombre(self):
        return self.nombre
    def getDuracion(self):
        return self.duracion
    def getNotaCorte(self):
        return self.nota_corte
    def getAreaConocimineto(self):
        return self.area_conocimiento
    def getModalidad(self): 
        return self.modalidad
    
    def setId(self, id):
        self.id = id
    def setNombre(self,nombre):
        self.nombre = nombre
    def setDuracion(self,duracion):
        self.duracion = duracion
    def setNotaCorte(self, nota_corte):
        self.nota_corte = nota_corte
    def setAreaConocimiento(self, area_conocimiento):
        self.area_conocimiento = area_conocimiento
    def setModalidad(self, modalidad): 
        self.modalidad = modalidad
    
    def __str__(self):
        return f"[{self.id}] ===> Nombre: {self.nombre} => Duracion: {self.duracion} => Nota de corte: {self.nota_corte} => Area de conocimiento: {self.area_conocimiento} => Modalidad: {self.modalidad}"