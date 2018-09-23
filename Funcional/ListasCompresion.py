import math
#Listas por compresion
lista = [1, 5, 8, 5, 9, 5,10]
lista2= [i**2 for i in lista] #A cada elemento de la lista, lo eleva al cuadrado
lista3 = [math.sqrt(i) for i in lista2] #A cada elementos de la lista dos, saca su raiz cuadrada
lista4 = [i for i in lista2 if i%2==0] #Agrega solo numeros pares
print(lista)
print(lista2)
print(lista3)
print(lista4)