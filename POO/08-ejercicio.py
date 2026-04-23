class Animal:
    def __init__(self,nomb):
        self._nombre = nomb #tipo de dato protegido
    
    def hablar(self):
        pass #metodo vacio para polimorfismo

class Perro(Animal):
    def hablar(self):
        print(self._nombre,"dice guau")

class Gato(Animal):
    def hablar(self):
        print(self._nombre,"dice miau")

animales = [Perro("Rex"),Gato("Michi")]

for animal in animales:
    animal.hablar()