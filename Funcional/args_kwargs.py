# Podemos especificar que un parámetros
# va a recibir múltiples valores poniendo
# un * antes de su nombre
def func(a,*c):
	print(a)
	print(c)

func(2,4,1,2,5,7,"hola")

# Por lo general, a esta variable se le 
# nombra args
def func(a,*args):
	print(a)
	print(c)


# Podemos especificar un parámetro que
# va a recibir los argumentos por llave
# que sobren, se nombran kwargs por
# convención y se colocan dos * antes de su
# nombre
def func(a,b,**kwargs):
	print(a)
	print(b)
	print(kwargs)

func(2,4,p=2,h=3,g=20)





