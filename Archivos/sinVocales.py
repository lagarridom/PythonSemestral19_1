nombre = input("Ingresa el nombre del archivo: ")

vocales = ('a','e','i','o','u','á')
lectura = open(nombre)
texto = lectura.read()
#print(texto)
lectura.close()
textoNuevo = ""
for caracter in texto:
	if caracter in vocales:
		caracter = ""
	textoNuevo += caracter

escritor = open(nombre,'w')
escritor.write(textoNuevo)