import numpy as np

# --- DEFINICIÓN DEL SISTEMA ---
def u(x, y): return x**2 - x + y - 0.75
def v(x, y): return -x**2 + 5*x*y + y

# --- NÚCLEO DEL PROGRAMA ---
def ejecutar_sistema(x0, y0, tolerancia, max_iter):
    ## x0, y0     -> Valores iniciales (1.2, 1.2 según guía)
    ## tolerancia -> Error porcentual objetivo
    ## max_iter   -> Límite de seguridad
    
    # 1. MÉTODO DE PUNTO FIJO (Sistemas)
    # Despejes sugeridos para convergencia:
    # x = sqrt(-y + x + 0.75)
    # y = x^2 / (5x + 1)
    print(f"\n{'--- a. PUNTO FIJO (SISTEMAS) ---':^50}")
    print(f"{'Iter':<5} | {'x':<12} | {'y':<12} | {'ea %':<10}")
    print("-" * 50)
    
    xi, yi = x0, y0
    for k in range(1, max_iter + 1):
        x_ant, y_ant = xi, yi
        # Evitamos raíces de negativos por si acaso
        xi = np.sqrt(abs(-y_ant + x_ant + 0.75))
        yi = x_ant**2 / (5*x_ant + 1)
        
        ea = max(abs((xi - x_ant)/xi), abs((yi - y_ant)/yi)) * 100
        print(f"{k:<5} | {xi:<12.6f} | {yi:<12.6f} | {ea:<10.4f}%")
        if ea < tolerancia: break

    # 2. MÉTODO DE NEWTON-RAPHSON (Sistemas)
    print(f"\n{'--- b. NEWTON-RAPHSON (SISTEMAS) ---':^50}")
    print(f"{'Iter':<5} | {'x':<12} | {'y':<12} | {'ea %':<10}")
    print("-" * 50)
    
    xi, yi = x0, y0
    for k in range(1, max_iter + 1):
        x_ant, y_ant = xi, yi
        
        # Elementos del Jacobiano
        du_dx, du_dy = 2*xi - 1, 1
        dv_dx, dv_dy = -2*xi + 5*yi, 5*xi + 1
        
        # Determinante del Jacobiano
        detJ = (du_dx * dv_dy) - (du_dy * dv_dx)
        
        # Sistema Newton: J * delta = -F
        # x_new = x_old - (u*dv_dy - v*du_dy) / detJ
        # y_new = y_old - (v*du_dx - u*dv_dx) / detJ
        xi = x_ant - (u(x_ant, y_ant)*dv_dy - v(x_ant, y_ant)*du_dy) / detJ
        yi = y_ant - (v(x_ant, y_ant)*du_dx - u(x_ant, y_ant)*dv_dx) / detJ
        
        ea = max(abs((xi - x_ant)/xi), abs((yi - y_ant)/yi)) * 100
        print(f"{k:<5} | {xi:<12.6f} | {yi:<12.6f} | {ea:<10.4f}%")
        if ea < tolerancia: break

    # --- 7. ANÁLISIS DE RESULTADOS ---
    print("\n" + "="*50)
    print("PUNTO 7: COMPROBACIÓN DE RESULTADOS FINALES")
    print("="*50)
    print(f"Coordenada final (X, Y): ({xi:.6f}, {yi:.6f})")
    print(f"Residuo u(x,y): {u(xi, yi):.10f}")
    print(f"Residuo v(x,y): {v(xi, yi):.10f}")
    print("="*50)

# --- LLAMADA SEGÚN PUNTO 7 ---
# Parámetros: x=1.2, y=1.2, tolerancia=0.01, max_iter=20
ejecutar_sistema(1.2, 1.2, 0.01, 20)