from modelo_animal import Animal
from modelo_de_hijo_caballo import Caballo
from modelo_hijo_drilococo import Cocodrilo
from modelo_hijo_pez import Pez
from modelo_hijo_escarabajo import Escarabajo
from modelo_hijo_pato import Pato
    #codigo principal
Caballo= Caballo("nombre: goldship", "edad: 5 años", "raza: Mustang", " Marrón", "tamaño: Grande", "alimentación: Hierba y avena")
cocodrilo= Cocodrilo("nombre: Rex", "edad: 12 años", "raza: Caimán", "color: Verde oscuro", "tamaño: Grande", "alimentación: Carnívoro")
pez= Pez("nombre: ei ", "edad: 2 años", "raza: cachama", "color: marron y blanco", "tamaño: Pequeño", "alimentación: Omnívoro")
escarabajo= Escarabajo("nombre: rino", "edad: 1 año", "raza: escarabajo rinoceronte", "color: negro", "tamaño: Mediano", "alimentación: Hoja y frutas")
Pato = Pato ("nombre: pay", "edad: 3 años", "raza: Pato mandarín", "color: Multicolor", "tamaño: Mediano", "alimentación: Omnívoro")

#mostrar datos de los animales
Animal = [Caballo, cocodrilo, pez, escarabajo, Pato]
for animal in Animal:
    print(f"\nanimal: {animal.__class__.__name__}")
    print(f"\nANIMAL: {animal.nombre}")
    print(f"Edad: {animal.edad}, Hábitat: {animal.habitat}, Dieta: {animal.dieta}, Tamaño: {animal.tamaño}, Color: {animal.color}")
    print(animal.moverse())
    print(animal.alimentarse())
    print(animal.comunicacion())
    print(animal.reproduccion())
    print(animal.adaptacion())
    print(animal.instintos())
    print(animal.descanso())
    print(animal.interaccion_social())
    