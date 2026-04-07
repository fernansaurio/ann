## Método de Punto Fijo para encontrar raíces de una función
# Cambia la función g(x) y los parámetros de control para experimentar con diferentes casos.

import numpy as np

# f(x) original para la comprobación
def f(x):
    return -x**2 + 1.8*x + 2.5

# 1. AQUÍ CAMBIAS LA FUNCIÓN DESPEJADA x = g(x) [cite: 661]
def g(x):
    # Ejemplo del ejercicio 4: f(x) = -x^2 + 1.8x + 2.5
    # Despejando una x: x = sqrt(1.8x + 2.5)
    return np.sqrt(1.8 * x + 2.5)

def punto_fijo(x0, error_objetivo):
    xi = x0
    error_calculado = 100.0
    k = 0
    
    # Encabezado de la tabla (usando anchos fijos para alinear)
    print(f"\n{'Iter':<5} | {'Valor x':<12} | {'Error %':<12}")
    print("-" * 35)

    # 2. AQUÍ CAMBIAS EL LÍMITE MÁXIMO DE ITERACIONES 
    # Si quieres que se detenga a las 3 vueltas forzosamente, pon (k < 3)
    while (k < 50): 
        xi_anterior = xi
        xi = g(xi_anterior)
        k += 1
        
        # Cálculo del error relativo porcentual 
        if xi != 0:
            error_calculado = abs((xi - xi_anterior) / xi) * 100
        
        print(f"{k:<5} | {xi:<12.6f} | {error_calculado:<12.6f}%")
        
        # 3. Comparación con error dado 
        if error_calculado <= error_objetivo:
            print(">>> Objetivo de error alcanzado.")
            break

# --- RESPUESTA FINAL ---
    print("-" * 35)
    print(f"RESULTADO FINAL:")
    print(f"Raíz aproximada: {xi:.6f}")
    print(f"Iteraciones realizadas: {k}")
    # Comprobación: evaluar la raíz en la f(x) original 
    print(f"Comprobación f(root): {f(xi):.6f} (debe ser cercano a 0)")

# ==========================================================
# LLAMADA PRINCIPAL (Aquí es donde tú controlas los datos)
# ==========================================================

# Parámetro 1: x0 (Valor inicial o punto de partida) 
# Parámetro 2: Error al cual debe llegar (ejemplo 0.05%) 

punto_fijo(5.0, 0.05)