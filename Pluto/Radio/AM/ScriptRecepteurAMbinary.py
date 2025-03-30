import numpy as np
import adi

def samples_to_bits(samples):
    samples = np.abs(samples)
    avg = np.mean(samples)
    return np.where(samples < avg, 0, 1)


sample_rate = 1e6 # Hz
center_freq = 500e6 # Hz
num_samps = 100000 # nombre d'échantillons retournés par appel à rx()

sdr = adi.Pluto("ip:192.168.2.1")
sdr.gain_control_mode_chan0 = 'slow_attack'
#sdr.rx_hardwaregain_chan0 = 70.0 # dB
sdr.rx_lo = int(center_freq)
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate) # largeur du filtre, il suffit de le mettre au même niveau que la fréquence d'échantillonnage pour l'instant.
sdr.rx_buffer_size = num_samps

def receive_message():
    # Recevoir des échantillons
    rx_samples = sdr.rx() 
    bits = samples_to_bits(rx_samples)

    return bits[0:100]

print(receive_message())