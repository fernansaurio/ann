import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -0.5 * x**2 + 2.5 * x + 4.5

x = np.linspace(-3, 8, 400)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = -0.5x^2 + 2.5x + 4.5', color='blue', linewidth=2)
plt.axhline(y=0, color='red', linestyle='--', label='Eje X (y=0)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.xlabel('Valores de x')
plt.ylabel('Valores de f(x)')
plt.title('Gráfica detallada de la función')
plt.legend()
plt.show()