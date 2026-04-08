import numpy as np
import matplotlib.pyplot as plt

# Función del ejercicio de Müller f(x) = x^3 - 13x - 12
def f(x):
    return x**3 - 13*x - 12

x = np.linspace(-4, 5, 400)
plt.figure(figsize=(8, 5))
plt.plot(x, f(x), label="f(x) = x³ - 13x - 12", color="purple")
plt.axhline(0, color="red", linestyle="--")
plt.grid(True)
plt.title("Gráfica para el Método de Müller")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()