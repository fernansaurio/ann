"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 3 - Asignacion 5

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import math

a, b, c = -0.5, 2.5, 4.5

print("--- Desarrollo analítico manual ---")
print(f"Ecuación: ({a})x^2 + ({b})x + ({c}) = 0")
print("Fórmula cuadrática: x = (-b ± sqrt(b^2 - 4ac)) / 2a")

# Paso 1: Discriminante
disc = (b**2) - (4 * a * c)
print(f"\nPaso 1. Discriminante = ({b})^2 - 4({a})({c})")
print(f"Discriminante = {b**2} - ({4 * a * c}) = {disc}")

# Paso 2: Raíz cuadrada del discriminante
raiz_disc = math.sqrt(disc)
print(f"\nPaso 2. Raíz del discriminante = sqrt({disc}) = {raiz_disc:.4f}")

# Paso 3: Calcular x1 y x2
print("\nPaso 3. Obtener x1 y x2:")
x1 = (-b + raiz_disc) / (2 * a)
x2 = (-b - raiz_disc) / (2 * a)

print(f"x1 = ({-b} + {raiz_disc:.4f}) / {2*a} = {x1:.4f}")
print(f"x2 = ({-b} - {raiz_disc:.4f}) / {2*a} = {x2:.4f}")