import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.95*x**3 - 5.9*x**2 + 10.9*x - 6

def secante_estandar(x_prev, x_curr, iteraciones):
    print("--- Método de la Secante (Estándar) ---")
    print(f"{'Iter':<5} | {'xi':<10} | {'f(xi)':<12}")
    
    for i in range(1, iteraciones + 1):
        fx_prev = f(x_prev)
        fx_curr = f(x_curr)
        
        x_next = x_curr - (fx_curr * (x_curr - x_prev)) / (fx_curr - fx_prev)
        print(f"{i:<5} | {x_next:<10.5f} | {f(x_next):<12.5f}")
        
        x_prev = x_curr
        x_curr = x_next
    return x_curr

def secante_modificado(x_curr, delta, iteraciones):
    print("\n--- Método de la Secante (Modificado) ---")
    print(f"{'Iter':<5} | {'xi':<10} | {'f(xi)':<12}")
    
    for i in range(1, iteraciones + 1):
        fx_curr = f(x_curr)
        dx = delta * x_curr
        fx_dx = f(x_curr + dx)
        
        x_next = x_curr - (dx * fx_curr) / (fx_dx - fx_curr)
        print(f"{i:<5} | {x_next:<10.5f} | {f(x_next):<12.5f}")
        
        x_curr = x_next
    return x_curr

# Ejecutar métodos
raiz_estandar = secante_estandar(2.5, 3.5, 3)
raiz_modificada = secante_modificado(3.5, 0.01, 3)

# Generar Gráfica
x_vals = np.linspace(0, 5, 400)
plt.figure(figsize=(8, 5))
plt.axhline(0, color='black', lw=1, linestyle='--')
plt.plot(x_vals, f(x_vals), label='f(x) = 0.95x³ - 5.9x² + 10.9x - 6', color='blue')

# Marcar las raíces encontradas
plt.plot(raiz_estandar, f(raiz_estandar), 'ro', label=f'Raíz Estándar: {raiz_estandar:.4f}')
plt.plot(raiz_modificada, f(raiz_modificada), 'gs', label=f'Raíz Modificada: {raiz_modificada:.4f}')

plt.title("Localización de la raíz real más grande")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()