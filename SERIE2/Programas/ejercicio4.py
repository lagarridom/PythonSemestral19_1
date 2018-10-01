class NumeroComplejo:

	def __init__(self, parteReal, parteImaginaria):
		self.parteReal = parteReal
		self.parteImaginaria = parteImaginaria

	def imprimirComplejo(self):
		print(str(self.parteReal) + '+' + str(self.parteImaginaria) + '*i')

	def __add__(self, numeroC):
		real = self.parteReal + numeroC.parteReal
		img = self.parteImaginaria + numeroC.parteImaginaria

		return NumeroComplejo(real, img)



real = float(input('Introduzca parte real del nuevo número: '))
img = float(input('Introduzca la parte imaginaria del nuevo número: '))

complejo = NumeroComplejo(real, img)
complejo.imprimirComplejo()

real = float(input('Introduzca parte real del nuevo número: '))
img = float(input('Introduzca la parte imaginaria del nuevo número: '))
complejo2 = NumeroComplejo(real, img) 
complejo2.imprimirComplejo()

sumaComplejoyComplejo2 = complejo + complejo2
sumaComplejoyComplejo2.imprimirComplejo()