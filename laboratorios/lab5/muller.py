import numpy as np
import pylab as plt
def muller(f, x0, x1, x2, tol=1e-6, max_iter=100):
	errors = []  # Lista para almacenar los errores en cada iteración
	for i in range(max_iter):
		# Calcular los coeficientes de la interpolación cuadrática inversa
		h0 = x1 - x0
		h1 = x2 - x1
		delta0 = (f(x1) - f(x0)) / h0
		delta1 = (f(x2) - f(x1)) / h1
		a = (delta1 - delta0) / (h1 + h0)
		b = a * h1 + delta1
		c = f(x2)
		# Calcular las raíces de la ecuación cuadrática
		discriminant = b**2 - 4*a*c
		if discriminant < 0:
			raise ValueError("No se puede calcular la raíz con estos puntos iniciales.")
		sqrt_discriminant = discriminant**0.5
		x3_plus = x2 - (2*c) / (b + sqrt_discriminant)
		x3_minus = x2 - (2*c) / (b - sqrt_discriminant)
		# Elegir la raíz más cercana a x2
		if abs(x3_plus - x2) < abs(x3_minus - x2):
			x3 = x3_plus
		else:
			x3 = x3_minus
		# Calcular el error
		error = abs((x3 - x2)/x3)*100
		errors.append(error)
		# Actualizar los valores para la siguiente iteración
		x0, x1, x2 = x1, x2, x3
		# Comprobar convergencia
		if error < tol:
			break
		print(f"Iteración {i+1}, Error: {error}, Raíz aproximada: {x3}")
	return x3, errors
# Ejemplo de uso
funcion_ejemplo = lambda x: x**3 - 13*x - 12  # aqui se modifica la ecuación
raiz_aproximada, errores = muller(funcion_ejemplo, 4.5, 5.5, 5)  # aqui se modifican los valores iniciales
print(f"Raíz aproximada: {raiz_aproximada:.6f}")