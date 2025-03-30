import numpy as np
import adi
import matplotlib.pyplot as plt
import time

sample_rate = 10e6 # Hz
center_freq = 1e9 # Hz

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate) # la fréquence de coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.rx_lo = int(center_freq)
sdr.rx_buffer_size = 2**12 # c'est le tampon que le Pluto utilise pour mettre en mémoire tampon les échantillons
s = 0

start_time = time.time()
for k in range(100):
    samples = sdr.rx()
    s += len(samples)

end_time = time.time()
secondes_écoulées = end_time - start_time
taux_de_reception = s/secondes_écoulées
taux_de_pertes = 1 - taux_de_reception/sample_rate

print(taux_de_reception)
print(taux_de_pertes)