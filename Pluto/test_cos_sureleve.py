import matplotlib.pyplot as plt 
import numpy as np 


def cos_sureleve(t,f):
    return (1+np.cos(t*f*2*np.pi))*f/2


def g(t, frequency, rho):
    T_s = 1 / frequency
    num = (4 * rho / (np.pi * np.sqrt(T_s))) * (
        np.cos((1 + rho) * np.pi * t / T_s) + 
        (T_s / (4 * rho * t)) * np.sin((1 - rho) * np.pi * t / T_s)
    )
    denom = 1 - (4 * rho * t / T_s) ** 2
    return num / denom

# Exemple d'utilisation
frequency = 1  # 1 kHz
t = np.linspace(-1, 1, 1000)  # Temps de -1 à 1 seconde
rho = 0.1

plt.plot(t,g(t, frequency, rho))
plt.show()