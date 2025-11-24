from base_datos import Base_datos
from carro_hijo1 import Carro
from minivan_hijo2 import minivan
from camion_hijo3 import camion

# codigo principal
obj_conexion = Base_datos()
 
while True:
    opVehiculo = int(input("elija el carro que desea usar \n1.Carro \n2.Minivan \n 3.Camion \n"))
    match opVehiculo:
        case 1:
            obj_carro = Carro("chevrolet", "rojo", "motor tipo 3", 2, 4, "gasolina", "si", "si", "si") 
            obj_conexion.guardar_datos(obj_carro)
            obj_conexion.imprimir_lista(1)
        case 2:
            obj_minivan = minivan("minivan compacta", "blanco", "tipo 6", 2, 7, "gasolina", "si")
            obj_conexion.guardar_datos(obj_minivan)
            obj_conexion.imprimir_lista(2)
        case 3:
            obj_camion = camion("trailer","azul", "motor tipo 25", 3, 3, "diesel", 50)
            obj_conexion.guardar_datos(obj_camion)
            obj_conexion.imprimir_lista(3)
  
