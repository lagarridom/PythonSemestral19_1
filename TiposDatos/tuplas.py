# Las tuplas son muy parecidas a las listas,
# estas se crean utilizando paréntesis

# La principal diferenia entre las tuplas y las listas es
# que una vez creada, las tuplas no se pueden modificar
tupla = (3,4+3j,True,[1,2,3],"Hola")
# Accedemos a sus elementos de la misma forma que con las listas
print(tupla[2])

tupla2 = (1,2,3,4)
print(tupla2[-1])
# No se puede reasignar sus elementos
#tupla2[-1] = 5 

# Podemos realizar operaciones aritméticas con ellas
print(tupla2 * 3)

# Las tuplas también se pueden crear sin poner los paréntesis
tupla3 = "hola",3,"QUE!"


print(tupla3)

# Podemos asignar los elementos de una tupla a los de otra
# Este método sirve para crear nuevas variables de forma rápida
a,b,c = 2,4,5
# (a,b,c) = (2,4,5)
# a = 2
# b = 4
# c = 5

print(a)
# También se puede realizar con listas
[d,e,f] = [3,4,5]

print(d)
