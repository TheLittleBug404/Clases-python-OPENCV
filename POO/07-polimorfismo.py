#polimorfismo permite que diferentes clases usen el mismo metodo pero con comportamientos distintos

class Gato:
    def hablar(self):
        print("Miau")

class Perro:
    def hablar(self):
        print("Guau")

#Uso
animales = [Gato(),Perro()]

for animal in animales:
    animal.hablar()