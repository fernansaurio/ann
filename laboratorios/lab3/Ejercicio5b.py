import numpy as np

## --- FUNCIONES DEL EJERCICIO 5 ---
def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5

def df(x):
    return 6*x**2 - 23.4*x + 17.7

def g(x):
    ## Despeje para punto fijo sugerido para x cerca de 3
    return (11.7*x**2 - 17.7*x + 5) / (2*x**2)

def calcular_punto_5(x0, tolerancia, max_iter):
    ## x0         -> Valor inicial (3.0)
    ## tolerancia -> Precisión (0.001)
    ## max_iter   -> Límite de vueltas (3)

    # Lógica de Punto Fijo
    print(f"\n{'--- b. PUNTO FIJO ---':^40}")
    xi_pf = x0
    ea = 100.0
    for k in range(1, max_iter + 1):
        xi_ant = xi_pf
        xi_pf = g(xi_ant)
        ea = abs((xi_pf - xi_ant) / xi_pf) * 100
        print(f"Iter {k}: x = {xi_pf:.6f} | ea = {ea:.4f}%")

    # Lógica de Newton-Raphson
    print(f"\n{'--- c. NEWTON-RAPHSON ---':^40}")
    xi_nr = x0
    ea = 100.0
    for k in range(1, max_iter + 1):
        xi_ant = xi_nr
        xi_nr = xi_ant - f(xi_ant) / df(xi_ant)
        ea = abs((xi_nr - xi_ant) / xi_nr) * 100
        print(f"Iter {k}: x = {xi_nr:.6f} | ea = {ea:.4f}%")

# 3. COMPARACIÓN FINAL (d)
    print("\n" + "="*50)
    print(f"{'5d. COMPARACIÓN DE RESULTADOS FINALES':^50}")
    print("="*50)
    
    # Aquí imprimimos el valor de 'x' que cada método logró tras 3 vueltas
    print(f"RAÍZ OBTENIDA POR PUNTO FIJO:     {xi_pf:.8f}")
    print(f"RAÍZ OBTENIDA POR NEWTON-RAPHSON: {xi_nr:.8f}")
    print("-" * 50)
    
    # ¿Qué comparamos? Comparamos el "Residuo" o Comprobación f(x)
    # Entre más cerca de CERO esté este valor, mejor es el método.
    print(f"Comprobación f(x) Punto Fijo:     {f(xi_pf):.10f}")
    print(f"Comprobación f(x) Newton-Raphson: {f(xi_nr):.10f}")
    print("="*50)
    
    # Conclusión automática basada en la comparación
    if abs(f(xi_nr)) < abs(f(xi_pf)):
        print("CONCLUSIÓN: Newton-Raphson es más preciso en 3 iteraciones.")
    else:
        print("CONCLUSIÓN: Punto Fijo es más preciso en 3 iteraciones.")

## LLAMADA CON LOS PARÁMETROS DE LA GUÍA
calcular_punto_5(3.0, 0.001, 3)