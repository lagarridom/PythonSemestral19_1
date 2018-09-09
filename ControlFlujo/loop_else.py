#14.-
respuesta = ""

while respuesta != "salir":
	respuesta = input("Escribe 'salir': ")
	if respuesta == "romper":
		break
else:
	print("Saliste de manera adecuada")

diccionario = {'Ana':10,'Julio':8,'Rodrigo':9}

nombre = input("Ingresa un nombre: ")

########

for nom in diccionario:
	if nom == nombre:
		print('Obtuvo '+str(diccionario[nom]))
		break
else:
	print("No se encontró ese nombre")