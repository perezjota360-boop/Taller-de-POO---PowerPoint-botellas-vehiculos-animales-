from modelo_animal import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return f"{self.nombre} nada con facilidad en el agua."

    def alimentarse(self):
        return f"{self.nombre} se alimenta de algas y pequeños insectos acuáticos."