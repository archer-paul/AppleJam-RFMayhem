import numpy as np
import adi
import matplotlib.pyplot as plt

sample_rate = 30e6 # Hz
center_freq = 2452e6 # Hz

sdr = adi.Pluto("usb:1.8.5")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

sdr.tx_enabled_channels = [0]





N = 1e6 # nombre d'échantillons à transmettre en une seule fois
t = np.arange(N)/sample_rate

n = 100
bandwidth = 30e6
samples = 0
bin = sample_rate/N

for k in range (n):
    samples += (0.995)*np.exp(2.0j*np.pi*(round(((-n/2 +k)*bandwidth/n)/bin)*bin)*t)
samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.

'''fft_size = 32768
RXLO = center_freq

RXFS=bandwidth
affichage = True
samples2 = 200
#collect data
rx_samples = np.zeros((samples2,fft_size), dtype=np.complex64)
for k in range(samples2):
    rx_samples[k,:30000] = sdr.rx()
num_rows = samples2
for i in range(num_rows):
    rx_samples[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i], fft_size)))**2)
# rx_samples = np.flip(rx_samples.astype('float64'), axis=0)
rx_samples = rx_samples.astype('float64')
if affichage :
    plt.imshow(rx_samples, aspect='auto', extent=[RXLO -RXFS/2,RXLO + RXFS/2,samples, 0])
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Time [5 ms]")
    plt.show()'''






# Start the transmitter
sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
sdr.tx(samples) # début de la transmission


plt.plot(samples)

plt.show()



