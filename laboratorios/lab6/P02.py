import numpy as np

def analizar_homogeneidad(b):
    """
    Determina si el sistema es homogéneo evaluando el vector de términos independientes.
    """
    # Verifica si todos los elementos del vector b son cercanos a 0
    if np.allclose(b, 0):
        return "El sistema es HOMOGÉNEO."
    else:
        return "El sistema es NO HOMOGÉNEO."

# Ejemplos de prueba
b_homogeneo = np.array([0, 0, 0])
b_no_homogeneo = np.array([1, 2, -4])

print("--- Análisis de Homogeneidad ---")
print(f"Vector {b_homogeneo}: {analizar_homogeneidad(b_homogeneo)}")
print(f"Vector {b_no_homogeneo}: {analizar_homogeneidad(b_no_homogeneo)}")