#Generar una clase con atributos y metodos para una cuenta bancaria 
class CuentaBancaria:
    #definicion de atributos
    def __init__(self,tit,sal):
        self.titular = tit
        self.saldo = sal

    #Metodos de la cuenta bancaria
    def depositar(self,monto):
        self.saldo = self.saldo + monto
    
    def retirar(self,monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
        else:
            print("Fondo insuficientes")
#####################################################################
cuenta = CuentaBancaria("Ricardo",100)
print("Datos de la cuenta")
print(f"Titular :::> {cuenta.titular}")
print(f"Saldo   :::> {cuenta.saldo}")
#quiero depositar dinero a mi cuenta
cuenta.depositar(100)
print(f"Nuevo saldo :::> {cuenta.saldo}")
cuenta.retirar(150)
print(f"Nuevo saldo retirado :::> {cuenta.saldo}")


    