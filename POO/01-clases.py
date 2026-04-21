#DEFINICION DE UNA CLASE
class Operaciones:
    def suma(self,a,b):
        return a + b

    def multiplicar(self,a,b):
        return a* b
    
    def resta(self,a,b):
        return a-b

    def division(self,a,b):
        return a/b
##################################################################

o = Operaciones()
resultado = o.suma(4,5)
print(resultado)
print(o.multiplicar(4,4))