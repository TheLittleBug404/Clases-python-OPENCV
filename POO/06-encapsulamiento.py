#encapsulamiento es la forma de proteger datos en una clase, evitando acceso directo indebido
#tipos de datos publicos 
#tipos de datos privados 
#tipos de datos protegidos
class CuentaBancaria:
    def __init__(self,sald):
        self.__saldo = sald #atributo es privado
    
    def depositar(self,monto):
        self.__saldo = self.__saldo + monto #modificando el saldo para un deposito
    
    def ver_saldo(self):
        return self.__saldo #devuelve mi variable saldo

#uso
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print(cuenta.ver_saldo()) #1500