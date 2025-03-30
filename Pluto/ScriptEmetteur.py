import numpy as np
import matplotlib.pyplot as plt
import adi

def spectrogram(data, RXLO=int(430e6), RXFS=int(30e5), samples=200, fft_size=32768, affichage=False):

    
    # Collecter les données
    rx_samples = np.zeros((samples, fft_size), dtype=np.complex64)

    print(len(sdr.rx()))
    for k in range(len(data)/30000):
        print(k)
        rx_samples[k, :30000] = sdr.rx()[k*30000:(k+1)*30000]

    num_rows = samples
    for i in range(num_rows):
        rx_samples[i, :] = 10 * np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i], fft_size))) ** 2)

    rx_samples = rx_samples.astype('float64')

    if affichage:
        plt.imshow(rx_samples, aspect='auto', extent=[RXLO - RXFS / 2, RXLO + RXFS / 2, samples, 0])
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Time [5 ms]")
        plt.show()

    return rx_samples

def setup(duration):
    sdr = adi.Pluto("usb:1.4.5")
    sdr.rx_lo = RXLO
    sdr.sample_rate = RXFS
    sdr.gain_control_mode_chan0 = "manual"
    sdr.rx_hardwaregain_chan0 = 40
    sdr.rx_buffer_size = int(RXFS * duration)
    sdr.tx_cyclic_buffer = True
    return sdr


def max_freq(data, RXLO=int(430e6), RXFS=int(30e6), samples=200, fft_size=32768, affichage=False):
    a = spectrogram(RXLO, RXFS, samples, fft_size, affichage)
    max_a = a.max()
    max_temps_index, max_freq_index = np.where(a == max_a)
    max_freq = RXLO - RXFS / 2 + max_freq_index * RXFS / fft_size
    return max_freq

def record_signal(sdr, RXLO=int(430e6), RXFS=int(30e6), duration=1):

    # Enregistrer les échantillons
    samples = sdr.rx()
    #np.save("recorded_signal.npy", samples)
    return samples

def replay_signal(sdr, data, file_path="recorded_signal.npy", RXLO=int(430e6), RXFS=int(30e6)):

    # Charger les échantillons enregistrés
    samples = data
    print(samples[:20])
    sdr.tx(samples)

duration = 1e-2
RXLO = int(430e6)
RXFS = int(30e6)
sdr = setup(duration)
# Enregistrer un signal
data = record_signal(sdr, RXLO=RXLO, RXFS=RXFS, duration=duration)

# Rejouer le signal enregistré
replay_signal(sdr, data = data, file_path="recorded_signal.npy", RXLO=RXLO, RXFS=RXFS)

# Afficher le spectrogramme et trouver la fréquence maximale
#print(max_freq(RXLO=RXLO, RXFS=RXFS, samples=500, fft_size=32768, affichage=True))
