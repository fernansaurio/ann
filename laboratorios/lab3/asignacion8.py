"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 3 - Asignacion 8

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import numpy as np
import matplotlib.pyplot as plt

# Generar valores para x (evitamos el 0 porque ln(0) no está definido)
x = np.linspace(0.1, 3.0, 200)

# Calcular f(x) = ln(x^2) - 0.7
y = np.log(x**2) - 0.7

# Graficar
plt.figure(figsize=(7, 5))
plt.plot(x, y, label='f(x) = ln(x^2) - 0.7', color='green')
plt.axhline(0, color='red', linestyle='--', label='y = 0')
plt.title("Método Gráfico para ln(x^2) = 0.7")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()