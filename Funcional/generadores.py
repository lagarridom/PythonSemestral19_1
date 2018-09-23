# Los generadores son muy parecidos a las 
# funciones, la principal diferenia es que 
# retornan los valores hasta que se les pide

def gen():
	yield 3
	yield 4
	yield 5
	yield 6

generador = gen()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

# La ejecución de lafunción generadora se 
# detiene en el primer yield y retoma su ejecución
# hasta llegar al siguiente yield cuando se le pide
# el valor

def saludar(*nombres):
	for nom in nombres:
		yield 'Hola '+nom
		print('Siguiente...')

gen = saludar('Jorge','Ana','Hugo','Jessica')

next(gen)
print('Pedir nuevo valor')
next(gen)
print('Pedir nuevo valor')
next(gen)
print('Pedir nuevo valor')
next(gen)

# Se pueden colocar los generadores en un cíclo for
# para que en cada iteración se pida el valor del mismo

def gen():
	yield 'a'
	yield 1
	yield 4+5j
	yield (2,3,4)

for valor in gen():
	print(valor)




