class Base_datos:
    def __init__(self):
        self.lista_carros = []
        
    def guardar_datos(self, nuevo_obj):
        self.lista_carros.append(nuevo_obj)
        
        
    def imprimir_lista(self, pregunta):
        self.pregunta = pregunta
        for nuevo_obj in self.lista_carros:
            if nuevo_obj.tipo_vehiculo != pregunta:
                continue
            
            match self.pregunta:
                case 1: 
                    print(f"Modelo: {nuevo_obj.modelo}")
                    print(f"Color: {nuevo_obj.color}")
                    print(f"Motor: {nuevo_obj.motor}")
                    print(f"Numero de puertas: {nuevo_obj.numero_de_puertas}")
                    print(f"Capacidad de pasajeros: {nuevo_obj.capacidad_de_pasajeros}")
                    print(f"Combustible: {nuevo_obj.tipo_de_combustible}")
                    print(f"Descapotable: {nuevo_obj.descapotable}")
                    print(f"Sistema de sonido: {nuevo_obj.sistema_de_sonido}")
                    print(f"Aire acondicionado: {nuevo_obj.aire_acondicionado}")
                    nuevo_obj.arrancar()
                    nuevo_obj.apagar()
                    nuevo_obj.acelerar_y_frenar()
                    nuevo_obj.verificar_sistema_de_direccion()
                    nuevo_obj.climatizar()
                    nuevo_obj.verificar_tipo_de_seguridad()
                    nuevo_obj.verificar_luces()
                    nuevo_obj.ajustar_sistema_de_ventanas()
                    nuevo_obj.ajustar_sistema_de_espejo()
                    print("\n ")
                    
                case 2:
                    print(f"Modelo: {nuevo_obj.modelo}")
                    print(f"Color: {nuevo_obj.color}")
                    print(f"Motor: {nuevo_obj.motor}")
                    print(f"Numero de puertas: {nuevo_obj.numero_de_puertas}")
                    print(f"Capacidad de pasajeros: {nuevo_obj.capacidad_de_pasajeros}")
                    print(f"Combustible: {nuevo_obj.tipo_de_combustible}")
                    print(f"Puerta corrediza: {nuevo_obj.puerta_corrediza}")
                    nuevo_obj.arrancar()
                    nuevo_obj.apagar()
                    nuevo_obj.acelerar_y_frenar()
                    nuevo_obj.verificar_sistema_de_direccion()
                    nuevo_obj.climatizar()
                    nuevo_obj.verificar_tipo_de_seguridad()
                    nuevo_obj.utilizar_puerta_corrediza()
                    print("\n ")
                    
                case 3:
                    print(f"Modelo: {nuevo_obj.modelo}")
                    print(f"Color: {nuevo_obj.color}")
                    print(f"Motor: {nuevo_obj.motor}")
                    print(f"Numero de puertas: {nuevo_obj.numero_de_puertas}")
                    print(f"Capacidad de pasajeros: {nuevo_obj.capacidad_de_pasajeros}")
                    print(f"Combustible: {nuevo_obj.tipo_de_combustible}")
                    print(f"Capacidad de carga: {nuevo_obj.capacidad_de_carga}")
                    nuevo_obj.arrancar()
                    nuevo_obj.apagar()
                    nuevo_obj.acelerar_y_frenar()
                    nuevo_obj.verificar_sistema_de_direccion()
                    nuevo_obj.climatizar()
                    nuevo_obj.verificar_tipo_de_seguridad()
                    nuevo_obj.verificar_capacidad_de_carga()
                    print("\n ")
                    