#Metodo grafico

import numpy as np
import matplotlib.pyplot as plt

# ---  DEFINICIÓN DE LA FUNCIÓN ---
def f(x):
    # Punto 1: Ecuación cuadrática 
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5.0  

# ---  GENERAR PUNTOS PARA LA GRÁFICA ---
# Ajustar este rango según la función (Punto 1 usa -5 a 10)
x = np.linspace(-5, 10, 500) 
y = f(x)

# --- CREACIÓN DE LA GRÁFICA ---
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'Curva de $f(x)$', color='blue', linewidth=2)

# Ejes principales resaltados
plt.axhline(0, color='black', linewidth=1.5) # Eje X (Raíces)
plt.axvline(0, color='black', linewidth=1)   # Eje Y


# --- CONFIGURACIÓN DE TÍTULOS CON LATEX ---
plt.title(r"Gráfica de la función: $f(x) = 2x^3 - 11.7x^2 + 17.7x - 5.0$", fontsize=14)
plt.xlabel(r"$x$ (Variable independiente)", fontsize=12)
plt.ylabel(r"$f(x)$ (Imagen)", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()