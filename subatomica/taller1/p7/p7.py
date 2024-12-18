import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

def kev_a_amu(energia_kev):
  """
  Convierte energía en keV a masa en unidades de masa atómica unificada (amu).

  Args:
    energia_kev: Energía en keV.

  Returns:
    Masa equivalente en amu.
  """

  # Constantes físicas (aproximadas)
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

#para manganesio
mn65=-51742*0.001
#para hierro
fe65=-58920*0.001
#Para cobalto
co65=-62898*0.001
#para nickel
ni65=-65125*0.001
#coordenada cobre
cu65=-67264*0.001
#para el Zinc 65
zn65=-65912*0.001
#para galio
ga65=-47130*0.001 
#Para germanio
ge65=-33790*0.001

datay = np.array([mn65,fe65,co65,ni65,cu65,zn65,ga65,ge65])
datax = np.array([25,26,27,28,29,30,31,32])

plt.scatter(datax,datay)

def func(x, a, b, c):
    return a+b*x+c*x**2
popt, pcov = curve_fit(func, datax, datay)
x=np.linspace(25,32,20)
plt.plot(x, func(x, *popt))

#Calculado para el ejercicio
def mass(Z):
    A = 61
    c = 1 #299792458
    m_n = 938.27
    m_p = 939.57
    a_v = 15.56
    a_s = 17.23
    a_c = 0.697
    a_sym = 93.14 
    a_p = 12
    return A*(m_n*c**2 - a_v + a_s/A**(1/3)+ a_sym) - Z*(-(m_n -m_p)*c**2 + 4*a_sym) + Z**2*(a_c/A**(1/3) + 4*a_sym/A) -56740

plt.plot(x,mass(x))

plt.show()
