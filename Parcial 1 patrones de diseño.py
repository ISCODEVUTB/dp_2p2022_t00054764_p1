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
        
class Humano(caracterizacion):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.armas = 60
        self.inventario = ["Flecha", "Arco","Daga","Espada"]
        self.liga = ["Los normales"]
        self.poderes = ["Maestro en armadura pesada","daga","espada a una mano"]
        self.habilidades = ["Es capaz de correr a altas velocidades","Conquista"]
        self.debilidades = ["Su nivel de energía disminuye cada vez que corre a una velocidad alta","No es inmortal"]
        self.personalidad = ["Carismático","Gruñón", "fuerza extrema"]
              
    def getStatus(self):
        print(f"Clase Humano")
        super().getStatus()
        
    def atacar(self, objetivo):
        objetivo.vida -= self.armas*0.6
        print(f"Vida del objetivo es: {objetivo.vida}")

class SuperHumano(caracterizacion):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 250
        self.fuerza = 90
        self.inventario = ["Poción de vida", "Espada","Extra"]
        self.liga = ["Los grandes"]
        self.poderes = ["Es capaz de convertirse en un doble de su tamaño","Puede tranformarse en cualquier objeto"]
        self.habilidades = ["Super fuerza","Capaz de resucitarse el mismo con la poción extra","Volar","Rayos X"]
        self.debilidades = ["Debido a su tamaño no puede correr rápido","Los rayos x no funcionan en la oscuridad"]
        self.personalidad = ["Enojo","ira", "creatividad"]
    
    def getStatus(self):
        print(f"Clase SuperHumano")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.8
        print(f"El objetivo se ha quedado con {objetivo.vida} puntos de vida")
              
class Artificiales(caracterizacion):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 300
        self.invisibilidad = 95
        self.inventario = ["Poción de curación","Invisibilidad extra"]
        self.liga = ["Las inteligencias"]
        self.poderes = ["Maestro de la invidibilidad", "Puede hacer invisible a cualquier personaje con su invisibilidad extra"]
        self.habilidades = ["Se hace invisible en cualquier momento y lugar","Solo puede usar la poción una vez"]
        self.debilidades = ["Solo puede hacerse invisible cuando su energía cargue completamente","No puedo hacer invisible al mismo personaje dos veces"]
        self.personalidad = ["Amable","cariñoso", "entusiasta"]

    def getStatus(self):
        print(f"Clase Artificial")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.invisibilidad*0.9
        print(f"El objetivo se ha quedado con {objetivo.vida} puntos de vida")

class Aliens(caracterizacion):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 500
        self.telequinesis = 90
        self.inventario =["Nave pegable","Armas ultima tecnología"]
        self.liga = ["Los extranjeros"]
        self.poderes = ["Maestro de la telequinesis","Maestro de armas"]
        self.habilidades = ["Es capaz de leer las mentes de los demás y dejarlos en un trance por unos minutos","Sabe manejar las mejores armas"]
        self.debilidades = ["Su nivel de poder disminuye con cada persona que agarra","No puede volar"]
        self.personalidad = ["Vengativo","Poderoso"]
        
    def getStatus(self):
        print(f"Clase Aliens")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.telequinesis*0.4
        print(f"El objetivo se ha quedado con {objetivo.vida} puntos de vida")
    
##Pruebas
humano = Humano("Kaladin")
humano.getStatus()
humano.verInventario()
humano.verLiga()
humano.verPoderes()
humano.verHabilidades()
humano.verDebilidades()
humano.verPersonalidad()
print("\n")

superhumano = SuperHumano("Yuno")
superhumano.getStatus()
superhumano.verInventario()
superhumano.verPoderes()
superhumano.verHabilidades()
superhumano.verDebilidades()
superhumano.verPersonalidad()
print("\n")

artificiales = Artificiales('Innova')
artificiales.getStatus()
artificiales.verInventario()
artificiales.verPoderes()
artificiales.verHabilidades()
artificiales.verDebilidades()
artificiales.verPersonalidad()
print("\n")

aliens = Aliens('Yoyo')
aliens.getStatus()
aliens.verInventario()
aliens.verPoderes()
aliens.verHabilidades()
aliens.verDebilidades()
aliens.verPersonalidad()
print("\n")
humano.atacar(aliens)
superhumano.atacar(artificiales)
artificiales.atacar(humano)
aliens.atacar(superhumano)