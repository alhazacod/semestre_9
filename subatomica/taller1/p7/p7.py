import numpy as np
import matplotlib.pyplot as plt

# Función para convertir de keV a amu
def kev_a_amu(energia_kev):
    """
    Convierte energía en keV a masa en unidades de masa atómica unificada (amu).

    Args:
      energia_kev: Energía en keV.

    Returns:
      Masa equivalente en amu.
    """
    c = 299792458  # Velocidad de la luz en m/s
    e = 1.602176634e-19  # Carga elemental en Coulomb
    amu = 1.66053906660e-27  # 1 unidad de masa atómica en kg

    # Conversión de keV a Joules
    energia_joules = energia_kev * e * 1000

    # Cálculo de la masa en kg
    masa_kg = energia_joules / c**2

    # Conversión de kg a amu
    masa_amu = masa_kg / amu

    return masa_amu

def parabola_simetria(z, A, f):
    # MeV
    alpha = 939.6 - 15.56 + (17.23 / ((A)**(1/3)) + (23.385))
    beta = 23.385 * 4 + 939.6 - 938.3
    gamma = (23.385 / A) * 4 + (0.697 / ((A)**(1/3)))
    n = A - z
    delta = f * (12 / ((A)**(1/2)))

    M = alpha * (A) - beta * z + gamma * z**2 + (delta / (A)**(1/2))
    # Pasamos M de MeV a amu
    M = mev_a_amu(M)
    curva = M - (A)
    return curva

def mev_a_amu(energia_mev):
    """
    Convierte energía en MeV a masa en unidades de masa atómica unificada (amu).

    Args:
      energia_mev: Energía en MeV.

    Returns:
      Masa equivalente en amu.
    """
    # Constante de conversión: 1 amu equivale aproximadamente a 931.5 MeV
    conversion_factor = 931.5

    # Cálculo de la masa en amu
    masa_amu = energia_mev / conversion_factor

    return masa_amu

# Puntos experimentales para el cobre 65
cu65 = kev_a_amu(-67263.7)
zn65 = kev_a_amu(-65912)
ni65 = kev_a_amu(-65125)
Ga65 = kev_a_amu(-62657.5)
co65 = kev_a_amu(-59185.2)
fe65 = kev_a_amu(-51218)
ge65 = kev_a_amu(-56478.2)
cr24 = kev_a_amu(-28310)
mn25 = kev_a_amu(-40967)
ar33 = kev_a_amu(-46940)
se34 = kev_a_amu(-33020)

# Lista de puntos experimentales
puntos = [(29, cu65), (30, zn65), (28, ni65), (31, Ga65), (27, co65), (26, fe65),
          (32, ge65), (24, cr24), (25, mn25), (33, ar33), (34, se34)]

# Ordenar los puntos por el valor de Z (eje X)
puntos_ordenados = sorted(puntos, key=lambda p: p[0])
z_puntos = np.array([p[0] for p in puntos_ordenados])
masa_puntos = np.array([p[1] for p in puntos_ordenados])

# Ajuste de los datos a una parábola de segundo grado
coeffs = np.polyfit(z_puntos, masa_puntos, 2)  # Ajuste a una parábola (grado 2)
parabola_fit = np.poly1d(coeffs)  # Función polinómica ajustada

# Graficar la parábola teórica (función continua)
z_cont = np.linspace(24, 34, 10000)
plt.plot(z_cont, parabola_simetria(z_cont, 65, 1), color='darkseagreen', label='parábola teórica')

# Graficar la parábola ajustada a los puntos experimentales
plt.plot(z_cont, parabola_fit(z_cont), color='navy', label='parábola experimental')

# Graficar los puntos experimentales
plt.scatter(z_puntos, masa_puntos, color='black', label='puntos experimentales')

# Determinar el isóbar más estable
indice_min = np.argmin(masa_puntos)
isobar_estable = puntos_ordenados[indice_min]
plt.scatter(isobar_estable[0], isobar_estable[1], color='red', label='isóbar más estable', zorder=5)

# Agregar flechas para las transiciones
for i in range(len(puntos_ordenados) - 1):
    if i < indice_min:
        z_inicio, masa_inicio = puntos_ordenados[i]
        z_fin, masa_fin = puntos_ordenados[i + 1]
    elif i >= indice_min:
        z_inicio, masa_inicio = puntos_ordenados[i + 1]
        z_fin, masa_fin = puntos_ordenados[i]

    # Determinar si la transición es beta- o captura electrónica
    if z_fin > z_inicio:
        transicion = 'β-'
    else:
        transicion = 'β+'

    # Dibujar la flecha
    plt.annotate('', xy=(z_fin, masa_fin), xytext=(z_inicio, masa_inicio),
                 arrowprops=dict(facecolor='gray', arrowstyle='->'))

    # Etiquetar la transición
    x_centro = (z_inicio + z_fin) / 2
    y_centro = (masa_inicio + masa_fin) / 2
    plt.text(x_centro, y_centro, transicion, fontsize=8, ha='center', color='darkgreen')


# Título y etiquetas
plt.title('A=65')
plt.xlabel('Z')
plt.ylabel('Exceso de Masa (amu)')

# Agregar leyenda
plt.legend()

# Mostrar la gráfica
plt.show()

