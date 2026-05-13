import numpy as np

MAX_ITER = 100
ES = 0.0005   # criterio de parada en %


def gauss_seidel(A, b, n, max_iter=MAX_ITER, es=ES):
    """
    Metodo de Gauss-Seidel con deteccion de convergencia/divergencia.

    Parametros:
        A        : np.ndarray (n x n)  — coeficientes
        b        : np.ndarray (n,)     — terminos independientes
        n        : numero de variables
        max_iter : maximo de iteraciones
        es       : criterio de parada en % (epsilon_s)

    Retorna:
        x        : np.ndarray con la solucion aproximada
        convergio: bool
    """
    x      = np.zeros(n)
    x_prev = np.zeros(n)

    # Encabezado de tabla
    header = f"{'Iter':<5}" + "".join(f"{'x' + str(i + 1):<12}" for i in range(n)) + f"{'ea_max(%)':<14}"
    print(header)

    for it in range(1, max_iter + 1):
        x_prev[:] = x.copy()

        # Calcular nuevos valores
        for i in range(n):
            s    = b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = s / A[i][i]

        # Calcular error relativo aproximado maximo
        # ea = |(x_nuevo - x_anterior) / x_nuevo| * 100
        ea_vec = []
        for i in range(n):
            if x[i] != 0:
                ea_vec.append(abs((x[i] - x_prev[i]) / x[i]) * 100)
            else:
                ea_vec.append(abs(x[i] - x_prev[i]))
        ea_max = max(ea_vec)

        # Imprimir fila de la tabla
        row = f"{it:<5}" + "".join(f"{v:<12.5f}" for v in x) + f"{ea_max:<14.5f}"
        print(row)

        # Detectar divergencia por explosion numerica
        if any(abs(v) > 1e10 for v in x):
            print(f"\n*** DIVERGENCIA detectada en iteracion {it} ***")
            return x, False

        if ea_max < es:
            print(f"\nConvergencia en iteracion {it}  (ea={ea_max:.6f}% < es={es}%)")
            return x, True

    print(f"\nNo convergio en {max_iter} iteraciones -> DIVERGENCIA.")
    return x, False


if __name__ == "__main__":
    # -------------------------------------------------------
    # Sistema 1 (imagen):
    #   2x1 +  x2 -  x3 =  1
    #   5x1 + 2x2 + 2x3 = -4
    #   3x1 +  x2 +  x3 =  5
    # (NO es diagonalmente dominante -> diverge)
    # -------------------------------------------------------
    A1 = np.array([[ 2,  1, -1],
                   [ 5,  2,  2],
                   [ 3,  1,  1]], dtype=float)
    b1 = np.array([1.0, -4.0, 5.0])

    print("=== Sistema 1 imagen — Gauss-Seidel ===")
    x1, ok1 = gauss_seidel(A1, b1, 3)
    print("Resultado:", "CONVERGENCIA" if ok1 else "DIVERGENCIA")

    # -------------------------------------------------------
    # Sistema 2 (imagen):
    #    x1 +  x2 -  x3 = -3
    #   6x1 + 2x2 + 2x3 =  2
    #  -3x1 + 4x2 +  x3 =  1
    # (NO es diagonalmente dominante -> diverge)
    # -------------------------------------------------------
    A2 = np.array([[ 1,  1, -1],
                   [ 6,  2,  2],
                   [-3,  4,  1]], dtype=float)
    b2 = np.array([-3.0, 2.0, 1.0])

    print("\n=== Sistema 2 imagen — Gauss-Seidel ===")
    x2, ok2 = gauss_seidel(A2, b2, 3)
    print("Resultado:", "CONVERGENCIA" if ok2 else "DIVERGENCIA")

    # -------------------------------------------------------
    # Sistema original del enunciado (referencia):
    #   4x1 -   x2 + 0.2x3 = 8
    #    x1 +  5x2 + 0.3x3 = 7
    #  0.1x1 + 0.2x2 + 3x3 = 5
    # (Diagonalmente dominante -> converge)
    # -------------------------------------------------------
    A3 = np.array([[4,   -1,  0.2],
                   [1,    5,  0.3],
                   [0.1, 0.2, 3.0]])
    b3 = np.array([8.0, 7.0, 5.0])

    print("\n=== Sistema original — Gauss-Seidel ===")
    x3, ok3 = gauss_seidel(A3, b3, 3)
    print("Resultado:", "CONVERGENCIA" if ok3 else "DIVERGENCIA")
    if ok3:
        for i, v in enumerate(x3):
            print(f"x{i + 1} = {v:.5f}")
