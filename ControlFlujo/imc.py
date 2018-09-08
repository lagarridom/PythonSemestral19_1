#6.-
# Ejercicio
# Determinar el el estado de peso basado
# en el IMC

peso = float(input("Dame tu peso en kg: "))
estatura = float(input("Dame tu estatura en m: "))

imc = peso/estatura**2

if imc < 18.5:
	print("Bajo de peso")
elif imc < 24.9:
	print("Normal")
elif imc < 29.9:
	print("Sobrepeso")
else:
	print("Obesidad")

print("IMC = "+str(imc))