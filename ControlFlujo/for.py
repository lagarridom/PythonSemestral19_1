#10.-
"""
for ITERADOR in ITERABLE:
	instrucciones
"""

for i in [10, 20, 30, 40, 50]:
	print(i)


nombres = ["luis", "pato", "gabriel"]

for nom in nombres:
	print("El es"+nom)

for elemento in ("cadena", 3, 3.4, True):
	print(type(elemento))

diccionario = {"lunes":"pollo","martes":"pescado","miercoles":"carne"}

for llave in diccionario:
	print("Los %s me gusta comer %s"%(llave,diccionario[llave]))
	#print("Los {} me gusta comer {}".format(llave,diccionario[llave]))

lista = [("Jorge",10),("Gueva",9),("Ana",10)]

for nombre,calif in lista:
	print("%s obtuvo %s"%(nombre,calif))

	