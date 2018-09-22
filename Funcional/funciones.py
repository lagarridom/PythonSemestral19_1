# definición de función
# SINTAXIS
# palabra clave def
# nombre de función
# paréntesis
# dos puntos
# bloque de código
def funcion1():
	a = 3
	b = 2
	print(a+b)

# llamar con nombre y paréntesis
funcion1()
funcion1()


# Las funciones pueden retornar valores
# Se hace con la palabra reservada return
def funcion2():
	a = 3
	b = 2
	return a+b

r = funcion2()
print(r)
# Cuando una función llega a un return, termina

def funcion3():
	a = "hola"
	b = "que"
	c = "hace"
	return a+b+c
	print('Adios')

r = funcion3()
print(r)

# Una función que no tiene un return
# por default retorna None

r = funcion1()
print(r)

# Puede haber múltiples return en una
# función, pero el primero que alcance 
# va a ser el usado

def func():
	if 3 > 4:
		return "tres es mayor"
	else:
		return "tres es menor"

r = func()
print(r)