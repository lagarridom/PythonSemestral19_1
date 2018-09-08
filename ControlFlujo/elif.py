#4.-
"""

if CONDICION:
	instrucciones
elif CONDICION:
	instrucciones
else:
	instrucciones

"""

# Determinar si un número es par y menor que 10
# Ver pass
num = int(input("Dame un número: "))

if num < 10 and num % 2 == 0:
	print("El número es par y menor a 10")
elif num < 10:
	print("El número es menor a 10")
elif num % 2 == 0:
	print("El número es par")
else:
	print("No es par ni menor a 10")
