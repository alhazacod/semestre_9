import numpy as np
import matplotlib.pyplot as plt

# Constante de Bohr (en Ångströms para mayor claridad en los gráficos)
a0 = 0.529177

# Definimos las funciones de onda radiales

def u_1s(r):
    return 2 / np.sqrt(a0**3) * np.exp(-r / (2 * a0))

def u_2s(r):
    return (1 / np.sqrt(2)) * (1 / np.sqrt(a0**3)) * (1 - r / (2 * a0)) * np.exp(-r / (2 * a0))

def u_2p(r):
    return (1 / (2 * np.sqrt(6))) * (1 / np.sqrt(a0**3)) * (r / a0) * np.exp(-r / (2 * a0))

# Rango de valores para r (en Ångströms)
r = np.linspace(0, 10, 1000)

# Calculamos las funciones de onda radiales
u1s = u_1s(r)
u2s = u_2s(r)
u2p = u_2p(r)

# Configuración de la gráfica
plt.figure(figsize=(8, 6))
plt.plot(r, u1s, label="$u_{1s}(r)$", color="blue")
plt.plot(r, u2s, label="$u_{2s}(r)$", color="green")
plt.plot(r, u2p, label="$u_{2p}(r)$", color="red")

plt.title("Funciones de onda radiales del átomo de hidrógeno", fontsize=16)
plt.xlabel("r (Å)", fontsize=14)
plt.ylabel("u(r)", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.show()

