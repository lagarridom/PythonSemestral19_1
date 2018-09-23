def darSalario(horas, dias,puesto = "Trabajador"):
	if puesto == "Jefe":
		return dias * horas * 700
	elif puesto == "Administrador":
		return dias * horas * 500
	elif puesto == "Trabajador":
		return dias * horas * 400
	else:
		return "Puesto inexistente"


s1 = darSalario(6,5,"Jefe")
s2 = darSalario(7,6)
s3 = darSalario(7,6,"Administrador")
s4 = darSalario(7,3,"Jugador de basket")

print(s1, s2, s3,  s4)





























