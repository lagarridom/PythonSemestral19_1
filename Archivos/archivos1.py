# Metodos de apertura
# w -> Abre archivo para escritura, en caso de ya
# 	   existir, borra todo su contenido
# r -> Abre archivo para lectura, en caso de que no
#	   exista, hay una excepción
# a -> Abre archivo para escritura, en caso de no
#	   existir, lo crea, en caso de que ya existiera 
#	   permite la escritura pero esta es SIEMPRE AL
#	   FINAL DEL ARCHIVO
# + -> Permite que el archivo sea tanto de escritura
#	   como de lectura ("w+","r+","a+")


# Antes de poder usar este código necesitamos
# crear un archivo con texto de prueba llamado 
# arch1.txt
archivo1 = open("arch1.txt")
# archivo = open("prueba1.txt","r")

# Abrimos el archivo llamado 'prueba1.txt'
# en modo de lectura
texto = archivo1.read()
print(texto)
# archivo.write("Otra cosa") -> Error


archivo2 = open("arch2.txt",'w')
# Creamos o sobreescribimos archivo llamado
# 'prueba2.txt' en modo de escritura


texto2 = "Texto 2\nSigo sin saber\nque decir\n"
archivo2.write(texto2)
archivo2.write("Final\n")
#archivo2.read() -> Error
# En general, cuando acabemos de trabajar con un
# archivo guardamos y cerramos

# En python es igual
archivo1.close()
archivo2.close()
