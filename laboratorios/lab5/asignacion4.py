"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 5 - Asignacion 4

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import numpy as np
import matplotlib.pyplot as plt

# Función con raíz doble en x=2 (Corregido signo para que de cero en x=2)
def f(x): return x**3 - 2*x**2 - 4*x + 8
def df(x): return 3*x**2 - 4*x - 4
def ddf(x): return 6*x - 4

x0_nr = 1.2
x0_mod = 1.2
tol = 1e-5

print("--- a) N-R Estándar ---")
for i in range(1, 20):
    x1 = x0_nr - f(x0_nr)/df(x0_nr)
    error = abs((x1 - x0_nr)/x1)*100
    print(f"Iter {i}: x = {x1:.6f}, Error = {error:.6f}%")
    if error < tol: break
    x0_nr = x1

print("\n--- b) N-R Modificado (Raíces Múltiples) ---")
for i in range(1, 20):
    num = f(x0_mod) * df(x0_mod)
    den = df(x0_mod)**2 - f(x0_mod)*ddf(x0_mod)
    x1 = x0_mod - (num/den)
    error = abs((x1 - x0_mod)/x1)*100
    print(f"Iter {i}: x = {x1:.6f}, Error = {error:.6f}%")
    if error < tol: break
    x0_mod = x1

print("\nAnálisis: El N-R Modificado converge a la raíz exacta en muchas menos iteraciones porque compensa la derivada que tiende a cero en las raíces dobles.")

# Gráfica
x = np.linspace(0, 3, 200)
plt.plot(x, f(x), label="f(x) = x³ - 2x² - 4x + 8")
plt.axhline(0, color="red", linestyle="--")
plt.title("Raíz Múltiple (Tangente al eje X en x=2)")
plt.grid(True)
plt.legend()
plt.show()