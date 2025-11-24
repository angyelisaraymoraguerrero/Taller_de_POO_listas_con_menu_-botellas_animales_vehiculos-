class autos:
    def __init__(self,modelo, color, motor, numero_de_puertas, capacidad_de_pasajeros, tipo_de_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_de_puertas = numero_de_puertas
        self.capacidad_de_pasajeros = capacidad_de_pasajeros
        self.tipo_de_combustible = tipo_de_combustible
        
        
    def arrancar(self):
        print("el vehiculo esta arrancando")
        
    def apagar(self):
        print("el vehiculo esta apagandose")
        
    def acelerar_y_frenar(self):
        print("el vehiculo puede acelerar y frenar correctamente")
        
    def verificar_sistema_de_direccion(self):
        print("el vehiculo tiene el sistema de direcciones en buen estado")
        
    def climatizar(self):
        print("el aire acondicionado esta encendido")
        
    def verificar_tipo_de_seguridad(self):
        print("verificando sistema de seguridad.....")
        
    def verificar_luces(self):
        print("las luces estan funcionando correctamente")
    
    def ajustar_sistema_de_ventanas(self):
        print("el sistema de ventanas esta funcionando correctamente")
    
    def ajustar_sistema_de_espejo(self):
        print("el sistema de espejo esta funcionando correctamente")
    