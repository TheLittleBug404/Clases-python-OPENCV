#funciones que retornan un valor
def saludar(nombre):
    #aca viene nuestro codigo de la funcion
    return f"Hola, {nombre}"


def suma(a,b):
    return a + b

print(saludar("Ricardo"))
print(saludar("Ri"))
print(saludar("cardo"))
print(saludar("Fernando"))
print(saludar("Jauregui"))
a = suma(2,3)
print(a)

