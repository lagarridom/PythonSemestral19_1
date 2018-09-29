class Perro:
	def ladrar(self):
		print('Wooof!!')

	def comer(self,comida):
		print('Estoy comiendo',comida)

# Definición de clase
# Métodos son parecidos a las funciones
# se necesita poner self como primer
# parámetro en métodos

#Creación de objetos

# "Instanciación"
perro1 = Perro()
# Como llamamos métodos en listas
# De igual forma llamamos métodos en objetos
perro1.ladrar()
perro1.comer('Dog Chow')

perro2 = Perro()
perro2.ladrar()

"""
La palabra self, va a denotar el objeto en particular,
cuando perro1 realiza el método comer, self es perro1.
Cuando perro2 realiza el método ladrar, self es perro2.
"""

print('Son iguales? -',perro1 == perro2)
print(type(perro1))