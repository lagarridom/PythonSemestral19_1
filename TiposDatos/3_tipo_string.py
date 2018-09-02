# CADENAS Y CARACTERES

# CARACTER
"""
caracter: Representacion de un simbolo tipografico (letra mayuscula
            minuscula, signo de puntuacion, digito de un num, etx)
Cada caracter esta definido en una tabla llamada ASCII
***MOSTRAR TABLA ascii***
Funciones asociadas a ASCII
int ord(str)
    recibe un caracter y regresa su numero en ascci
str chr(int)
    recine un caracter
"""
#FUNCIONES PARA TRABAJAR CON ASCII
print(ord("3"))
print(chr(65))

"""
En diversos lenguajes existe el tipo CHAR
y el conjunto de char se le conoce como un
string,
en python no existe el char, solo los strings
y estos nos permiten almacenar tanto cadenas de texto
como CHAR
"""

# Formas de declarar una cadena
cadena = "texto"
cadena2 = 'texto'
char = "a"
char2 = 'b'

print(type(char))

repeticion_de_a = "a" * 5
print(repeticion_de_a)
repeticion_de_ab = "ab" * 6

# Concatenacion de cadenas
texto = "asi " + " se concatenan cadenas"
texto1 = "Jesus "
texto2 = "y"
texto3 = " Maria"
texto_final = texto1 + texto2 + texto3
print(texto)
print(texto_final)

#busqueda ***Explicar que es un metodo***
num_veces = texto_final.count("a")
indice = texto.find("cad")
indice2 = texto.find("cad",0,5)
print(num_veces)
print(indice)
print(indice2)

#Comparacion
"texto" == "texto"
booleano = texto == texto_final
booleano2 = texto < texto_final  # Compara por ASCII
print(booleano)
print(booleano2)

#Longitud de una cadena
longitud_texto = len(texto)
print(longitud_texto)

#Acceder a un caracter
ejemplo = "abcdefg"
ejemplo[2]
ejemplo[:]
ejemplo[:3]
ejemplo[2:]

#acceder a un intervalo

#Funciones Chidas
"spam, eggs, ham".split(", ")
## separa por un una cadena concreta

a = ", ".join(["spam", "eggs", "ham"])
##une las cadenas de la lista por medio de la cadena ", "

"Hello ME".replace("ME", "world")
##remplaza una cadena por otra

"This is a sentence.".startswith("This")
##empieza con This

"This is a sentence.".endswith("sentence.")
##termina con sentence.

"This is a sentence.".upper()
##convierte la cadena a mayusculas

"AN ALL CAPS SENTENCE".lower()
##convierte la cadena a minusculas

#Formato
entero = 2
real = 4.5
complejo = 4 + 4.5j
texto_formato = "entero: {}\nreal: {}\ncomplejo: {}\n".format(entero,real,complejo)
print(texto_formato)

"""
caracteres especiales:
\n salto de linea
\t tabulador
\\ diagonal invertida
\" comilla doble
\' comilla simple
"""

import string
string.digits  # Todos los digitos
string.ascii_letters  # Todas las letras ASCII
