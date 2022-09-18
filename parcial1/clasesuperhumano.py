from caracterizacion import caracterizacion
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