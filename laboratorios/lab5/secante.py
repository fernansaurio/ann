import numpy as np
import pylab as plt
def secante(f, x_a, x_b, tolerancia=0.1, max_iteraciones=1000):
	tabla = []
	for i in range(max_iteraciones):
		f_a = f(x_a)
		f_b = f(x_b)
		x_c = x_a - f_a * (x_b - x_a) / (f_b - f_a)
		error = abs(x_c - x_a)
		tabla.append([x_a, x_b, x_c, error])
		if error < tolerancia:
			break
		x_a, x_b = x_b, x_c
	raiz_aproximada = tabla[-1][2]
	return raiz_aproximada, tabla
# Ejemplo de uso:
def funcion_ejemplo(x):
	return -0.4*x**2 + 2.3*x + 2.2  # Función de ejemplo
raiz, tabla_iteraciones = secante(funcion_ejemplo, 6, 7)
#modificar los valores iniciales
# Imprimir resultados
print("\nTabla de iteraciones:")
print("[xa, xb, xc, error]")
for i, iteracion in enumerate(tabla_iteraciones):
	print(f"Iteración {i + 1}: {iteracion}")
x=np.linspace(-5,10)
plt.plot(x, (funcion_ejemplo(x)), 'r')
plt.show()