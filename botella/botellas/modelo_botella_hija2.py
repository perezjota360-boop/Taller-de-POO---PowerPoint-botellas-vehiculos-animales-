sfrom modelo_botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, dato_materiales, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):
        super().__init__(dato_materiales, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados)
        
        
    def asignacion_material(self, dato_materiales, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):    
        super().asignacion_material2(dato_materiales, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados)
        self.material = dato_materiales
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseño = dato_diseño
        self.grabados = dato_grabados
        self.tapa = dato_tapa
        
    
    def compatible_bebidas_calientes(self):
        return "compatible para bebidas muy calientes y frías."


