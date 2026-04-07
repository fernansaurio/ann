import numpy as np
import matplotlib.pyplot as plt

# Definimos las funciones usando np.exp para que funcionen con arreglos de números
def f(x):
    return (2 * np.exp(x**2)) - (5 * x)

def g(x):
    return 0.4 * np.exp(x**2)

def punto_fijo(x0, error_deseado):
    xi = x0
    error_calculado = 100
    k = 0
    max_iter = 50

    print(f"{'Iter':<5} | {'Raiz':<12} | {'Error':<12}")
    print("-" * 35)

    # El bucle debe ser controlado y NO llamar a la función a sí misma
    while k < max_iter and error_calculado > error_deseado:
        xn = g(xi)
        
        if xn == 0: break # Evitar división por cero
        
        error_calculado = abs((xn - xi) / xn)
        xi = xn
        k += 1
        print(f"{k:<5} | {xn:<12.6f} | {error_calculado:<12.6f}")

    print(f"\nResultado final: Raíz = {xi:.6f} en {k} iteraciones.")

# --- EJECUCIÓN ---

# 1. Llamamos al cálculo numérico
punto_fijo(0.5, 0.01) 

# 2. Generamos la gráfica DESPUÉS del cálculo
x = np.linspace(0, 1.5, 100) # Rango ajustado para ver el cruce
plt.figure(figsize=(8, 5))
plt.plot(x, f(x), "r", label="f(x) = 2e^(x²) - 5x")
plt.axhline(0, color='black', linestyle='--') # Línea del cero
plt.title("Método de Punto Fijo")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show() # Ahora sí se mostrará