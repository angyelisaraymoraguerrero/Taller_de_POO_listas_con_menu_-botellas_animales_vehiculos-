class Base_datos:
    def __init__(self):
        self.lista_botellas = []
        
    def guardar_obj(self, nuevo_obj):
        self.lista_botellas.append(nuevo_obj)
        
    def imprimir_lista(self):
        for nuevo_obj in self.lista_botellas:
           nuevo_obj.mostrar_info()
                    
                    
                   
                   
                    