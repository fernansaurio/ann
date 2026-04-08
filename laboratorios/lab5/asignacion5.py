import numpy as np
import matplotlib.pyplot as plt

def f(x): return 0.95*x**3 - 5.9*x**2 + 10.9*x - 6

# a) Gráfica
x_vals = np.linspace(0, 5, 200)
plt.plot(x_vals, f(x_vals), label="f(x)")
plt.axhline(0, color="red", linestyle="--")
plt.title("Búsqueda de la raíz más grande")
plt.grid(True); plt.legend(); plt.show()

# b) Método de la Secante (3 iteraciones)
print("--- b) Método de la Secante ---")
xa = 2.5
xb = 3.5
for i in range(1, 4):
    xc = xb - f(xb)*(xb - xa)/(f(xb) - f(xa))
    error = abs((xc - xb)/xc)*100
    print(f"Iter {i}: x_i+1 = {xc:.6f}, Error = {error:.4f}%")
    xa, xb = xb, xc

# c) Método de la Secante Modificada (3 iteraciones)
print("\n--- c) Secante Modificada ---")
xi = 3.5
delta = 0.01
for i in range(1, 4):
    f_xi = f(xi)
    f_xidelta = f(xi + delta*xi)
    xi_next = xi - (delta * xi * f_xi) / (f_xidelta - f_xi)
    error = abs((xi_next - xi)/xi_next)*100
    print(f"Iter {i}: x_i+1 = {xi_next:.6f}, Error = {error:.4f}%")
    xi = xi_next