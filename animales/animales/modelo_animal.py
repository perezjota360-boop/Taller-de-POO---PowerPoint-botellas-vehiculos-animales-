# Clase base
class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    # Métodos generales
    def moverse(self):
        return f"{self.nombre} se está moviendo."

    def comunicacion(self):
        return f"{self.nombre} emite sonidos para comunicarse."

    def reproduccion(self):
        return f"{self.nombre} puede reproducirse según su especie."

    def alimentarse(self):
        return f"{self.nombre} se alimenta de {self.dieta}."

    def adaptacion(self):
        return f"{self.nombre} se adapta a su hábitat: {self.habitat}."

    def instintos(self):
        return f"{self.nombre} sigue sus instintos naturales."

    def descanso(self):
        return f"{self.nombre} necesita descansar diariamente."

    def interaccion_social(self):
        return f"{self.nombre} puede interactuar con otros de su especie."

    # Asignar atributos si se necesita modificar después
    def asignar_atributos(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color