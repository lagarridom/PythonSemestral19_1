############################
#Agenda Telefonica 
############################

directorio={"Jorge":5541415228,"Gali":5535714785,"Andrea":5523015969,"Pato":5545678734,"Luis":5544335645}


def agregarContacto(directorio):
	nuevoNombre = input("Ingresa el nombre: ")
	nuevoTelefono = int(input("Ingresa el teléfono: "))
	directorio[nuevoNombre] = nuevoTelefono	

def eliminarContacto(directorio):
	nombre = input("Ingresa el nombre: ")
	directorio.pop(nombre)

def mostrarContacto(directorio):
	for persona in directorio:
		print(persona)

while True:
	print("\n1.-Agregar contacto\n2.-Mostrar contactos\n3.-Eliminar contacto\n4.-Salir")
	opcion = input("¿Qué deseas realizar?:  ")
	if opcion =='1':
		agregarContacto(directorio)
	elif opcion =='2':
		mostrarContacto(directorio)
	elif opcion == '3':
		eliminarContacto(directorio)
	elif opcion == '4':
		print("Vuelve pronto!")
		break
	else:
		print("Opción incorrrecta, intenta de nuevo!")
