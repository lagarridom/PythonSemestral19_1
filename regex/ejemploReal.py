import re

# https://regex101.com/

archivo = open('datosReal.txt')
texto = archivo.read()
archivo.close()

patronF = re.compile(r"Frequencies\s*--\s*(\d+\.\d+)\s+(\d+\.\d+)\s*(\d+\.\d+)")
promFrec = {}

for n, match in enumerate(patronF.finditer(texto)):
	suma = 0;
	for valor in match.groups():
		suma += float(valor)

	promFrec[n] = suma/3


patronR = re.compile(r"Rot. str.\s+--\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)")
promRot = {}

for n, match in enumerate(patronR.finditer(texto)):
	suma = 0;
	for valor in match.groups():
		suma += float(valor)

	promRot[n] = suma/3


patron = re.compile(r"Sum of electronic and thermal Enthalpies=\s+(-?\d+.\d+)")
entalp = patron.search(texto).group(1)

print("FRECUENCIAS")
print(promFrec)
print("ROT STR")
print(promRot)
print("ENTALPIA")
print(entalp)