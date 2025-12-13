from modelo_animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return f"{self.nombre} corre rápidamente por praderas."

    def alimentarse(self):
        return f"{self.nombre} come pasto y heno."