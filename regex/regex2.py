
"""
patron.findall(texto)

Retorna una lista que contiene todos las concordancias
generadas. En caso de existir grupos, retorna una lista 
con los grupos sin incluir el 0


patron.finditer(texto)

Retorna un iterador que va a ir retornando objetos Match
de cada concordancia.

"""

# Profundizar en el concepto de objetos match

import re

texto = """Mi teléfono es 5520391428 y el de mi jefe es 5539482039,
El de mi hermana es 5529283847 y el de mi mamá es 5220391820."""

patron = re.compile(r"\d{2}\d{8}")

lista = patron.findall(texto)
print(lista)


patron = re.compile(r"(\d{2})\d{8}")


for match in patron.finditer(texto):
	print(match)
	print(match.group())
	print(match.group(1))


# Tarea -> Hacer comprobación de lada con nacionalidad
