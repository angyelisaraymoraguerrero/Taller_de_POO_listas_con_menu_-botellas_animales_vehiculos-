from modelo_animales import animales
class hipopotamo(animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, velocidad, peso,):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.velocidad = velocidad
        self.peso=peso
        
    def instintos(self):
        super().instintos()
        print("El hipopótamo muestra su instinto territorial permaneciendo en el agua y defendiendo su espacio")
        
    def deducir_velocidad(self):
        print(f"el peso aproximado de un hipopotamo {self.peso} les permite correr a una velocidad aproximada de {self.velocidad} km/h")
        
    def mostrar_info(self):
        print(f"edad: {self.edad}")
        print(f"habitat: {self.habitat}")
        print(f"dieta: {self.dieta}")
        print(f"tamaño: {self.tamaño}")
        print(f"color:{self.color}")
        print(f"velocidad: {self.velocidad}")
        print(f"peso:{self.peso}")
        self.moverse()
        self.comunicar()
        self.reproducirse()
        self.alimentarse()
        self.adaptar()
        self.instintos()
        self.descansar()
        self.sueño()
        self.deducir_velocidad()
        