#8.-
# Ejercicio 
# Imprimir 'clap' cada múltiplo de 7 o
# con números que contengan 7

final = int(input("Hasta que número? "))
numero = 0
while numero < final:
	numero += 1
	
	if numero % 7 == 0:
		print('clap')
	elif '7' in str(numero):
		print('clap')
	else:
		print(numero)
	

