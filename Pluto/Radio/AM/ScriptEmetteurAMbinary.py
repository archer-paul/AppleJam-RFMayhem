import numpy as np
import adi

n = 6

def bits_to_samples(bits):
    return np.where(bits == 0, 1, 2**n)

sample_rate = 30e6 # Hz
center_freq = 605e6 # Hz

sdr = adi.Pluto("ip:192.168.2.1")

sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.gain_control_mode_chan0 = 'manual'
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

def send_message(bits):
    print(bits)
    samples = bits_to_samples(bits)
    samples *= 2**(14-n)

    for k in range (10000):
        sdr.tx(samples) # début de la transmission

bits = np.random.randint(0, 2, 10000)

send_message(bits)