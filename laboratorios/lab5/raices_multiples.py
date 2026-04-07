import numpy as np
import pylab as plt
def newton_raphson_modificado(funcion, derivada_primera,
derivada_segunda, x_inicial, tolerancia=0.1,
max_iteraciones=1000):
	tabla_iteraciones = []
	xi = x_inicial
	for i in range(max_iteraciones):
		f_xi = funcion(xi)
		f_prime_xi = derivada_primera(xi)
		f_double_prime_xi = derivada_segunda(xi)
		xnuevo = xi - (f_xi * f_prime_xi) / (f_prime_xi**2 - f_xi
		* f_double_prime_xi)
		error = abs(xnuevo - xi)/xnuevo*100
		tabla_iteraciones.append([xi, error])
		if error < tolerancia:
			break
		xi = xnuevo
	raiz_aproximada = tabla_iteraciones[-1][1]
	print("\nRaíz:", xi)
	return raiz_aproximada, tabla_iteraciones
# Ejemplo de uso:
def funcion_ejemplo(x):
	return x**3 - 5*x**2 + 7*x - 3 #modificar la ecuacion
def derivada_primera_ejemplo(x):
	return 3*x**2 - 10*x + 7 #modificar las derivadas
def derivada_segunda_ejemplo(x):
	return 6*x - 10 #modificar las derivadas
raiz, tabla = newton_raphson_modificado(funcion_ejemplo,
derivada_primera_ejemplo, derivada_segunda_ejemplo,
x_inicial=0) #modificar el valor inicial
# Imprimir resultados
print("\nTabla de iteraciones:")
print("[xi, error]")
for i, iteracion in enumerate(tabla):
	print(f"Iteración {i + 1}: {iteracion}")
x=np.linspace(0,4)
plt.plot(x, (funcion_ejemplo(x)), 'r')
plt.show()