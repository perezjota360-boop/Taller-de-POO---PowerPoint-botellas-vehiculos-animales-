from modelo_botella import Botella
    # clase hija que hereda de Botella
class Botella_plastico(Botella):
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):
        super().__init__(dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados)
        
        
        
    def asignacion_material(self, dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):  
        super().asignacion_material(dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados)     
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseño = dato_diseño
        self.tapa = dato_tapa
        self.grabados = dato_grabados
        
    def asignacion_material2(self, dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados) :
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseño = dato_diseño
        self.tapa = dato_tapa
        self.grabados = dato_grabados   
    
    def compatible_bebidas_calientes(self):
        return "No es compatible para bebidas muy calientes."
