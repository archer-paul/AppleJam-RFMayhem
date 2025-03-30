import numpy as np
import adi

sample_rate = 1e6 # Hz
center_freq = 100e6 # Hz
num_samps = 10000 # nombre d'échantillons retournés par appel à rx()

sdr = adi.Pluto('ip:192.168.2.1')
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 70.0 # dB
sdr.rx_lo = int(center_freq)
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate) # largeur du filtre, il suffit de le mettre au même niveau que la fréquence d'échantillonnage pour l'instant.
sdr.rx_buffer_size = num_samps

samples = sdr.rx() # recevoir des échantillons de la Pluton
print(samples[0:10])    