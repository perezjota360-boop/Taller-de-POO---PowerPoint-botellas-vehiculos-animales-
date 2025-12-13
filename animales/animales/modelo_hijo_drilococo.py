from modelo_animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return f"{self.nombre} se desplaza lentamente en tierra y ágilmente en el agua."

    def alimentarse(self):
        return f"{self.nombre} come carne de animales acuáticos y terrestres."