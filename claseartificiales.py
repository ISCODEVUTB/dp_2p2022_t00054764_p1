from caracterizacion import caracterizacion
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
