import re

# Generar un código que lea el contenido de el archivo contactos.txt
# y guarde todos los correos VÁLIDOS en un nuevo archivo llamado
# correos.txt

archivo = open("contactos.txt")
texto = archivo.read()
archivo.close()

patronCorreos = re.compile(r"[\d\w.]+@[\w]+\.\w+(.\w+)*")

archivoN = open("correos.txt","w")

for match in patronCorreos.finditer(texto):
	archivoN.write(match.group()+"\n")

archivoN.close()

"""
# Ahora en lugar de guardar solo los correos, guardarlos de la siguiente forma
# correo
# dominio

patronCorreos = re.compile(r"[\d\w.]+@([\w]+\.\w+(.\w+)*)")

archivoN = open("correos.txt","w")

for match in patronCorreos.finditer(texto):
	archivoN.write(match.group()+"\n")
	archivoN.write(match.group(1)+"\n")

archivoN.close()
"""
