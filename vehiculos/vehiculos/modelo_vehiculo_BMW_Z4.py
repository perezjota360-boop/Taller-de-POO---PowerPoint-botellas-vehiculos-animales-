from modelo_vehiculo import Vehiculo

class BMW_Z4(Vehiculo):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)

    def aceleracion_frenado(self):
        return f"El {self.modelo} tiene aceleración deportiva y frenado de alta precisión."

    def tipo_seguridad(self):
        return f"El {self.modelo} cuenta con airbags, frenos ABS y control de estabilidad."
