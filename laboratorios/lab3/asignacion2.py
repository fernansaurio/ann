"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 3 - Asignacion 2

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función
x = np.linspace(-3, 8, 100)
y = -0.5 * x**2 + 2.5 * x + 4.5

# Graficar
plt.plot(x, y)
plt.axhline(0, color='red') # Línea en y=0
plt.title("Método Gráfico: f(x) = -0.5x^2 + 2.5x + 4.5")
#plt.show()
plt.savefig("grafico_asignacion2.png")