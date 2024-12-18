
import numpy as np
import matplotlib.pyplot as plt

# Definir el potencial efectivo
# V_eff(r) = - R_H * a_0 / r + l * (l + 1) * R_H * a_0 / r^2
def potencial_efectivo(r, l):
    R_H = 1  # Unidad de energía de Rydberg
    a_0 = 1  # Unidad de radio de Bohr
    return -R_H * a_0 / r + (l * (l + 1) * R_H * a_0) / r**2

# Definir los valores de r
r = np.linspace(0.1, 10, 500)  # Evitar división por cero en r = 0

# Valores de l
l_values = [0, 2, 4]

# Colores para las curvas
colors = ['b', 'g', 'r']

# Crear la figura
plt.figure(figsize=(8, 6))

# Graficar el potencial efectivo para cada valor de l
for l, color in zip(l_values, colors):
    V_eff = potencial_efectivo(r, l)
    plt.plot(r, V_eff, label=f'l = {l}', color=color)

# Configuración del gráfico
plt.title('Potencial Efectivo del Átomo de Hidrógeno', fontsize=14)
plt.xlabel('r ($a_0$)', fontsize=12)
plt.ylabel('$V_{eff}(r)$ ($R_H$)', fontsize=12)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # Línea horizontal en y = 0
plt.grid(alpha=0.6)
plt.legend(fontsize=12)
plt.ylim(-10, 10)
plt.xlim(0, 10)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

