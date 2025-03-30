import numpy as np
import adi
import matplotlib.pyplot as plt

sample_rate = 1e6 # Hz
center_freq = 915e6 # Hz
num_samps = 100000 # nombre d'échantillons par appel à rx()

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)

# Configurer Rx
sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 50.0 # dB, augmenter pour augmenter le gain de réception, mais attention à ne pas saturer le CAN


# Effacer le tampon juste pour être sûr
for i in range (0, 10):
    raw_data = sdr.rx()

# Recevoir des échantillons
rx_samples = sdr.rx()
print(rx_samples)


# Calculer la densité spectrale de puissance (version du signal dans le domaine de la fréquence)
psd = np.abs(np.fft.fftshift(np.fft.fft(rx_samples)))**2
psd_dB = 10*np.log10(psd)
f = np.linspace(sample_rate/-2, sample_rate/2, len(psd))

# Tracer le domaine temporel
plt.figure(0)
plt.plot(np.real(rx_samples[::100]))
plt.plot(np.imag(rx_samples[::100]))
plt.xlabel("temps")

# Tracer le domaine freq
plt.figure(1)
plt.plot(f/1e6, psd_dB)
plt.xlabel("Frequences [MHz]")
plt.ylabel("DSP")
plt.show()
