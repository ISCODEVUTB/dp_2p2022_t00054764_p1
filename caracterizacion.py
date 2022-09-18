from abc import ABC,abstractmethod
class personajes():
    def __int__(self):
        pass
class caracterizacion(personajes):
    @abstractmethod
    def __init__(self,nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.poderes = []
        self.habilidades =[]
        self.debilidades = []
        self.personalidad= []
    
    @abstractmethod
    def atacar(self, objetivo):
        pass
    
    @abstractmethod
    def getStatus(self):
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")
    
    def subirDeNivel(self):
        self.nivel += 1
        
    def verInventario(self):
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)
            
    def verLiga(self):
        print(f"Liga de {self.nombre}")
        for objeto in self.liga:
            print(objeto)
    
    def verPoderes(self):
        print(f"Los poderes de: {self.nombre}")
        for objeto in self.poderes:
            print(objeto)
            
    def verHabilidades(self):
        print(f"Las habilidades de: {self.nombre}")
        for objeto in self.habilidades:
            print(objeto)
            
    def verDebilidades(self):
        print(f"Las debilidades de: {self.nombre}")
        for objeto in self.debilidades:
            print(objeto)
        
    def verPersonalidad(self):
        print(f"La personalidad del avatar: {self.nombre}")
        for objeto in self.personalidad:
            print(objeto)
        


