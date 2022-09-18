from caracterizacion import caracterizacion
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
    