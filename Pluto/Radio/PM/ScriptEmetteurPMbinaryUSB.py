import numpy as np
import adi

#def text_to_bits(text):
#    return np.unpackbits(np.frombuffer(text.encode(), dtype=np.uint8))

def bits_to_samples(bits):
    n = len(bits)//2 -1
    samples  = np.zeros(n)
    for k in range (n):
        match bits[2*k], bits[2*k +1] :
            case 0, 0 :
                samples[k] = 0
            case 0, 1 :
                samples[k] = 1
            case 1, 0 :
                samples[k] = 2
            case 1 , 1 :
                samples[k] = 3

    return samples

sample_rate = 100e6 # Hz
center_freq = 900e6 # Hz

sdr = adi.Pluto("usb:1.7.5")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

def send_message(bits):
    print(bits)
    samples = bits_to_samples(bits)
    print(samples)
    
    x_degrees = samples*360/4.0 + 45 # 45, 135, 225, 315 degrees
    x_radians = x_degrees*np.pi/180.0 # sin() et cos() avec des angles en radians
    x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) # ce qui produit nos symboles complexes QPSK

    print(x_symbols)

    samples = np.repeat(x_symbols, 16) # 16 échantillons par symbole (impulsions rectangulaires)
    samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non entre -1 et +1 comme certains SDRs.
    # Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
    
    # Start the transmitter
    sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
    sdr.tx(samples) # début de la transmission
    
bits = np.zeros(100)
for k in range (25):
       bits[4*k +2], bits[4*k +3] = 1, 0

send_message(bits)