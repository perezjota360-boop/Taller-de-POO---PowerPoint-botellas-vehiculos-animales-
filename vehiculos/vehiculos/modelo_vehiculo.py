# Clase base
class Vehiculo:
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    # Métodos generales
    def arranque(self):
        return f"El {self.modelo} arranca."

    def apagado(self):
        return f"El {self.modelo} se apaga."

    def aceleracion_frenado(self):
        return f"El {self.modelo} acelera y frena según se requiera."

    def sistema_direccion(self):
        return f"El {self.modelo} tiene sistema de dirección funcional."

    def climatizacion(self):
        return f"El {self.modelo} tiene climatización para confort."

    def tipo_seguridad(self):
        return f"El {self.modelo} cuenta con sistemas de seguridad."

    def luces(self):
        return f"El {self.modelo} enciende y apaga luces."

    def sistema_ventanas(self):
        return f"El {self.modelo} permite abrir y cerrar ventanas."

    def sistema_espejo(self):
        return f"El {self.modelo} tiene espejos ajustables."

    # Método para actualizar atributos si se desea
    def asignar_atributos(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
