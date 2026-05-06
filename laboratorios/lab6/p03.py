import numpy as np

def evaluar_y_resolver(nombre, A, b):
    print(f"\n{'='*40}\nSistema {nombre}:\n{'='*40}")
    
    # 1. Homogeneidad
    if np.allclose(b, 0):
        print("[+] Tipo: HOMOGÉNEO")
    else:
        print("[+] Tipo: NO HOMOGÉNEO")
        
    # 2. Consistencia y Solución
    n_ecuaciones, n_incognitas = A.shape
    rango_A = np.linalg.matrix_rank(A)
    matriz_ampliada = np.column_stack((A, b))
    rango_Ab = np.linalg.matrix_rank(matriz_ampliada)
    
    if rango_A != rango_Ab:
        print("[!] Estado: INCONSISTENTE (0 soluciones).")
        print("-> Problema: Las ecuaciones se contradicen. No se puede resolver.")
        return
        
    if rango_A < n_incognitas:
        print("[!] Estado: CONSISTENTE (Infinitas soluciones).")
        print("-> Problema: Faltan restricciones (grados de libertad > 0). No hay solución única.")
        return
        
    # 3. Resolución (Si llegamos aquí, hay solución única)
    print("[+] Estado: CONSISTENTE (Solución única). Resolviendo...")
    try:
        # np.linalg.solve requiere matrices cuadradas. Si es sobredeterminado consistente, usamos lstsq
        if n_ecuaciones == n_incognitas:
            x = np.linalg.solve(A, b)
        else:
            x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            
        print(f"-> Solución: x = {x[0]:.4f}, y = {x[1]:.4f}, z = {x[2]:.4f}")
    except np.linalg.LinAlgError as e:
        print(f"-> Error matemático al intentar resolver: {e}")

# Definición de los sistemas dados en la imagen
sistemas = {
    "A": (
        np.array([[2, 3, -1], [4, -1, 3], [1, 2, -3]]),
        np.array([0, 0, 0])
    ),
    "B": (
        np.array([[2, 3, -1], [4, -1, 3], [1, 2, -3]]),
        np.array([1, 2, -4])
    ),
    "C": (
        np.array([[2, 3, -1], [4, -1, 3]]),
        np.array([1, 2])
    ),
    "D": (
        np.array([[2, 3, -1], [4, -1, 3], [1, 2, -3], [3, 5, -3]]),
        np.array([-3, 7, 6, 3])
    )
}

# Ejecución
for nombre, (A, b) in sistemas.items():
    evaluar_y_resolver(nombre, A, b)