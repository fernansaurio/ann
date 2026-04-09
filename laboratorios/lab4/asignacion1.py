"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 4 - Asignacion 1

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import math

def g(x):
    return 2 * math.sin(math.sqrt(x))

x0 = 0.5
tolerancia = 0.001
error = 100.0
iteracion = 1

print("Iteración de Punto Fijo: x_(i+1) = 2*sin(sqrt(x_i))")
print(f"{'Iter':<5} | {'x_i':<10} | {'x_(i+1)':<10} | {'Error Ea (%)':<10}")
print("-" * 45)

while error > tolerancia:
    x1 = g(x0)
    error = abs((x1 - x0) / x1) * 100.0
    
    print(f"{iteracion:<5} | {x0:.6f}   | {x1:.6f}   | {error:.5f}%")
    
    x0 = x1
    iteracion += 1

print(f"\nRaíz aproximada final: {x0:.6f}")