import numpy as np
import adi
import matplotlib.pyplot as plt


sample_rate = 1e6 # Hz
center_freq = 600e6 # Hz

sdr = adi.Pluto("usb:1.7.5")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB


# Paramètres du signal
f_central = 1e6  # Fréquence centrale en Hz
bandwidth = 20e6  # Largeur de bande en Hz
t_duration = 1e-3  # Durée du signal en secondes
fs = sample_rate

# Génération de l'axe temporel
t = np.arange(0, t_duration, 1/fs)

# Fréquence du signal créneau
f_square = bandwidth / 2  # Fréquence du signal créneau

# Génération du signal créneau
signal = np.sign(np.sin(2 * np.pi * f_central * t)) * (np.abs(np.sin(2 * np.pi * f_square * t)) > 0.5)

# Visualisation du signal
plt.figure(figsize=(10, 6))
plt.plot(t, signal)
plt.title('Signal créneau centré à 100 kHz avec une largeur de bande de 20 kHz')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


N = 10000 # nombre d'échantillons à transmettre en une seule fois
t = np.arange(N)/sample_rate
samples = (2**14)*signal # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.

# Start the transmitter
sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
sdr.tx(samples) # début de la transmission