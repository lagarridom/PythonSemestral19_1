# Código que permite que sobreescribe contenido de un archivo
# pero con minúsculas

# Pedimos nombre de archivio (arch1.txt)
nombre = input("Ingresa el nombre del archivo: ")

# Creamos tupla con vocales
vocales = ('a','e','i','o','u')

# Creamos objeto archivo de lectura
lectura = open(nombre)
# Guardamos texto de archivo
texto = lectura.read()
lectura.close()


textoNuevo = ""

'''
Por cada caracter en el texto, si el caracter se
encuentra en la tupla de vocales, no vamos a escribir
ese caracter en textoNuevo, en caso contrario, lo vamos
a escribir en textoNuevo
'''
for caracter in texto:
	if caracter in vocales:
		caracter = ""
	textoNuevo += caracter

# Creamos objeto archivo de escritura y borramos
# el contenido que tenía el archivo que abrimos
escritor = open(nombre,'w')

# Escribimos textoNuevo en el
escritor.write(textoNuevo)
