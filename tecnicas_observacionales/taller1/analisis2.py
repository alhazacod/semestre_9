import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from functions import *


# Cargar el archivo CSV
df = pd.read_csv('data2.csv')

# Calcular F_obj para cada lámpara según la ecuación (3)
df['F_obj'] = df['F_mean']*df["Area_px"] - df['F_bg_mean']*df["Area_px"]

# Usar una distancia de referencia para la primera lámpara
d1 = 20  

# Calcular d(i) 
df['d_prelim'] = d1 * np.sqrt(df['F_obj'].iloc[0] / df['F_obj'])

# Corrección de luminosidad relativa 
x1,y1,x2,y2 = distance_real(df['Lamp'].iloc[0], df['d_real'].iloc[0], df['Lamp'].iloc[1], df['d_real'].iloc[1], df['Lamp'])
df['d_real'] = y1-3
df['r'] = df['F_mean']*df["Area_px"]*y1**2 / (df['F_mean'].iloc[0]*df["Area_px"].iloc[0]*y1[0]**2)

# Calcular las distancias ajustadas 
df['d_adjusted'] = d1 * np.sqrt(df['r'] * df['F_obj'].iloc[0] / df['F_obj'])

# Calcular el error de los datos con respecto al valor real
df['d_prelim_error'] = np.abs(df['d_prelim'] - df['d_real'])/df['d_real'] * 100
df['d_adjusted_error'] = np.abs(df['d_adjusted'] - df['d_real'])/df['d_real'] * 100




# Mostrar los resultados
print('Analisis: ---------------------------')
print(df[['Lamp', 'F_mean', 'F_bg_mean', 'Area_px', 'd_real', 'F_obj', 'd_prelim', 'd_prelim_error']])


fig, axes = plt.subplots(1, figsize=(16, 6))

#plot_real_distances(axes[1], x1, y1, y2)
plot_real_distances(axes, x1, y1, y2)

# Primer punto (forzar paso)
x1, y1 = df['Lamp'].iloc[0], df['d_prelim'].iloc[0]

plot_with_forced_fit(axes, df['Lamp'], df['d_prelim'], x1, y1,
                     'Distancia Preliminar (Antes de Corrección)', 
                     'Número de Lámpara', 
                     'Distancia Preliminar')

x1, y1 = df['Lamp'].iloc[0], df['d_adjusted'].iloc[0]
#plot_with_forced_fit(axes[1], df['Lamp'], df['d_adjusted'], x1, y1,
#                     'Distancia Ajustada (Después de Corrección)', 
#                     'Número de Lámpara', 
#                     'Distancia Ajustada')
axes.set_ylabel('d [cm]')

plt.tight_layout()
plt.show()
