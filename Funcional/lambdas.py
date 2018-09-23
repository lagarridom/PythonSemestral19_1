def suma(a,b):
	return a + b
def resta(a,b):
	return a - b
def division(a,b):
	return a / b
def multiplicacion(a,b):
	return a * b
#lambda <argumento>: <expresion>
suma = lambda a,b: a+b
resta = lambda a,b: a-b
multiplicacion = lambda a,b: a*b
division = lambda a,b: a/b
numero1 = int(input("Dame un numero"))
numero2 = int(input("Dame otro numero"))

print('Funciones')
print(suma(numero1,numero2))
print(resta(numero1,numero2))
print(division(numero1,numero2))
print(multiplicacion(numero1,numero2))
print('Lambdas')
print(suma(numero1,numero2))
print(resta(numero1,numero2))
print(division(numero1,numero2))
print(multiplicacion(numero1,numero2))
