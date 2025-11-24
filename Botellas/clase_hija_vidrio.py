from clase_principal import botellas
class botellas_vidrio(botellas):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados, tipo_vidrio):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)
        self.tipo_vidrio = tipo_vidrio
        
    def verificar_cierre_hermetico(self):
        super().verificar_cierre_hermetico() 
        print(f"su tapa es de {self.tapa} y contiene cierre hermetico")   
        
    def transportar(self):
        super().transportar()
        print (f"hay que tener cuidado al momento de transportarla ya que el {self.material} al caerse se puede partir")
        
    def verificar_compatibilidad_con_temperaturas(self):
        print ("apta para bebidas calientes y frias")
        
    def verificar_reutilizacion(self):
        print(f"no se puede reutilizar pero{self.retornar()}" )
        
    def retornar(self):
        print ("se puede retornar")
        
    def mostrar_info(self):
        print(f"material = {self.material}")
        print (f"capacidad = {self.capacidad}")
        print(f"forma = {self.forma}")
        print(f"diseño = {self.diseño}")
        print(f"tapa = {self.tapa}")
        print(f"grabados = {self.grabados}")
        print(f"tipo_vidrio = {self.tipo_vidrio}")
        self.contener_liquidos()
        self.facilitar_vertido()
        self.verificar_cierre_hermetico()
        self.transportar()
        self.verificar_compatibilidad_con_temperaturas()
        self.verificar_reutilizacion()
        self.retornar()
        print("\n")
    
        