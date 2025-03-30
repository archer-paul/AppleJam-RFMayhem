import numpy as np
import adi

def samples_to_symbols(samples):
    n = len(samples)
    symbols = np.zeros(n)
    for k in range (n):
        x = samples[k].real
        y =samples[k].imag
        if x >= 0 and y >= 0 :
            symbols[k] = 0
        elif x < 0 and y >= 0 :
            symbols[k] = 1 
        elif x >= 0 and y < 0 :
            symbols[k] = 2
        else :
            symbols[k] = 3

    return symbols

def symbols_to_bytes(symbols):
    n = len(symbols)
    bits = np.zeros(n//8)
    for k in range(n//16):
        s0, s1, s2, s3 = 0, 0, 0, 0
        for l in range(16):
            match symbols[16*k + l]:
                case 0 :
                    s0 += 1
                case 1 :
                    s1 += 1
                case 2 :
                    s2 += 1
                case 3 :
                    s3 += 1
        m = max(s0, s1, s2, s3)
        if s0 == m:
            bits[2*k], bits[2*k + 1] = 0, 0
        elif s1 == m:
            bits[2*k], bits[2*k + 1] = 0, 1
        elif s2 == m:
            bits[2*k], bits[2*k + 1] = 1, 0
        else:
            bits[2*k], bits[2*k + 1] = 1, 1
    return bits
        

def bits_to_text(bits):
    bytes = np.packbits(bits)
    return bytes.tobytes().decode()

sample_rate = 1e6 # Hz
center_freq = 915e6 # Hz
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
    symbols = samples_to_symbols(rx_samples)
    print(symbols[0:100])
    bits = symbols_to_bytes(symbols)
    #text = bits_to_text(bits)s

    return bits

print(receive_message())