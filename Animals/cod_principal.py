from animal_caballo import caballo
from animal_hipopotamo import hipopotamo
from animal_pato import pato
from base_de_datos import base_de_datos

#------------Codigo principal--------------
obj_base_datos = base_de_datos()

while True:
    print("------------menu del zoologico------------")
    print("De que animal desea almacenar informacion hoy?")
    preguntaAnimal = int(input("1. Caballo\n2.Pato\n3.Hipopotamo\n4.Eliminar datos guardados\n5.mostrar datos guardados\n0.salir\n"))
    match preguntaAnimal:
        case 1:
            print("ingrese los siguientes datos del animal:")
            nombre = "caballo"
            edad = int(input("edad:"))
            habitat = input("habitat:")
            dieta = input("dieta:")
            tamaño = input("tamaño:")
            color = input("color:")
            raza = input("raza:")
            velocidad = float(input("velocidad:"))
            obj_caballo = caballo(nombre, edad, habitat,dieta, tamaño, color, raza, velocidad)
            obj_base_datos.guardar_objetos(obj_caballo)
            print("\n")
            
        case 2:
            print("ingrese los siguientes datos del animal:")
            nombre = "pato"
            edad = int(input("edad:"))
            habitat = input("habitat:")
            dieta = input("dieta:")
            tamaño = input("tamaño:")
            color = input("color:")
            velocidad = float(input("velocidad:"))
            obj_pato = pato(nombre, edad, habitat,dieta, tamaño, color, velocidad)
            obj_base_datos.guardar_objetos(obj_pato)
            print("\n")
            
        case 3:
            print("ingrese los siguientes datos del animal:")
            nombre = "pato"
            edad = int(input("edad:"))
            habitat = input("habitat:")
            dieta = input("dieta:")
            tamaño = input("tamaño:")
            color = input("color:")
            velocidad = float(input("velocidad:"))
            peso = float(input("peso"))
            obj_hipopotamo = hipopotamo(nombre, edad, habitat,dieta, tamaño, color, velocidad, peso)
            obj_base_datos.guardar_objetos(obj_hipopotamo)
            print("\n")
            
        case 4:
            if not obj_base_datos.lista_animales: 
                print("la lista esta vacia, no hay nada por eliminar")
            else:
                obj_base_datos.lista_animales.clear()
                print("los datos han sido eliminados exitosamente")
            print("\n")
           
        case 5:
            if not obj_base_datos.lista_animales:
                print("la lista esta vacia, no hay nada que imprimir")
            else:    
                obj_base_datos.imprimir_info()
            
        case 0:
            print("ha sido un gusto su visita, le esperamos de nuevo")
            break
            
            
            
            
            
            
            
            
    

