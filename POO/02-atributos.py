class Persona:
    #atributos de entrada nombre:n y edad:e 
    def __init__(self,n,e):
        self.nombre = n
        self.edad = e

#~#################################################################

p1 = Persona("Ricardo",34)
print(p1.nombre)
print(p1.edad)

p2 = Persona("Ana",33)
print(p2.nombre)
print(p2.edad)

p3 = Persona("Ruben",17)
print(p3.nombre)

