class Animal:

	def respirar(self):
		print("Estoy respirando")

	def alimentarse(self):
		print("Me estoy alimentando")

# Clase perro esta heredando de la clase animal
# Está adquiriendo todos los métodos y atributos de esta
class Perro(Animal):

	def ladrar(self):
		print("Woof!")

	'''
	def alimentarse(self):
		print("Estoy comiendo croquetas")
	'''

perro1 = Perro()
perro1.ladrar()
perro1.respirar()
perro1.alimentarse()
