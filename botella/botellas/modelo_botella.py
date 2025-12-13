#se crea la clase
class Botella :
    # metodo constructor
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):
        self.material = dato_material
        self.forma = dato_forma
        self.capacidad = dato_capacidad
        self.diseño = dato_diseño
        self.tapa = dato_tapa
        self.grabados = dato_grabados
    # metodos de la clase
    def contener_liquidos(self):
        return "La botella puede contener líquidos."

    def facilitar_vertido(self):
        return "La botella permite verter el líquido fácilmente."

    def cierre_hermetico(self):
        if self.tapa:
            return "La botella tiene un cierre hermético."
        return "La botella no cuenta con cierre hermético."

    def transportar(self):
        return "La botella es apta para el transporte."
    
    def compatibilidad(self):
        return "La botella es compatible con bebidas calientes/frias ."

    def manejo(self):
        return "La botella es manejable."
    
    def reutilizacion(self):
        return "La botella es reutilizable."
    
    def transparencia(self):
        return f"La botella es transparente."
    
    def asignacion_material(self, dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):  
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseño = dato_diseño
        self.tapa = dato_tapa
        self.grabados = dato_grabados
    
    def asignacion_material2(self, dato_material, dato_capacidad, dato_forma, dato_diseño, dato_tapa, dato_grabados):  
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseño = dato_diseño
        self.tapa = dato_tapa
        self.grabados = dato_grabados
    
    
