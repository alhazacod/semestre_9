import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import linregress

T = np.array([0.418,0.517,0.787,1.252,1.452,1.968,2.603,3.02,3.498,3.579,4.023,4.606,5.301,6.013])
c_v = np.array([0.007,0.0087,0.0136,0.0229, 0.0229, 0.041, 0.0621, 0.0809, 0.1065, 0.1109, 0.1407, 0.1864, 0.2567, 0.3464])

# Calcular c_v / T y T^2
c_v_over_T = c_v / T
T_squared = T**2

# Realizar la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(T_squared, c_v_over_T)

# Resultados ajustados
a = slope
gamma = intercept

# Calcular errores asociados
error_a = std_err
n = len(T_squared)
residuals = c_v_over_T - (a * T_squared + gamma)
variance = np.sum(residuals**2) / (n - 2)
error_gamma = np.sqrt(variance * (1 / n + np.mean(T_squared)**2 / np.sum((T_squared - np.mean(T_squared))**2)))

print(f'a = {a:.5f}±{error_a:.8f}')
print(f'gamma = {gamma:.5f}±{error_gamma:.8f}')

# Graficar los datos y el ajuste
plt.figure(figsize=(8, 6))
plt.scatter(T_squared, c_v_over_T, color="blue", label="Datos experimentales")
plt.plot(T_squared, a * T_squared + gamma, color="red", label="Ajuste lineal")
plt.xlabel("$T^2$ (K$^2$)")
plt.ylabel("$c_v / T$ (cal mol$^{-1}$ K$^{-2}$)")
plt.title("Ajuste lineal de $c_v / T = \\gamma + a T^2$")
plt.legend()
plt.grid()
plt.show()

# Conversion de gamma a unidades SI (J/mol*K^2)
gamma_SI = gamma * 4.184 * 10**(-2)  # (1 cal = 4.184 J)

# Constante universal de los gases (en J/mol*K)
R = 8.314

# Cálculo de la energía de Fermi
E_F = (np.pi**2 * R) / (3 * gamma_SI)
print(E_F)
