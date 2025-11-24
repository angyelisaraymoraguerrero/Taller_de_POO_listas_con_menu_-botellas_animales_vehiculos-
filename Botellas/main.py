from clase_hija_plastico import botellas_plastico
from clase_hija_vidrio import botellas_vidrio
from base_de_datos import Base_datos
#codigo principal
obj_base_datos = Base_datos()
 
 
while True:
    print("------------MENU-------------")
    opcionGeneral = int(input("1.Agregar botella \n2.Eliminar todas las botellas \n3.Imprimir botella\n0.salir\n"))
    match opcionGeneral:
        case 1: 
            print("elija el material \nmateriales disponibles: plastico y vidrio\n")
            opcionBotella = input()
            match opcionBotella:
                case "plastico":
                    material = "vidrio"
                    capacidad = int(input("ingrese la capacidad:"))
                    forma = input("ingrese la forma:")
                    diseño = input("ingrese el diseño:")
                    tapa = input("tapa:")
                    grabados = input("ingrese los grabados: ")
                    tipo_plastico = input("ingrese el tipo de plastico: ")
                    flexibilidad = input("ingrese la flexibilidad: ")
                    obj_botella_plastico = botellas_plastico(material, capacidad, forma, diseño, tapa, grabados, tipo_plastico, flexibilidad)
                    obj_base_datos.guardar_obj(obj_botella_plastico)
                    
                    
                case "vidrio":
                    material = "vidrio"
                    capacidad = int(input("ingrese la capacidad:"))
                    forma = input("ingrese la forma:")
                    diseño = input("ingrese el diseño:")
                    tapa = input("tapa:")
                    grabados = input("ingrese los grabados: ")
                    tipo_vidrio = input("ingrese el tipo de vidrio: ")
                    obj_botella_vidrio = botellas_vidrio(material, capacidad, forma, diseño, tapa, grabados, tipo_vidrio)
                    obj_base_datos.guardar_obj(obj_botella_vidrio)
        case 2:
            
            if not obj_base_datos.lista_botellas: 
                print("la lista esta vacia, no hay nada por eliminar")
            else:
                obj_base_datos.lista_botellas.clear()
                print("las botellas que ha guardado han sido eliminadas")
        case 3:
            if not obj_base_datos.lista_botellas:
                print("la lista esta vacia, no hay nada que imprimir")
            else:    
                obj_base_datos.imprimir_lista()
        case 0:
            break

"""
h1 = botellas_plastico("plastico ", "500 ml", "rectagular", "diseo unico","plastico", "agua vida", "tipo tal", "muy flexible")
h1.contener_liquidos()
h1.facilitar_vertido()
h1.verificar_cierre_hermetico()
h1.transportar()
h1.manejar()
h1.verificar_compatibilidad_con_temperaturas()
h1.verificar_reutilizacion()
h1.verificar_transparencia()

h2 = botellas_vidrio("vidrio", "1000ml","forma unica", "dise;o unico", "tapa de plastico", "coca-cola", "vidrio tipo 1")

h2.contener_liquidos()
h2.facilitar_vertido()
h2.verificar_cierre_hermetico()
h2.transportar()
h2.manejar()
h2.verificar_compatibilidad_con_temperaturas()
h2.verificar_reutilizacion()
h2.verificar_transparencia()"""