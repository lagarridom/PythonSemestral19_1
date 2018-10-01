from trabajadores import Empleado, Gerente, Departamento

empleado1 = Empleado("Luis","Diseñador",200)
empleado2 = Empleado("Ana","Contadora",300)
empleado3 = Empleado("Pedro")

print(empleado2)
print(empleado3)

empleado3.darAumento(.2)
print(empleado3)
print(empleado3.salario)

print(empleado1)

empleado1.despedir()

print(empleado1)

gerente1 = Gerente("Verónica",600)
print(gerente1)
gerente1.darAumento(.1)
print(gerente1)

administracion = Departamento(empleado2,empleado3,gerente1)

empleado4 = Empleado("Guillermo","Economista",350)
empleado5 = Empleado("Jessica")
gerente2 = Gerente("Rodrigo",600)

contaduria = Departamento(empleado4,empleado5,gerente2)

for i in [empleado4,empleado5,gerente2]:
	print(i.nombre," gana: ",i.salario)

contaduria.darAumentos(.1)

for i in [empleado4,empleado5,gerente2]:
	print(i.nombre,"Ahora gana: ",i.salario)

print(administracion.darMiembros())
print(contaduria.darMiembros())

economia = administracion + contaduria

print(economia.darMiembros())