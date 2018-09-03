# diccionario = {}
# Los diccionarios no son secuencias, a estos se les considera como mapeos
# Estos estan conformados por elementos, y a su vez, estos elementos están 
# conformados por una llave y un valor
diccionario = {"luis":8,"pato":7,"gabriel":10}
# El primer elemento tiene la llave "luis" y el valor 8

# Para acceder a sus elementos se realiza de forma similar a como se hace 
# con las listas, pero en vez de poner la posición del elemento, se pone
# la llave de este
print(diccionario["gabriel"])

# Se pueden crear nuevos elementos asignando un valor a una llave que no exista
diccionario["susana"] = 9
print(diccionario)

# Los diccionarios pueden tener como llave cualquier objeto inmutable
# Los diccionarios pueden tener cualquier objeto como valor
diccionario = {(1,2,3):[3,6,5],"hola":"a",4:"b"}

print(diccionario[(1,2,3)])

diccionario = {"a":1,"b":2}

# get
# Nos regresa el valor de el elemento con la llave
# especificada, de no encontrarla, regresa el valor por default
print(diccionario.get("a",10))
print(diccionario.get("c",10))

# items nos da los elementos del diccionario
print(diccionario.items())
# keys nos da las llaves del diccionario
print(diccionario.keys())
# values nos da los valores del diccionario
print(diccionario.values())

# Con pop podemos eliminar elementos del diccionario, en los paréntesis
# colocamos la llave del elemento que queremos eliminar
diccionario.pop("a")
print(diccionario)



