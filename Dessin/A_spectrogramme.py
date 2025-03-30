import numpy as np
import adi
import matplotlib.pyplot as plt

sample_rate = 30e6 # Hz
center_freq = 600e6 # Hz

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

N = 1e6 # nombre d'échantillons à transmettre en une seule fois
t = np.arange(N)/sample_rate

n = 100
bandwidth = 20e6
samples = 0
bin = sample_rate/N

#les deux barres vertcales du bas
samples = (1/2)*(0.5*np.exp(2.0j*np.pi*(-bandwidth/2)*t) + 0.5*np.exp(2.0j*np.pi*(-bandwidth/2)*t))
samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.
# Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
for i in range(50):
    sdr.tx(samples) # transmettre le lot d'échantillons une fois

#la barre centrale
for k in range (n):
    samples += (0.5/n)*np.exp(2.0j*np.pi*(round(((-n/2 +k)*bandwidth/n)/bin)*bin)*t)
samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.

# Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
for i in range(50):
    sdr.tx(samples) # transmettre le lot d'échantillons une fois

#les deux barres vertcales du milieu
samples = (1/2)*(0.5*np.exp(2.0j*np.pi*(-bandwidth/2)*t) + 0.5*np.exp(2.0j*np.pi*(-bandwidth/2)*t))
samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.
# Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
for i in range(50):
    sdr.tx(samples) # transmettre le lot d'échantillons une fois

#la barre du haut
for k in range (n):
    samples += (0.5/n)*np.exp(2.0j*np.pi*(round(((-n/2 +k)*bandwidth/n)/bin)*bin)*t)
samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.

# Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
for i in range(50):
    sdr.tx(samples) # transmettre le lot d'échantillons une fois

