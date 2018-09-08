#7.-
"""
while CONDICION:
    instrucciones
"""


"""
Desarroolllar un programa que muestre los primeros n numeros naturales
tomando en cuenta al 0 como primer numero natural
"""

n = int(input("Dame un numero natural: "))
i = 0
while i <= n:
    print(i)
    i += 1  # Contador porque incrementa en un cada iteración
    # Su valor es igual a i mas 1


##Mostrar todos los numeros excepto el 5
n = int(input("Dame un numero natural: "))
i = -1
while i < n:
    i += 1
    if i == 5:
        continue
    print(i)

##Mostrar todos los numeros excepto el 5 como maximo 10 sin importar n

n = int(input("Dame un numero natural: "))
i = -1
while i < n:
    i += 1
    if i == 5:
        continue
    print(i)
    if i == 10:
        break
