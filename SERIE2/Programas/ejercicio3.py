##################
# Cuenta Bancaria
##################
class CuentaBancaria:

	def __init__(self, saldo, nombre):
		self.saldo = saldo
		self.nombre = nombre
		self.mostrarInformacion()

	def mostrarInformacion(self):
		print(self.nombre, "Cuenta con :", str(self.saldo), "de saldo")

	def deposito(self, cantidad):
		print("Deposito de", self.nombre,"por :", str(cantidad))
		####incrementar la cantidad de saldo
		self.saldo += cantidad
		self.mostrarInformacion()

	def retiro(self, cantidad):
		print("Retiro de", self.nombre, "por :", str(cantidad))
		cantidadRetirar = cantidad
		if cantidadRetirar > self.saldo:
			print(self.nombre, "No hay saldo suficiente")
		else:
			##Reducir la cantidad de saldo de la cuenta
			self.saldo -= cantidadRetirar
			self.mostrarInformacion()



cuenta1 = CuentaBancaria(12, "Luvi")
cuenta2 = CuentaBancaria(125, "Gali")


cuenta2.retiro(89)
cuenta1.retiro(120)




