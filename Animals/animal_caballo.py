from modelo_animales import animales
class caballo(animales):
    
    def __init__(self,nombre, edad, habitat, dieta, tamaño, color, raza, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.raza = raza
        self.velocidad = velocidad
        
    def cabalgar(self):
        print(f"el caballo de raza {self.raza} puede cabalgar a una velocidad de {self.velocidad} km/h")
        
    def instintos(self):
        super().instintos()
        print("El caballo actúa siguiendo su instinto de manada y se mantiene alerta ante cualquier peligro")
        
    def mostrar_info(self):
        print(f"edad: {self.edad}")
        print(f"habitat: {self.habitat}")
        print(f"dieta: {self.dieta}")
        print(f"tamaño: {self.tamaño}")
        print(f"color:{self.color}")
        print(f"raza: {self.raza}")
        print(f"velocidad: {self.velocidad}")
        self.moverse()
        self.comunicar()
        self.reproducirse()
        self.alimentarse()
        self.adaptar()
        self.instintos()
        self.descansar()
        self.sueño()
        self.cabalgar()
        
        
    