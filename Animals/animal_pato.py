from modelo_animales import animales
class pato(animales):
   
    
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.velocidad = velocidad
        
    def volar(self):
        print(f"el pato despega y vuela con una velocidad promedio de {self.velocidad} km/h")
        
    def nadar(self):
        print("el pato puede nadar")
        
    def instintos(self):
        super().instintos()
        print("El pato sigue su instinto acuático y nada rápido para alejarse del peligro")
        
    def mostrar_info(self):
        print(f"edad: {self.edad}")
        print(f"habitat: {self.habitat}")
        print(f"dieta: {self.dieta}")
        print(f"tamaño: {self.tamaño}")
        print(f"color:{self.color}")
        print(f"velocidad: {self.velocidad}")
        self.moverse()
        self.comunicar()
        self.reproducirse()
        self.alimentarse()
        self.adaptar()
        self.instintos()
        self.descansar()
        self.sueño()
        self.volar()
        self.nadar()
        