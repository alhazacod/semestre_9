import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def distance_real(x1,y1,x2,y2,x):
    # Configuración de la primera recta
    x1, y1 = x1, y1 + 3
    x2, y2 = x2, y2 + 3
    m1 = (y2 - y1) / (x2 - x1)
    b1 = y1 - m1 * x1

    # Configuración de la segunda recta
    x1, y1 = x1, y1 - 6
    x2, y2 = x2, y2 - 6
    m2 = (y2 - y1) / (x2 - x1)
    b2 = y1 - m2 * x1

    y1 = m1 * x + b1
    y2 = m2 * x + b2

    return x,y1,x,y2

def plot_with_forced_fit(ax, x, y, x1, y1, title, xlabel, ylabel):
    # Calcular la pendiente mientras se fuerza que pase por el primer punto
    model = LinearRegression(fit_intercept=False)  # Sin intercepto inicialmente
    x_reshaped = (x - x1).values.reshape(-1, 1)  # Ajustar al nuevo origen
    model.fit(x_reshaped, y - y1)
    
    slope = model.coef_[0]
    intercept = y1 - slope * x1  # Forzar intersección en el primer punto
    y_pred = slope * x + intercept
    equation = f"y = {slope:.2f}x + {intercept:.2f}"

    # Graficar
    ax.scatter(x, y, color='blue', label='Datos')
    ax.plot(x, y_pred, color='red', label=f'Ajuste Forzado ({equation})')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    ax.grid(True)

def plot_real_distances(ax, x, y1, y2):
    # Graficamos las líneas y el área entre ellas
    ax.fill_between(x, y1, y2, color='orange', alpha=0.3, label='Distancia Real ± 3m')
    ax.grid(True)
