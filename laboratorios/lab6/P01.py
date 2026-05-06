import numpy as np

def analizar_consistencia(A, b):
    """
    Determina si un sistema Ax = b es consistente o inconsistente, 
    y el tipo de solución que posee.
    """
    n_ecuaciones = A.shape[0]
    n_incognitas = A.shape[1]
    
    print(f"Ecuaciones: {n_ecuaciones}, Incógnitas: {n_incognitas}")
    if n_ecuaciones != n_incognitas:
        print("-> Advertencia: El sistema no es cuadrado (ecuaciones != incógnitas).")
    
    # Cálculo de rangos para aplicar el Teorema de Rouché-Capelli
    rango_A = np.linalg.matrix_rank(A)
    matriz_ampliada = np.column_stack((A, b))
    rango_Ab = np.linalg.matrix_rank(matriz_ampliada)
    
    if rango_A != rango_Ab:
        return "Resultado: Sistema INCONSISTENTE (No tiene solución)."
    elif rango_A == n_incognitas:
        return "Resultado: Sistema CONSISTENTE con SOLUCIÓN ÚNICA."
    else:
        return "Resultado: Sistema CONSISTENTE con SOLUCIONES INFINITAS."

# Ejemplo de prueba (Sistema 'a' del documento)
A_prueba = np.array([[2, 3, -1], [4, -1, 3], [1, 2, -3]])
b_prueba = np.array([0, 0, 0])

print("--- Análisis de Consistencia ---")
print(analizar_consistencia(A_prueba, b_prueba))