
# Las listas son secuencias que pueden contener
# cualquier tipo de dato
# Se crean utilizando corchetes
lista1 = [3,True,"hola",4+3j]

# Estas pueden incluso contener otras listas
lista2 = [4,5,7,["hola",3,4.5]]

# Accedemos a sus elementos de la misma forma 
# que con las cadenas de texto

print(lista1[2])		
print(lista2[3][2])		
print(lista1[-1])		

print(lista1[1:3])		

lista3 = ["Lunes","Martes"]

# Podemos realizar ciertas operaciones aritméticas con ellas
print(lista3*4)			
print(lista3 + ["Miercoles","Juebebes"])

# Podemos modificar el tamaño de las listasd
# Con el método append agregamos un elemento al final de esta
lista4 = [10,9,8,9,10,7]
lista4.append(6)
print(lista4)

# Con el método count contamos el número de veces que aparece
# un elemento en la lista
print(lista4.count(9))

# Con reverse invertimos el orden de la lista
lista5 = ["uno","dos","tres"]
lista5.reverse()
print(lista5)

calificaciones = [10,4,8,11,9,8]

# Con sort ordenamos los elementos de la lista por su valor
calificaciones.sort()

print(calificaciones)
calificaciones.reverse()
print(calificaciones)

num = calificaciones.count(8)
print(num)

lista = [1,2,3,4,5,6]

# Podemos eliminar elementos de una lista con pop
# Si no ponemos nada entre los paréntesis, por default
# elimina el último elemento de la lista
lista.pop()
print(lista)

# Podemos dar la posición del elemento que queremos eliminar
lista.pop(1)
print(lista)
# [1,3,4,5]

# Podemos almacenar el elemento que se está eliminando en una variable
elemento = lista.pop(0)
print(elemento)
print(lista)

listaL = ["a", "b", "c"]

# Los elementos de la lista se pueden modificar después de haber sido creada
listaL[1] = "D"
print(listaL)