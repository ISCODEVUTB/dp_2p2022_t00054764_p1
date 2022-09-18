from caracterizacion import caracterizacion
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