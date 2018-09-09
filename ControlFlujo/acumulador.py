# Realizar la suma de los números que ingrese el usuario
# hasta cierto valor

suma = 0

'''
En un loop infinito vamos a pedirle un número entero al usuario,
cada uno de estos números los vamos a estar sumando a la variables
suma. Cuando el usuario ingrese como número el 0, vamos a salir
del loop infinito
'''
while True:
	numero = int(input("Dame el número que quieres sumar: "))
	if numero == 0:
		break
	suma += numero

# Imprimimos la suma
print("La suma es: "+ str(suma))
