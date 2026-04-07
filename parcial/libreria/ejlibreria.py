#El siguiente codigo permite calcular la raiz de una funcion por diferentes metodos
# El codigo permite ingresarlo directamente desde consola utilizando una sintaxis en especifico, igualando las variables a sus valores
# Si no se necesita esa funcion desde consola, se pueden usar los valores fijos dentro del codigo
import sys
import time
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, diff
from sympy.parsing.latex import parse_latex

def main():
    # =========================================================================
    # 📦 CAJÓN DE CONFIGURACIÓN RÁPIDA 📦
    # =========================================================================
    LEER_DESDE_CONSOLA = True

    # Valores fijos (Solo se utilizan si LEER_DESDE_CONSOLA = False)
    fijo_ec = "x^2 - 4"
    fijo_metodo = "biseccion"
    fijo_p1 = 0.0
    fijo_p2 = 5.0
    fijo_tol = 1e-6      # Tolerancia por defecto
    fijo_max_iter = 100  # Máximo de iteraciones por defecto
    fijo_grafica = True
    fijo_time = True
    # =========================================================================

    # 1. Asignación de variables (Consola vs Fijos)
    if LEER_DESDE_CONSOLA:
        args_dict = {}
        for arg in sys.argv[1:]:
            if '=' in arg:
                clave, valor = arg.split('=', 1)
                args_dict[clave.lower()] = valor
                
        if 'ec' not in args_dict or 'metodo' not in args_dict:
            print('Uso: python3 ejlibreria.py ec="x^2 - 4" metodo=biseccion p1=0 p2=5 tol=1e-6 iter=100 grafica=true time=true')
            sys.exit(1)

        latex_eq = args_dict['ec']
        metodo = args_dict['metodo'].lower()
        
        try:
            # Si no pasas los valores, usa los predeterminados de forma segura
            p1 = float(args_dict.get('p1', 0.0))
            p2 = float(args_dict.get('p2', 0.0))
            tol = float(args_dict.get('tol', 1e-6))
            max_iter = int(args_dict.get('iter', 100))
        except ValueError:
            print("Error: p1, p2, tol y iter deben ser valores numéricos.")
            sys.exit(1)

        mostrar_grafica = args_dict.get('grafica', 'false').lower() == 'true'
        contar_tiempo = args_dict.get('time', 'false').lower() == 'true'
        
    else:
        # Usamos las variables encajonadas
        print("Aviso: Ejecutando con valores fijos en el código.")
        latex_eq = fijo_ec
        metodo = fijo_metodo
        p1 = fijo_p1
        p2 = fijo_p2
        tol = fijo_tol
        max_iter = fijo_max_iter
        mostrar_grafica = fijo_grafica
        contar_tiempo = fijo_time

    # 2. Parsear la ecuación de LaTeX
    x = symbols('x')
    try:
        expr = parse_latex(latex_eq)
    except Exception as e:
        print(f"Error al procesar LaTeX. Asegúrate de escribir bien la ecuación: {e}")
        sys.exit(1)
    
    f_py = lambdify(x, expr, 'math')
    expr_diff = diff(expr, x)
    df_py = lambdify(x, expr_diff, 'math')
    g_expr = x - expr
    g_py = lambdify(x, g_expr, 'math')

    # 3. Configurar C++ (ctypes)
    try:
        lib = ctypes.CDLL('./libraices.so')
    except OSError:
        print("Error: No se encontro 'libraices.so'. Compila el archivo C++ primero.")
        sys.exit(1)

    CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
    c_f = CMPFUNC(f_py)
    c_df = CMPFUNC(df_py)
    c_g = CMPFUNC(g_py)

    for func in [lib.biseccion, lib.falsa_posicion, lib.newton_raphson, lib.secante, lib.punto_fijo]:
        func.restype = ctypes.c_double

    # 4. Ejecución y medición
    raiz = None
    start_time = time.perf_counter()

    #Caja vacia de contador de ejecuciones
    iteraciones = ctypes.c_int(0)

    if metodo == 'biseccion':
        raiz = lib.biseccion(c_f, ctypes.c_double(p1), ctypes.c_double(p2), ctypes.c_double(tol), ctypes.c_int(max_iter), ctypes.byref(iteraciones))
    elif metodo == 'falsa_posicion':
        raiz = lib.falsa_posicion(c_f, ctypes.c_double(p1), ctypes.c_double(p2), ctypes.c_double(tol), ctypes.c_int(max_iter), ctypes.byref(iteraciones))
    elif metodo == 'newton_raphson':
        raiz = lib.newton_raphson(c_f, c_df, ctypes.c_double(p1), ctypes.c_double(tol), ctypes.c_int(max_iter), ctypes.byref(iteraciones))
    elif metodo == 'secante':
        raiz = lib.secante(c_f, ctypes.c_double(p1), ctypes.c_double(p2), ctypes.c_double(tol), ctypes.c_int(max_iter), ctypes.byref(iteraciones))
    elif metodo == 'punto_fijo':
        raiz = lib.punto_fijo(c_g, ctypes.c_double(p1), ctypes.c_double(tol), ctypes.c_int(max_iter), ctypes.byref(iteraciones))
    else:
        print(f"Método desconocido: {metodo}")
        sys.exit(1)
        
    end_time = time.perf_counter()

    iteraciones = iteraciones.value if hasattr(iteraciones, 'value') else 'N/A'

    # 5. Imprimir resultados
    print(f"\n--- RESULTADOS ---")
    print(f"Ecuación: f(x) = {expr}")
    print(f"Método  : {metodo}")
    print(f"Iteraciones: {iteraciones}")
    
    if np.isnan(raiz):
        print(f"Estado  : FALLO tras {max_iter} iteraciones o intervalo inválido.")
    else:
        print(f"Raíz    : x = {raiz:.6f}")
        print(f"Error f(x): {f_py(raiz):.2e}")
        print(f"Tolerancia usada: {tol}")
    
    if contar_tiempo:
        print(f"Tiempo C++: {(end_time - start_time) * 1000:.6f} ms")
    print("------------------\n")

    # 6. Graficar dinámicamente
    if mostrar_grafica and not np.isnan(raiz):
        r_val = float(raiz)
        rango = max(5.0, abs(p2 - p1) if metodo in ['biseccion', 'falsa_posicion'] else 5.0)
        
        x_vals = np.linspace(r_val - rango, r_val + rango, 400)
        y_vals = [f_py(val) for val in x_vals]
        
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f'$f(x) = {expr}$')
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1, alpha=0.3)
        plt.plot(r_val, 0, 'ro', markersize=8, label=f'Raíz: {r_val:.4f}')
        
        if metodo in ['biseccion', 'falsa_posicion']:
            plt.axvspan(p1, p2, color='green', alpha=0.1, label=f'Intervalo [{p1}, {p2}]')

        plt.title(f'Gráfica - Método: {metodo}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

if __name__ == "__main__":
    main()