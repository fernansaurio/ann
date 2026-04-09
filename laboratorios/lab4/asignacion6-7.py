"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 4 - Asignacion 6-7

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import numpy as np

# a) Punto fijo para sistemas
# Despejes para iteración simple: 
# De ec 2: x = sqrt(y + 5xy)
# De ec 1: y = -x^2 + x + 0.75
def g1(x, y): return np.sqrt(y + 5*x*y) 
def g2(x, y): return -(x**2) + x + 0.75

print("--- a) Iteración de Punto Fijo (Sistema) ---")
x0, y0 = 1.2, 1.2
for i in range(1, 4):
    x1 = g1(x0, y0)
    y1 = g2(x0, y0)
    print(f"Iter {i}: x = {x1:.5f}, y = {y1:.5f}")
    x0, y0 = x1, y1

# b) Newton-Raphson para sistemas
def u(x, y): return x**2 - x + y - 0.75
def v(x, y): return x**2 - 5*x*y - y

# Derivadas parciales (Jacobiano)
def J(x, y):
    du_dx = 2*x - 1
    du_dy = 1
    dv_dx = 2*x - 5*y
    dv_dy = -5*x - 1
    return np.array([[du_dx, du_dy], [dv_dx, dv_dy]])

print("\n--- b) Newton-Raphson (Sistema) ---")
x0, y0 = 1.2, 1.2
for i in range(1, 4):
    # Vector de funciones
    F = np.array([u(x0, y0), v(x0, y0)])
    
    # Matriz Jacobiana
    Jac = J(x0, y0)
    
    # Resolver [Jac] * [deltas] = -F
    deltas = np.linalg.solve(Jac, -F)
    
    x1 = x0 + deltas[0]
    y1 = y0 + deltas[1]
    
    print(f"Iter {i}:")
    print(f"  Jacobiano:\n{Jac}")
    print(f"  F(x,y): {F}")
    print(f"  Nuevo x = {x1:.5f}, Nuevo y = {y1:.5f}\n")
    
    x0, y0 = x1, y1