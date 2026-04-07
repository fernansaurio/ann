import numpy as np
import matplotlib.pyplot as plt

def f(x): return 2*np.sin(np.sqrt(x)) - x

x = np.linspace(0.1, 5, 400)
plt.plot(x, f(x), label='f(x)')
plt.axhline(0, color='red', linestyle='--')
plt.title("Localización de Raíces")
plt.grid(True)
plt.show()