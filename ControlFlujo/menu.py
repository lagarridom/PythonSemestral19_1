#9.-
# Ejemplo de menú

while True:
	respuesta = input("""

	Selecciona una opción:

	a) Imprimir un Hola mundo bien chido

	b) Sumar 2 + 2

	c) Que te cante

	d) Contar cuantas letras tiene 'Electroencefalografista'

	*) Salir
	""")
	if respuesta == 'a':
		print("HoL@ MunD0!!??!")
	elif respuesta == 'b':
		print(2+2)
	elif respuesta == 'c':
		print("Amigo voy a darte un buen consejo, si quieres ......")
	elif respuesta == "d":
		print(len("Electroencefalografista"))
	else:
		break