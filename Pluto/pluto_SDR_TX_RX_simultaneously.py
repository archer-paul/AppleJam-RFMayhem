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

# Configurer Rx
sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 50.0 # dB, augmenter pour augmenter le gain de réception, mais attention à ne pas saturer le CAN

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

# Effacer le tampon juste pour être sûr
for i in range (0, 10):
    raw_data = sdr.rx()

# Recevoir des échantillons
rx_samples = sdr.rx()
print(rx_samples)

# Arrêter la transmission
sdr.tx_destroy_buffer()

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
