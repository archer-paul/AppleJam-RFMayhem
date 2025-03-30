import numpy as np
import adi
import matplotlib.pyplot as plt

sample_rate = 1e6 # Hz
center_freq = 915e6 # Hz
num_samps = 100000 # nombre d'échantillons par appel à rx()

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)

# Config Tx
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = -50 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB


# Créer une forme d'onde de transmission (QPSK, 16 échantillons par symbole)
num_symbols = 1000
x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
x_degrees = x_int*360/4.0 + 45 # 45, 135, 225, 315 degrees
x_radians = x_degrees*np.pi/180.0 # sin() et cos() avec des angles en radians
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) # ce qui produit nos symboles complexes QPSK
samples = np.repeat(x_symbols, 16) # 16 échantillons par symbole (impulsions rectangulaires)
samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non entre -1 et +1 comme certains SDRs.

# Start the transmitter
sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
sdr.tx(samples) # début de la transmission
