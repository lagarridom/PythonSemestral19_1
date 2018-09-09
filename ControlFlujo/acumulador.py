# Realizar la suma de los números que ingrese el usuario
# hasta cierto valor

suma = 0

while True:
	numero = int(input("Dame el número que quieres sumar: "))
	if numero == 0:
		break
	suma += numero

print("La suma es: "+ str(suma))