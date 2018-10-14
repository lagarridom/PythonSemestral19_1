import re

# Crear un código que pida al usuario un 
# teléfono y dependiendo del texto ingresado
# determine si es un teléfono válido o no

texto = input("Ingresa un teléfono: ")

#patron = re.compile(r"\d{10}")
patron = re.compile(r"^\d{2}\d{8}$")

if patron.search(texto):
	print("Teléfono correcto")
else:
	print("Teléfono incorrecto")

# Hola mi telefono es 5534467029
