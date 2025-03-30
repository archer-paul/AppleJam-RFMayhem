import numpy as np
import adi
import matplotlib.pyplot as plt
#signal = np.sin(np.linspace(0,10000,100000)*2*np.pi*830e6)
sdr = adi.Pluto("ip:192.168.2.1")
sdr.tx_cyclic_buffer = True


# def emettre(center_freq,lien, sample_rate = 1e6, temps=5000, sdr = sdr):
sample_rate = 30e6 # Hz


sdr.sample_rate =int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(2.4e9)
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

sdr.tx_enabled_channels = [0]

N = 10000 # nombre d'échantillons à transmettre en une seule fois
sdr._tx_buffer_size = N 
t = np.arange(N)/sample_rate
samples = 0.5*np.exp(2.0*1j*np.pi*100e3*t) # Simulez une sinusoïde de 100 kHz, qui devrait apparaître à 915,1 MHz au niveau du récepteur.
samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.
#sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
# Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.

sdr.tx(samples)
# sdr.tx_cyclic_buffer = False
# for i in range(temps):
#     sdr.tx(samples) # transmettre le lot d'échantillons une fois

# Start the transmitter

plt.plot(samples)
plt.show()

# emettre(2400e6,"ip:192.168.2.1")
