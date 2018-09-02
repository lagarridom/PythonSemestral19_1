"""
Contiene el uso de un booleano
"""

  # Constantes definidas por defecto
"""
  None representa vacio -> Nonetype ---- Se asemeja al null ó nul de otros lenuajes
  True posee valor de verdadero -> tipo Bool
  False posee valor de falso -> tipo Bool -> None, 0, "", [], (), {}

"""
  # Carcteristicas y definicion del booleano
"""
Un booleano es un tipo de dato que solo posee dos
valores verdadero (True) y falso (False)
"""
variable = None
print(variable)
tipo_variable = type(variable)
print(variable)

booleano = True

# OPERADORES DE ORDEN, COMPARACION, O BOOLEANOS
#
# operandos: variables del mismo tipo de datos
# resultado: bool
#
"""
==  si a == b entonces True caso contrario False
!=  si a != b entonces True caso contrario False
<   si a < b entonces True caso contrario False
>   si a > b entonces True caso contrario False
<=  si a <= b entonces True caso contrario False
>=  si a >= b entonces True caso contrario False

Expresion booleana es un conjunto de
operadores booleados con ciertos datos
da como resultado un booleano
"""

num1 = 4
num2 = 5
booleano = 4 > 5
# Probar con cada uno

# OPERADORES LOGICOS Ó RELACIONALES
#
# OPERADOR: BOOL
# RESULTADO: BOOL
#
"""
and     a and b     si los dos son True regresa True
or      a or b      si por lo menos uno es True regresa True
not     not a       regresa lo opuesto a a
Expresion relacional conjunto de operadores RELACIONALES
con datos comportados como booleanos
da como resultado un booleano
"""
True and True
True and False
True and False and True
True and 0

True or False
False or False

False or False or True

not False

#Determinar un numero impar
num = 10
booleano = num % 2 != 0

# Ejercicio 1 - Quiero un numero par mayor a 5
numero_de_prueba = 4
numero_de_prueba % 2 == 0 and numero_de_prueba > 5
