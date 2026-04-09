"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 4 - Asignacion 4

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar la librería compartida de C++
# Asegúrate de haber compilado previamente a libnewton.so
lib_path = os.path.abspath('./lib.so')
try:
    lib = ctypes.CDLL(lib_path)
except OSError:
    print(f"Error: No se pudo cargar {lib_path}.")
    exit()

# 2. Definir las firmas de la función de C++ para Python
# double newton_raphson(double x0, double tol, int max_iter, int* iters_used, double* history)
lib.newton_raphson.argtypes = [
    ctypes.c_double,                # x0
    ctypes.c_double,                # tol
    ctypes.c_int,                   # max_iter
    ctypes.POINTER(ctypes.c_int),   # puntero a iters_used
    ctypes.POINTER(ctypes.c_double) # puntero al arreglo history
]
lib.newton_raphson.restype = ctypes.c_double

# 3. Configurar parámetros iniciales
x0 = 5.0
tol = 0.001
max_iter = 100

# Variables por referencia para obtener datos de C++
iters_used = ctypes.c_int(0)
ArrayType = ctypes.c_double * (max_iter + 1)
history_array = ArrayType()

# 4. LLAMAR A LA LIBRERÍA C++
print("Ejecutando algoritmo en C++...")
raiz = lib.newton_raphson(x0, tol, max_iter, ctypes.byref(iters_used), history_array)

# Extraer los datos a una lista estándar de Python
n_iters = iters_used.value
x_vals = [history_array[i] for i in range(n_iters + 1)]

print(f"Raíz calculada: {raiz:.6f}")
print(f"Iteraciones completadas: {n_iters}")
print("Historial de pasos de x:", [round(x, 4) for x in x_vals])

# 5. Generar la Gráfica en Python
def f(x): return x**2 - 4
def df(x): return 2*x

x_range = np.linspace(0, 6, 400)
plt.figure(figsize=(8, 6))
plt.plot(x_range, f(x_range), label="f(x) = x^2 - 4", color="blue")
plt.axhline(0, color="black", linewidth=1)

# Dibujar las líneas de las iteraciones calculadas por C++
for i in range(n_iters):
    xi = x_vals[i]
    plt.plot(xi, f(xi), 'ro') # Punto en la curva
    plt.plot([xi, xi], [0, f(xi)], 'r--') # Línea de proyección al eje X
    
    # Línea tangente usando la derivada
    x_tangent = np.linspace(x_vals[i+1] - 0.5, xi + 0.5, 10)
    y_tangent = df(xi) * (x_tangent - xi) + f(xi)
    plt.plot(x_tangent, y_tangent, 'g--', alpha=0.6)

# Marcar el punto final de convergencia
plt.plot(raiz, 0, 'go', markersize=8, label=f"Raíz Final: {raiz:.4f}")

plt.title("Newton-Raphson: Backend en C++ / Visualización en Python")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()