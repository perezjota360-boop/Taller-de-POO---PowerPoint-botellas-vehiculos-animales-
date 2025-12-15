#se crea la clase
class Botella :
    # metodo constructor
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):
        self.material = dato_materiales
        self.forma = dato_forma
        self.capacidad = dato_capacidad
        self.diseño = dato_diseño
        self.tapa = dato_tapa
        self.grabados = dato_grabados
    # metodos de la clase
    def contener_liquidos(self):
        return "La botella puede contener líquidos."

    def facilitar_vertido(self):
        return "La botella se le puede verter el líquido fácilmente."

    def cierre_hermetico(self):
        if self.tapa:
            return "La botella tiene un cierre hermético."
        return "La botella no cuenta con cierre hermético."

    def transportar(self):
        return "La botella es comoda para el transporte."
    
    def compatibilidad(self):
        return "La botella puede contenere bebidas calientes/frias ."

    def manejo(self):
        return "La botella es manejable."
    
    def reutilizacion(self):
        return "La botella es reutilizable."
    
    def transparencia(self):
        return f"La botella es transparente."
    
    def asignacion_material(self, dato_materiales, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):  
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseño = dato_diseño
        self.tapa = dato_tapa
        self.grabados = dato_grabados
    
    def asignacion_material2(self, dato_materiales, dato_capacidad, dato_forma, dato_tapa, dato_grabados,dato_diseño):  
        self.material = dato_materiales
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseño = dato_diseño
         self.grabados = dato_grabados
        self.tapa = dato_tapa
       
    
    

