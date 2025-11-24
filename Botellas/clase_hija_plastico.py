from clase_principal import botellas

class botellas_plastico(botellas):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados, tipo_plastico, flexibilidad):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)
        self.tipo_plastico = tipo_plastico
        self.flexibilidad = flexibilidad
    
    def verificar_cierre_hermetico(self):
        super().verificar_cierre_hermetico()
        print(f"la tapa es de: {self.tapa} y contiene cierre hermetico")
        
    def transportar(self):
        super().transportar()
        print(f"su material de {self.material} permite que sea facil de transportar")
    
    def verificar_reutilizacion(self):
        print("las botellas plasticas permiten reutilizarse varias veces manteniendo el higiene siempre y cuando se limpien adecuadamente")
    
    def verificar_compatibilidad_con_temperaturas(self):
        print("adecuada solo para bebidas frias")
        
    def mostrar_info(self):
        print(f"material = {self.material}")
        print (f"capacidad = {self.capacidad}")
        print(f"forma = {self.forma}")
        print(f"diseño = {self.diseño}")
        print(f"tapa = {self.tapa}")
        print(f"grabados = {self.grabados}")
        print(f"tipo de plastico = {self.tipo_plastico}")
        print(f"flexibilidad = {self.flexibilidad}")
        
        self.contener_liquidos()
        self.facilitar_vertido()
        self.verificar_cierre_hermetico()
        self.transportar()
        self.verificar_compatibilidad_con_temperaturas()
        self.verificar_reutilizacion()
        print("\n")
        
        
        
        
        
        