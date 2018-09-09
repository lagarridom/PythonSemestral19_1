# En modo de apertura a
# puntero inicia al final del archivo

#archivo = open('arch2.txt','a')
archivo = open('arch2.txt','a+')
# append siempre escribe al final
archivo.write('Otro Final\n')
texto1 = archivo.read()
print(texto1) # Ver que no imprime nada

archivo.seek(0)
texto2 = archivo.read()
print(texto2)

archivo.seek(0)
print(archivo.readlines())

archivo.seek(0)
lineas = archivo.readlines()
print(lineas[0])

archivo.close()