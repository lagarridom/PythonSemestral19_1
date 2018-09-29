# Se debe realizar un código que guarde entradas a un archivo
# y después poder recopilarlas


archivo = open('datos.txt','a+')

while True:
	respuesta = input("""

Ingrese la opción a realizar:
a) Guardar calificación
b) Obtener calificación
c) Mostrar calificaciones
*) Salir

""")
	if respuesta == 'a':
		nombre = input("Nombre: ")
		calificacion = input("Calificación: ")
		archivo.write(nombre + ',' + calificacion + '\n')
		print(" CALIFICACIÓN GUARDADA")

	elif respuesta == 'b':
		archivo.seek(0)
		nombre = input("Nombre: ")
		listaLineas = archivo.readlines()
		for elemento in listaLineas:
			nom,calif = elemento.split(',')
			if nombre == nom:
				print('Calificación: '+calif)
				break
		else:
			print("No se encontró calificación")

	elif respuesta == 'c':
		archivo.seek(0)
		listaLineas = archivo.readlines()
		for elemento in listaLineas:
			nom,calif = elemento.split(',')
			print(nom + " sacó " + calif)
	else:
		archivo.close()
		break
