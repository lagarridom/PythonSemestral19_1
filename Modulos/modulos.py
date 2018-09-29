# El módulo math nos da funciones y variables
# matemáticas básicas ya preestablecidas
import math
x = math.pi
y = math.e

print(x)
print(y)

print(math.cos(x))

print(math.factorial(4))

print(math.log(y))

# El módulo random da funciones con carácter
# aleatorio

# randint da un número entero aleatorio en un rango
# choice devuelve un elemento de un arreglo al azar
from random import choice,randint
lista = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
print(choice(lista))
print(choice(lista))
print(choice(lista))

print(randint(-5,5))
print(randint(-5,5))

# La principal función que nos brinda time
# es sleep, que nos permite detener la ejecución
# de un programa un determinado número de segundos
import time
print('Voy a detenerme 3 segundos')
time.sleep(3)
print('Terminé')