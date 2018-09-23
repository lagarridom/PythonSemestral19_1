def decorador(funcionOriginal): #funcionA(funcionB)----> funcionC
	def funcionModificada(*args, **kwargs): #Funcion que modifica la funcion
		print("Vamos a sumar dos numeros")
		funcionOriginal(*args, **kwargs)
		print("Acabamos de sumar dos numeros")
	return funcionModificada

@decorador 
def funcionOriginal(a,b):
	suma = a + b 
	print(suma)
numero1 = int(input("Dame un numero"))
numero2 = int(input("Dame otro numero"))
funcionOriginal(numero1, numero2) #Llamada funcion