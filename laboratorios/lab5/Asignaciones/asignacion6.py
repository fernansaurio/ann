import numpy as np
import cmath
import matplotlib.pyplot as plt

# Definición de las funciones
def fa(x): return x**3 + x**2 - 3*x - 5
def fb(x): return x**3 - 0.5*x**2 + 4*x - 3

def muller_method(f, x0, x1, x2, tol=1e-5, max_iter=20):
    print(f"{'Iter':<5} | {'x3 (Aprox)':<15} | {'f(x3)':<15}")
    print("-" * 40)
    
    for i in range(1, max_iter + 1):
        # Convertimos a complex por si el discriminante es negativo
        x0_c, x1_c, x2_c = complex(x0), complex(x1), complex(x2)
        
        h0 = x1_c - x0_c
        h1 = x2_c - x1_c
        d0 = (f(x1_c) - f(x0_c)) / h0
        d1 = (f(x2_c) - f(x1_c)) / h1
        
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = f(x2_c)
        
        # Discriminante
        radical = cmath.sqrt(b**2 - 4*a*c)
        
        # Elegir el mayor denominador
        if abs(b + radical) > abs(b - radical):
            den = b + radical
        else:
            den = b - radical
            
        dx = -2 * c / den
        x3 = x2_c + dx
        
        # Como buscamos raíz real, tomamos la parte real para mostrar
        x3_real = x3.real
        error = abs(dx)
        
        print(f"{i:<5} | {x3_real:<15.6f} | {f(x3_real).real:<15.6e}")
        
        if error < tol:
            return x3_real
        
        x0, x1, x2 = x1_c, x2_c, x3

    return x2.real

# --- Resolución ---
print("Inciso A: f(x) = x³ + x² - 3x - 5")
raiz_a = muller_method(fa, 0, 1, 2)
print(f"Raíz final A: {raiz_a:.6f}\n")

print("Inciso B: f(x) = x³ - 0.5x² + 4x - 3")
raiz_b = muller_method(fb, 0, 0.5, 1)
print(f"Raíz final B: {raiz_b:.6f}\n")

# --- Gráficas ---
x_vals_a = np.linspace(-1, 3, 400)
x_vals_b = np.linspace(-1, 2, 400)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica A
ax1.plot(x_vals_a, fa(x_vals_a), 'b-', label='f(x) = x³ + x² - 3x - 5')
ax1.axhline(0, color='black', lw=1, linestyle='--')
ax1.plot(raiz_a, fa(raiz_a), 'ro', markersize=8, label=f'Raíz: {raiz_a:.4f}')
ax1.set_title("Inciso A")
ax1.grid(True)
ax1.legend()

# Gráfica B
ax2.plot(x_vals_b, fb(x_vals_b), 'g-', label='f(x) = x³ - 0.5x² + 4x - 3')
ax2.axhline(0, color='black', lw=1, linestyle='--')
ax2.plot(raiz_b, fb(raiz_b), 'ro', markersize=8, label=f'Raíz: {raiz_b:.4f}')
ax2.set_title("Inciso B")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()