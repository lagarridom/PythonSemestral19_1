"""
Podemos pedir datos por teclado
y podemos imprimir datos
"""
entrada = input()  # Permite leer desde el teclado
print(entrada)  # Permite imprimir en pantalla

entrada2 = input("Dime algo:")  # Puede recibir una cadena a mostrar
tipo_entrada2 = type(entrada2)
print("Entrada: {} Tipo: {}".format( entrada2, tipo_entrada2))

###podemos configurar print
print("a","b","c", sep="**", end="\n\n\n")

##intentamos sumar dos numeros capturados por teclado
num1 = input("Dame un numero:")
num2 = input("Dame otro numero:")
suma = num1 + num2
print("la suma de los numeros es: {}".format(suma))


#CASTEO
"""
Castear consiste en convertir una variable asociada a un tipo de dato
especifico a otra variable asociada a otro tipo de dato
"""
#Ejemplos de casteo
num = "3"
num_bueno = int(num)

num = "3.5"
num_bueno = float(num)

num = 4
num_cadena = str(num)

#complejo
complejo = complex(num_bueno)
real = 3
imaginario = 4.4
complejo = complex(real, imaginario)  # No soporta cadenas
complejo.conjugate()
complejo.real
complejo.imag

###Ahora si se viene lo chido
num1 = int(input("Dame un numero:"))
num2 = int(input("Dame otro numero:"))
suma = num1 + num2
print("la suma de los numeros es: {}".format(suma))
