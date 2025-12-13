from modelo_animal import Animal

class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return f"{self.nombre} nada en el agua y camina en tierra."

    def alimentarse(self):
        return f"{self.nombre} come plantas acuáticas, insectos y peces pequeños."