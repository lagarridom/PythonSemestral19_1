class Empleado:
	def __init__(self, nombre, trabajo = "Asistente", salario=100):
		self.nombre = nombre
		self.trabajo = trabajo
		self.salario = salario

	# Este método mágico define que se va a imprimir cuando se trata de imprimir un objeto
	# print(objeto)
	def __str__(self):
		return "Nombre: "+self.nombre+"\nTrabajo: "+self.trabajo+"\nSalario: "+str(self.salario)

	def darAumento(self,porcentaje):
		self.salario *= 1+porcentaje

	def despedir(self):
		self.trabajo = "Ninguno"
		self.salario = 0

class Gerente(Empleado):
	def __init__(self,nombre,salario):
		Empleado.__init__(self,nombre,"Gerente",salario)
		# Al heredar de una clase, se puede hacer uso de los métodos 
		# con los que se contaba y extender su funcionamiento de esta forma
		# Aquí estamos especificando que el trabajo va a ser gerente

	def darAumento(self,porcentaje,bonus = .1):
		Empleado.darAumento(self,porcentaje + bonus)
		# Estamos utilizando el método darAumento de empleado y estamos
		# agregando un bono por ser gerente


# Departamento va a ser una agrupación de trabajadores
class Departamento:
	def __init__(self,*args):
		self.miembros = list(args)

	def darAumentos(self,porcentaje):
		for miembro in self.miembros:
			miembro.darAumento(porcentaje)

	# Definimos que al sumar dos departamentos, nos va a devolver un nuevo
	# departamento que contenga la suma de los trabajadores
	def __add__(self,dep2):
		return Departamento(*(self.miembros + dep2.miembros))
		# El asterísco en la línea anterior es utilizado para realizar algo llamado
		# desempaquetamiento.
		# Departamento recibe una serie de objetos
		# Departamento(obj1,obj2,obj3,obj4,ojb5)
		# self.miembros es una lista de objetos -> [obj1,obj2,obj3]
		# dep2.miembros es otra lista de objetos -> [obj4,obj5]
		# si sumamos estos nos da una lista conjunta -> [obj1,obj2,obj3,obj4,obj5]
		# si colocasemos esta lista en la creación de departamento nos daría un error
		# Departamento([obj1,obj2,obj3,obj4,obj5]) -> ERROR
		# Si colocamos un asterísco antes se realiza un desempaquetamiento de lista
		# Departamento(*[obj1,obj2,obj3,obj4,obj5])-> Departamento(obj1,obj2,obj3,obj4,obj5)

	def darMiembros(self):
		return [miembro.nombre for miembro in self.miembros]
