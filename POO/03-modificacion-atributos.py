class Persona:
    def __init__(self,n):
        self.nombre = n

    def cambiar_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
###########################################################
p1 = Persona("Pedro")
print(p1.nombre) #Pedro
p1.cambiar_nombre("Juan")
print(p1.nombre) #Juan