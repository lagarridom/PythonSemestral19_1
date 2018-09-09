# 13.-
# Ejercicio
# Imprimir numero hasta 100
# Si es múltiplo de 3 imprimir 'Fizz'
# Si es múltiplo de 5 imprimir 'Buzz'
# Si es múltiplo de los 2 imprimir 'FizzBuzz'

for numero in range(101):
	if numero % 3 == 0 and numero % 5 == 0:
		print('FizzBuzz')
	elif numero % 3 == 0:
		print('Fizz')
	elif numero % 5 == 0:
		print('Buzz')
	else:
		print(numero)