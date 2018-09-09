# En modo de apertura 'a'
# puntero inicia al final del archivo

#archivo = open('arch2.txt','a')
archivo = open('arch2.txt','a+') # Podemos escribir y leer
# append siempre escribe al final
archivo.write('Otro Final\n')
texto1 = archivo.read()
print(texto1) # No imprime nada porque el
# puntero está hasta el final


# Movemos puntero al inicio
archivo.seek(0)
texto2 = archivo.read()
print(texto2) # Imprime texto del archivo


archivo.seek(0)
lineas = archivo.readlines() # Creamos lista con líneas de archivo
print(lineas)
print(lineas[0])

archivo.close()
