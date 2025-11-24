from modelo_auto import autos

class Carro(autos):
    def __init__(self, modelo, color, motor, numero_de_puertas, capacidad_de_pasajeros, tipo_de_combustible, descapotable, sistema_de_sonido, aire_acondicionado ):
        super().__init__(modelo, color, motor, numero_de_puertas, capacidad_de_pasajeros, tipo_de_combustible)
        self.descapotable = descapotable
        self.sistema_de_sonido = sistema_de_sonido
        self.aire_acondicionado = aire_acondicionado
        self.tipo_vehiculo = 1
        
    def arrancar(self):
        super().arrancar()
        print(f"el carro {self.modelo} ha arrancado")
        
    def apagar(self):
        super().apagar()
        print(f"el carro{self.modelo} esta arrancando")
        
    def verificar_tipo_de_seguridad(self):
        super().verificar_tipo_de_seguridad()
        print(f"el sistema de seguridad de las {self.numero_de_puertas} puertas esta funcionando correctamente - ALTO NIVEL DE SEGURIDAD")
        
    def utilizar_descapotable(self):
        respuesta = int(input("1.bajar el descapotable \n2.subir el descapotable\n"))
        if respuesta == 1:
            print ("bajando techo descapotable")
        else:
            print("subiendo techo descapotable")
    
    def imprimir_info(self):
        info = f"modelo: {self.modelo}, color: {self.color}"
        print(info)