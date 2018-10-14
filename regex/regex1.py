
"""
patron.search(texto)

Genera un objeto match de la primer concordancia
encontrada en el texto, en caso de no haber ninguna
concordancia, retorna None 


patron.sub(rempl, texto)

Genera una cadena que reemplace las concordancias
por un valor de reemplazo preestablecido

"""


"""
match.group(n)
# Retorna el grupo n del match
"""


#print("hola\ncomo\nestas?")
#print(r"hola\ncomo\nestas?")


import re

texto = "Mi teléfono es 5534467029  y el de mi hermana es 5539482019"

patron = re.compile(r"(\d{2})\d{8}")

#print(type(patron))

match = patron.search(texto)
#print(match1)

#print(type(match1))

# Si cambiamos el patron a uno que no  
# genere match, patron va a ser None


print(match.group()) #print(match1.group(0))
print(match.group(1))

textoNuevo = patron.sub("TELEFONO",texto)

print(textoNuevo)
