import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y sus derivadas
def f(x): return x**3 + 2*x**2 - 4*x + 8
def df(x): return 3*x**2 + 4*x - 4
def d2f(x): return 6*x + 4

def newton_estandar(x0, tol=1e-5, max_iter=10):
    puntos = [x0]
    for _ in range(max_iter):
        x_next = x0 - f(x0)/df(x0)
        puntos.append(x_next)
        if abs(x_next - x0) < tol: break
        x0 = x_next
    return puntos

def newton_modificado(x0, tol=1e-5, max_iter=10):
    puntos = [x0]
    for _ in range(max_iter):
        # Fórmula para raíces múltiples sin conocer m
        denominador = df(x0)**2 - f(x0)*d2f(x0)
        x_next = x0 - (f(x0)*df(x0)) / denominador
        puntos.append(x_next)
        if abs(x_next - x0) < tol: break
        x0 = x_next
    return puntos

# Parámetros iniciales
x_inicio = 1.2
hist_estandar = newton_estandar(x_inicio)
hist_modificado = newton_modificado(x_inicio)

# Graficación
x_vals = np.linspace(-4, 3, 400)
plt.figure(figsize=(10, 5))
plt.plot(x_vals, f(x_vals), label='f(x)', color='black', linewidth=1.5)
plt.axhline(0, color='red', linestyle='--')
plt.plot(hist_estandar, [f(x) for x in hist_estandar], 'o-', label='N-R Estándar')
plt.plot(hist_modificado, [f(x) for x in hist_modificado], 's--', label='N-R Modificado')

plt.title("Comparación: Newton-Raphson Estándar vs Modificado")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

print(f"Raíz Estándar: {hist_estandar[-1]:.6f} en {len(hist_estandar)-1} iteraciones")
print(f"Raíz Modificado: {hist_modificado[-1]:.6f} en {len(hist_modificado)-1} iteraciones")