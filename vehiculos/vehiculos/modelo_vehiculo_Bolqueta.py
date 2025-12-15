from modelo_vehiculo import Vehiculo

class Bolqueta(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)

    def transporte_carga(self):
        return f"La {self.modelo} se utiliza principalmente para transportar materiales de construcción o carga pesada."

    def sistema_direccion(self):
        return f"La {self.modelo} tiene dirección reforzada para soportar cargas pesadas."

