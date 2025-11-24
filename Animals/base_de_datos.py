class base_de_datos:
    def __init__(self):
        self.lista_animales = []
        
    def guardar_objetos(self,nuevo_obj):
        self.lista_animales.append(nuevo_obj)
        
    def imprimir_info(self):
        for nuevo_obj in self.lista_animales:
            nuevo_obj.mostrar_info()