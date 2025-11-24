from modelo_auto import autos

class minivan(autos):
    def __init__(self, modelo, color, motor, numero_de_puertas, capacidad_de_pasajeros, tipo_de_combustible, puerta_corrediza ):
        super().__init__(modelo, color, motor, numero_de_puertas, capacidad_de_pasajeros, tipo_de_combustible)
        self.puerta_corrediza = puerta_corrediza
        self.tipo_vehiculo = 2
        
    def arrancar(self):
        super().arrancar()
        print(f"el auto modelo {self.modelo} ha arrancado")
        
    def apagar(self):
        super().apagar()
        print(f"el auto modelo {self.modelo} esta arrancando")
        
    def verificar_tipo_de_seguridad(self):
        super().verificar_tipo_de_seguridad()
        print(f"el sistema de seguridad de las {self.numero_de_puertas} puertas esta funcionando correctamente la mayoria de veces - NIVEL DE SEGURIDAD MEDIO")
        
    def utilizar_puerta_corrediza(self):
        if self.puerta_corrediza.lower() == "si":
            respuesta = int(input("1.abrir puerta corrediza \n2.cerrar puerta corrediza\n"))
            if respuesta == 1:
                print ("abriendo puerta corrediza")
            else:
                print("cerrando puerta corrediza")
    
        