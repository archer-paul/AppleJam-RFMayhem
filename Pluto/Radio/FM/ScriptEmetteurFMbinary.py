import numpy as np
import adi
import random

sample_rate = 30e6 # Hz
center_freq = 600e6 # Hz

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

N = 1e3 # nombre d'échantillons à transmettre en une seule fois
t = np.arange(N)/sample_rate

n = 100
bandwidth = 10e6
bin = sample_rate/N

alea = np.random.randint(-bandwidth, bandwidth, n)

for i in range (1000):
    for k in range (n):
        samples = 0.5*np.exp(2.0j*np.pi*(alea[i])*t)
        samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.
        sdr.tx(samples)
