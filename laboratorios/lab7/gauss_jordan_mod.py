MAX_N = 10


def gauss_jordan(matrix, n):
    """
    Metodo de Gauss-Jordan generalizado.

    Parametros:
        matrix : lista de n listas, cada una con n+1 elementos [coef | b].
                 Se modifica in-place.
        n      : numero de variables (1 hasta MAX_N).
    """
    for i in range(n):
        # Pivoteo parcial con valor absoluto
        max_row = max(range(i, n), key=lambda k: abs(matrix[k][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Verificar singularidad
        if abs(matrix[i][i]) < 1e-12:
            print("Sistema singular o sin solucion unica.")
            return

        # Hacer elemento diagonal igual a 1
        divisor = matrix[i][i]
        for k in range(i, n + 1):
            matrix[i][k] /= divisor

        # Hacer ceros en TODA la columna (arriba y abajo)
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]


def display(matrix, n):
    """Muestra la matriz aumentada con formato."""
    for i in range(n):
        print("  ".join(f"{matrix[i][j]:9.4f}" for j in range(n + 1)))


if __name__ == "__main__":
    # -------------------------------------------------------
    # Sistema 1 (imagen):
    #   2x1 +  x2 -  x3 =  1
    #   5x1 + 2x2 + 2x3 = -4
    #   3x1 +  x2 +  x3 =  5
    # -------------------------------------------------------
    n1 = 3
    m1 = [
        [2,  1, -1,  1],
        [5,  2,  2, -4],
        [3,  1,  1,  5],
    ]

    print("=== Sistema 1 ===")
    print("Matriz original:")
    display(m1, n1)
    gauss_jordan(m1, n1)
    print("Solucion:")
    for i in range(n1):
        print(f"x{i + 1} = {m1[i][n1]:.4f}")

    # -------------------------------------------------------
    # Sistema 2 (imagen):
    #    x1 +  x2 -  x3 = -3
    #   6x1 + 2x2 + 2x3 =  2
    #  -3x1 + 4x2 +  x3 =  1
    # -------------------------------------------------------
    n2 = 3
    m2 = [
        [ 1,  1, -1, -3],
        [ 6,  2,  2,  2],
        [-3,  4,  1,  1],
    ]

    print("\n=== Sistema 2 ===")
    print("Matriz original:")
    display(m2, n2)
    gauss_jordan(m2, n2)
    print("Solucion:")
    for i in range(n2):
        print(f"x{i + 1} = {m2[i][n2]:.4f}")
