#11.-
# Ejercicio 
# Quitar las vocales de una frase

vocales = ('a','A','e','E','i','I','o','O','u','U')

texto = input("Ingresa una frase: ")

final = ""
for caracter in texto:
	if caracter in vocales:
		continue
	final += caracter

print(final)