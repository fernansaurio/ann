"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 5 - Asignacion 6

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

def muller_complex(f, x0, x1, x2, iters=5):
    print(f"\nValores Iniciales: {x0}, {x1}, {x2}")
    for i in range(iters):
        h1, h2 = x1 - x0, x2 - x1
        d1, d2 = (f(x1) - f(x0))/h1, (f(x2) - f(x1))/h2
        a = (d2 - d1)/(h2 + h1)
        b = a*h2 + d2
        c = f(x2)
        
        disc = cmath.sqrt(b**2 - 4*a*c)
        den = b + disc if abs(b + disc) > abs(b - disc) else b - disc
        
        x3 = x2 - (2*c)/den
        error = abs((x3 - x2)/x3)*100
        print(f"Iter {i+1}: Raíz = {x3.real:.6f}, Error = {error:.4f}%")
        x0, x1, x2 = x1, x2, x3

# a) f(x) = x^3 + x^2 - 3x - 5
def fa(x): return x**3 + x**2 - 3*x - 5
print("--- Müller a) f(x) = x³ + x² - 3x - 5 ---")
muller_complex(fa, 1.0, 2.0, 2.5) # Raíz real cercana a ~2.0

# b) f(x) = x^3 - 0.5x^2 + 4x - 3
def fb(x): return x**3 - 0.5*x**2 + 4*x - 3
print("\n--- Müller b) f(x) = x³ - 0.5x² + 4x - 3 ---")
muller_complex(fb, 0.0, 0.5, 1.0) # Raíz real positiva cercana a ~0.76

# Gráficas
x = np.linspace(-2, 3, 200)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(x, fa(x)); ax[0].axhline(0, color='red'); ax[0].set_title("Ecuación A"); ax[0].grid()
ax[1].plot(x, fb(x)); ax[1].axhline(0, color='red'); ax[1].set_title("Ecuación B"); ax[1].grid()
plt.show()