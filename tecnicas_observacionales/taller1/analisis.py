import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Cargar el archivo CSV
# Asegúrate de reemplazar 'nombre_del_archivo.csv' con la ruta correcta a tu archivo
df = pd.read_csv('data.csv')

# Calcular F_obj para cada lámpara según la ecuación (3)
df['F_obj'] = (df['L_mean'] - df['L_bg_mean']) * df['Area_px']

# Usar una distancia de referencia para la primera lámpara
d1 = 23.06  # Distancia arbitraria

# Calcular d(i) preliminar usando la ecuación (4)
df['d_prelim'] = d1 * np.sqrt(df['F_obj'].iloc[0] / df['F_obj'])

# Corrección de luminosidad relativa según la ecuación (5)
df['r'] = df['L_mean'] / df['L_mean'].iloc[0]

# Calcular las distancias ajustadas usando la ecuación (6)
df['d_adjusted'] = d1 * np.sqrt(df['r'] * df['F_obj'].iloc[0] / df['F_obj'])

# Mostrar los resultados
print(df[['Lamp', 'F_obj', 'd_prelim', 'r', 'd_adjusted']])



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

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Primer punto (forzar paso)
x1, y1 = df['Lamp'].iloc[0], df['d_prelim'].iloc[0]

plot_with_forced_fit(axes[0], df['Lamp'], df['d_prelim'], x1, y1,
                     'Distancia Preliminar (Antes de Corrección)', 
                     'Número de Lámpara', 
                     'Distancia Preliminar')

x1, y1 = df['Lamp'].iloc[0], df['d_adjusted'].iloc[0]
plot_with_forced_fit(axes[1], df['Lamp'], df['d_adjusted'], x1, y1,
                     'Distancia Ajustada (Después de Corrección)', 
                     'Número de Lámpara', 
                     'Distancia Ajustada')

plt.tight_layout()
plt.show()
