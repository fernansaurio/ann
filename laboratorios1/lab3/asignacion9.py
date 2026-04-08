import math

def f(m):
    g = 9.8
    c = 15.0
    v = 35.0
    t = 9.0
    return (g * m / c) * (1 - math.exp(-(c * t) / m)) - v

a = 50.0
b = 70.0
c_anterior = 0.0

print("Falsa Posición - Paracaidista")
print("Iter | Masa (m)  | Error (%)")

for i in range(1, 100):
    c_actual = (a * f(b) - b * f(a)) / (f(b) - f(a))
    
    if i == 1:
        error = 100.0
    else:
        error = abs((c_actual - c_anterior) / c_actual) * 100.0
        
    print(f" {i:2d}  | {c_actual:.5f} | {error:.4f}%")
    
    if error < 0.1 and i > 1:
        print(f"\nResultado final: La masa es {c_actual:.2f} kg")
        break
        
    if f(a) * f(c_actual) < 0:
        b = c_actual
    else:
        a = c_actual
        
    c_anterior = c_actual