from modelo_auto import autos

class camion(autos):
    def __init__(self, modelo, color, motor, numero_de_puertas, capacidad_de_pasajeros, tipo_de_combustible, capacidad_de_carga ):
        super().__init__(modelo, color, motor, numero_de_puertas, capacidad_de_pasajeros, tipo_de_combustible)
        self.capacidad_de_carga = capacidad_de_carga
        self.tipo_vehiculo = 3
        
    def arrancar(self):
        super().arrancar()
        print(f"el carro {self.modelo} ha arrancado")
        
    def apagar(self):
        super().apagar()
        print(f"el carro{self.modelo} esta arrancando")
        
    def verificar_tipo_de_seguridad(self):
        super().verificar_tipo_de_seguridad()
        print(f"el sistema de seguridad de las {self.numero_de_puertas} puertas esta funcionando correctamente la mayoria de veces - NIVEL DE SEGURIDAD MEDIO")
        
    def verificar_capacidad_de_carga(self):
        respuesta = int(input("ingrese el peso en kilogramos de la carga que va a llevar el camion \n"))
        if respuesta<self.capacidad_de_carga:
            print ("el peso no sobrepasa la capacidad de carga que puede llevar el camion \npuede continuar....")
        else:
            print("el peso sobrepasa la capacidad de carga que puede llevar el camion \nno puede continuar")
        