class Empleado:
# Cada empleado recibirá un salario normal hasta las 48 horas
# Si trabaja más de 48 horas, se considerará como horas
# extra que tendrán un sueldo por hora diferente

	def __init__(self, SUELDOHN, SUELDOHE):
		self.sueldoHN = SUELDOHN
		self.sueldoHE = SUELDOHE
		self.horas = 0

	def trabajar(self,HORAS):
		print('Estoy trabajando...')
		self.horas += HORAS

	def ConsoltarPaga(self):
		if self.horas <= 48:
			return self.horas * self.sueldoHN
		else:
			return 48 * self.sueldoHN + (self.horas - 48) * self.sueldoHE


empleado1 = Empleado(400,500)
empleado2 = Empleado(500,600)

print('Sueldo1 :',empleado1.ConsoltarPaga())
empleado1.trabajar(10)
print('Sueldo1 :',empleado1.ConsoltarPaga())
empleado1.trabajar(38)
print('Sueldo1 :',empleado1.ConsoltarPaga())
empleado1.trabajar(3)
print('Sueldo1 :',empleado1.ConsoltarPaga())
empleado2.trabajar(20)
print('Sueldo2 :',empleado2.ConsoltarPaga())

print(empleado1.horas)