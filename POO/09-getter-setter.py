#el get se usa para acceder al atributo 
#El set se usa para modificar el atributo

class Persona:
    def __init__(self,nombre):
        self.__nombre = nombre ##atributo privado
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

#uso
p = Persona("Juan")
print(p.get_nombre())
#modificamos el atributo __nombre
p.set_nombre("Carlos")
print(p.get_nombre())