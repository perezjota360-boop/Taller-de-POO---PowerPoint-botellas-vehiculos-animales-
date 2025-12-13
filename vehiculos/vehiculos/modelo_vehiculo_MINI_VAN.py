from modelo_vehiculo import Vehiculo

class MiniVan(Vehiculo):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)

    def capacidad_carga(self):
        return f"El {self.modelo} está diseñada para transportar carga y pasajeros."

    def sistema_ventanas(self):
        return f"El {self.modelo} tiene ventanas manuales o eléctricas según versión."
