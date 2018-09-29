class Perro:
	# dos guiones bajo,init,dos guiones bajo
	# Es un método que se va a realizar siempre que
	# creemos un nuevo objeto
	# Se le conoce como 'constructor'
	def __init__(self,NOMBRE,EDAD,ALIMENTO):
		self.nombre = NOMBRE
		self.edad = EDAD
		self.alimento = ALIMENTO

	def ladrar(self):
		print('Wooof!!')

	def comer(self):
		print('Estoy comiendo',self.alimento)
		# self.alimento es la alimento de cada perro en particular


perro1 = Perro('Luna',4,'DOG CHOW')
perro2 = Perro('Maya',2,'Pollo')

# Podemos acceder sus atributos de esta forma
print(perro1.nombre)
print(perro2.edad)

# Cada objeto realiza la acción de una forma en particular
perro1.comer()
perro2.comer()