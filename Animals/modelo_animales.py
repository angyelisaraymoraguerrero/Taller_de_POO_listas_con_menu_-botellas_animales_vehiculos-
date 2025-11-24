class animales:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color
        
    def moverse(self):
        print(f"el {self.nombre} se mueve con facilidad entre su habitat {self.habitat}")
        
    def comunicar(self):
        print(f"el {self.nombre} se comunica")
        
    def reproducirse(self):
        print(f"el {self.nombre} esta en su proceso de reproduccion")
        
    def alimentarse(self):
        print(f"el {self.nombre} se alimenta de {self.dieta}")
        
    def adaptar(self):
        print(f"el {self.nombre} se adapta facilmente, sobre todo en su habitat {self.habitat}")    
        
    def instintos(self):
        pass
    
    def descansar(self):
        print(f"el {self.nombre} esta descansando")
        
    def sueño(self):
        print(f"el {self.nombre} descansa bastante")
   
        
        
        