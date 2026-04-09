"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 3 - Asignacion 4

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

def f(x):
    return -0.5 * x**2 + 2.5 * x + 4.5

a = 5.0
b = 10.0
c_anterior = 0.0

print("Iter | c_aprox | Error (%)")
print("-" * 28)

for i in range(1, 4):
    c_actual = (a + b) / 2.0
    
    if i == 1:
        error = 0.0
    else:
        error = abs((c_actual - c_anterior) / c_actual) * 100.0
        
    print(f"  {i}  | {c_actual:.4f}  | {error:.2f}%")
    
    # Evaluar en qué subintervalo está la raíz
    if f(a) * f(c_actual) < 0:
        b = c_actual
    else:
        a = c_actual
        
    c_anterior = c_actual