def decorador1(funcion):
	def nuevaFuncion(*args,**kwargs): #Puede o no tener **kwargs
		print("Bienvenido ingresa usuario y contrasena")
		funcion(*args, **kwargs) #Puede o no tener **kwargs
		print("Hasta luego :D")
	return nuevaFuncion

@decorador1
def funcionValida(user, passw):
	usuario = str(input("Ingrese nombre de usuario: "))
	contrasena = str(input("Ingrese comtrasena de usuario: "))
	if((user==usuario) and (passw==contrasena)): #Valida datos
		print("Has ingresado")
	else:
		print("Has ingresado algo mal :(")

usuarioOriginal = "Eduardo"
contrasenaOriginal = "1234"
funcionValida(usuarioOriginal, contrasenaOriginal)
'''Otra prueba de decorador
@decorador1
def funcionOriginal(a,b):
	suma = a + b 
	print(suma)
funcionOriginal(6,6)
'''