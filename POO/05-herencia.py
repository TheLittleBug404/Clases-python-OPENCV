#Clase padre
class Animal:
    def __init__(self,nomb):
        self.nombre = nomb #Guarda el nombre del animal
    
    def ladrar(self):
        print("El animal hace un sonido")

#clase hijo
class Perro(Animal):
    def ladrar(self):
        print(self.nombre," es un perro")

#uso em herencia
mi_perro = Perro("Firulais")
mi_perro.ladrar()