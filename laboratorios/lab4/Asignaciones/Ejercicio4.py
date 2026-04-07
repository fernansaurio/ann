import numpy as np

# --- DEFINICIÓN DE FUNCIONES MATEMÁTICAS ---

def f(x):
    # Función original: f(x) = -x^2 + 1.8x + 2.5
    return -x**2 + 1.8*x + 2.5

def df(x):
    # Derivada para Newton-Raphson: f'(x) = -2x + 1.8
    return -2*x + 1.8

def g(x):
    # Despeje para Punto Fijo: x = sqrt(1.8x + 2.5)
    return np.sqrt(1.8 * x + 2.5)

# --- NÚCLEO DEL PROGRAMA ---

def ejecutar_laboratorio(x0, tolerancia, max_iter):
    """
    x0         -> Punto de partida para la búsqueda (Semilla).
    tolerancia -> Error relativo porcentual máximo permitido (ea < tolerancia).
    max_iter   -> Freno de seguridad: número máximo de vueltas permitidas.
    """
    
    # 1. MÉTODO DE PUNTO FIJO
    print(f"\n{'--- PUNTO FIJO ---':^40}")
    print(f"{'Iter':<5} | {'xi':<15} | {'ea %':<15}")
    print("-" * 40)
    
    xi_pf = x0
    ea_pf = 100.0
    k_pf = 0
    
    # El bucle se detiene por precisión (tolerancia) O por seguridad (max_iter)
    while ea_pf > tolerancia and k_pf < max_iter:
        xi_ant = xi_pf
        xi_pf = g(xi_ant)
        k_pf += 1
        
        if xi_pf != 0:
            ea_pf = abs((xi_pf - xi_ant) / xi_pf) * 100
        
        print(f"{k_pf:<5} | {xi_pf:<15.8f} | {ea_pf:<15.8f}%")

    # 2. MÉTODO DE NEWTON-RAPHSON
    print(f"\n{'--- NEWTON-RAPHSON ---':^40}")
    print(f"{'Iter':<5} | {'xi':<15} | {'ea %':<15}")
    print("-" * 40)
    
    xi_nr = x0
    ea_nr = 100.0
    k_nr = 0
    
    while ea_nr > tolerancia and k_nr < max_iter:
        xi_ant = xi_nr
        xi_nr = xi_ant - f(xi_ant) / df(xi_ant)
        k_nr += 1
        
        if xi_nr != 0:
            ea_nr = abs((xi_nr - xi_ant) / xi_nr) * 100
            
        print(f"{k_nr:<5} | {xi_nr:<15.8f} | {ea_nr:<15.8f}%")

 
    # COMPROBACIÓN FINAL
    # --- RESUMEN DE RESULTADOS FINALES ---
    print("\n" + "="*45)
    print("RESUMEN DE RESULTADOS")
    print("="*45)
    # Resultados Punto Fijo
    print(f"PUNTO FIJO:     Raíz = {xi_pf:.8f} | Iter: {k_pf}")
    print(f"                f(root) = {f(xi_pf):.12f}")             #f(root) para verificar que es cercano a 0, |Comprobacion del error|
    print("-" * 45)
    # Resultados Newton-Raphson
    print(f"NEWTON-RAPHSON: Raíz = {xi_nr:.8f} | Iter: {k_nr}")
    print(f"                f(root) = {f(xi_nr):.12f}")
    print("="*45)

# ==========================================================
# LLAMADA AL PROGRAMA (Se puede modificar los parámetros)
# ==========================================================

# Parámetro 1: x0 (Valor inicial)
# Parámetro 2: tolerancia (Error objetivo %)
# Parámetro 3: max_iter (Límite de seguridad)

ejecutar_laboratorio(5.0, 0.05, 50)