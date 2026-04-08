import math

def calcular_raices():
    a = -0.5
    b = 2.5
    c = 4.5
    
    # Cálculo del discriminante
    discriminante = (b**2) - (4 * a * c)
    
    # Cálculo de las raíces
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    print(f"Raíz 1 (x1): {x1:.4f}")
    print(f"Raíz 2 (x2): {x2:.4f}")

calcular_raices()