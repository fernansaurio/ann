import ctypes
import numpy as np
import matplotlib.pyplot as plt

# 1. Carga de la librería compilada en C++
# Asegúrate de haber recompilado con: g++ -fPIC -shared -o ejercicio3new.so Ejercicio3.cpp
lib = ctypes.CDLL('./ejercicio3new.so')
lib.calcular_newton.argtypes = [ctypes.c_double, ctypes.c_double]
lib.calcular_newton.restype = ctypes.c_double

# 2. Definición de la función de ejecución
def ejecutar_newton(x0, error):
    """
    Función para llamar al cálculo en C++ y mostrar resultados.
    Parámetros:
    x0    -> Valor inicial (semilla) para empezar a buscar la raíz.
    error -> Tolerancia de error porcentual para detenerse (ej. 0.001).
    """
    # Llamada al cálculo pesado en C++
    raiz_hallada = lib.calcular_newton(x0, error)
    
    print(f"Raíz calculada en C++: {raiz_hallada:.6f}")
    return raiz_hallada

# 3. Definición de la función matemática para graficar
def f_py(x):
    # f(x) = 2*sen(sqrt(x)) - x (Ejercicio 1 y 3)
    return 2 * np.sin(np.sqrt(x)) - x

# --- PARÁMETROS DE CAMBIO ---
# Cambiamos x0 a 2.0 para evitar que la derivada "dispare" el valor a negativos
valor_x0 = 2.0        # Punto de partida (Cambiable)
error_deseado = 0.001 # Error objetivo 0.001% (Cambiable) 

# Ejecución
raiz = ejecutar_newton(valor_x0, error_deseado)

# 4. Generación de la Gráfica Visual
x_vals = np.linspace(0.1, 4, 500) # Rango de visualización en el eje X
y_vals = f_py(x_vals)

plt.figure(figsize=(10, 6))
# Usamos r'' para evitar el SyntaxWarning de LaTeX
plt.plot(x_vals, y_vals, label=r'$f(x) = 2sen(\sqrt{x}) - x$', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Marcar raíz encontrada (Punto Rojo)
plt.scatter([raiz], [0], color='red', zorder=5, s=100)
plt.annotate(f' Raíz: {raiz:.6f}', (raiz, 0.1), color='red', fontweight='bold')

plt.title("Método de Newton-Raphson - Visualización (Lab 4)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, linestyle='--')
plt.legend()

# Ajustamos los límites de la gráfica para ver la raíz real
plt.xlim(0, 4) 
plt.ylim(-2, 1)

plt.show()