#1.-

"""
Código para convertir grados Celsius a grados Fahrenheit
y depués de grados Fahrenheit a Celsius
"""

# F = (9/5)*C + 32
# Explicar un poco de jerarquía de operaciones
grados_C = input("Ingresa Celsius: ")
convertido = (9/5)*float(grados_C) + 32

print(grados_C+" ºC -> "+str(convertido)+" ºF")

grados_F = input("Ingrese Fahrenheit: ")
convertido = (5/9)*(float(grados_F) - 32)

print(grados_F+" ºF -> "+convertido+" ºC")
# Enseñar el tipo de formateo %.3F si da tiempo al final