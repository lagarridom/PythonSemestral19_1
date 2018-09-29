class Perro:
	
	def __init__(self,NOMBRE,EDAD,ALIMENTO,RAZA):
		self.nombre = NOMBRE
		self.edad = EDAD
		self.alimento = ALIMENTO
		self.raza = RAZA

	def ladrar(self):
		print('Wooof!!')

	def comer(self):
		print('Estoy comiendo',self.alimento)


	# Método mágico
	def __add__(self,Perro2):
		# print('Los perros se sumaron')
		# return Perro(Nombre,edad,alimento,raza)
		return Perro(self.nombre+' Jr',0, self.alimento, self.raza+'-'+Perro2.raza)

perro1 = Perro('Max',2,'Pollo','Labrador')
perro2 = Perro('Luna',3,'Croquetas','Collie')

perroHijo = perro1 + perro2
print(perroHijo.nombre)
print(perroHijo.edad)
print(perroHijo.raza)
perroHijo.comer()