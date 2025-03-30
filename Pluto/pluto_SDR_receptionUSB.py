import numpy as np
import adi

sample_rate = 30e6 # Hz
center_freq = 895e6 # Hz
num_samps = 50000 # nombre d'échantillons retournés par appel à rx()

import matplotlib.pyplot as plt

sdr = adi.Pluto("usb:1.18.5")
sdr.gain_control_mode_chan0 = 'slow_attack'
sdr.rx_lo = int(center_freq)
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate) # largeur du filtre, il suffit de le mettre au même niveau que la fréquence d'échantillonnage pour l'instant.
sdr.rx_buffer_size = num_samps

samples = sdr.rx() # recevoir des échantillons de la Pluton
print(samples[0:100])

psd = np.abs(np.fft.fftshift(np.fft.fft(samples)))**2
psd_dB = 10*np.log10(psd)
f = np.linspace(sample_rate/-2, sample_rate/2, len(psd))

# Tracer le domaine temporel
plt.figure(0)
plt.plot(np.real(samples[::100]))
plt.plot(np.imag(samples[::100]))
plt.xlabel("temps")

# Tracer le domaine freq
plt.figure(1)
plt.plot(f/1e6, psd_dB)
plt.xlabel("Frequences [MHz]")
plt.ylabel("DSP")
plt.show()

