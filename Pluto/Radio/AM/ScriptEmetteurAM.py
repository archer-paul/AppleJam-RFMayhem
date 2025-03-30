import numpy as np
import adi

def text_to_bits(text):
    return np.unpackbits(np.frombuffer(text.encode(), dtype=np.uint8))

def bits_to_samples(bits):
    return bits +1

sample_rate = 1e6 # Hz
center_freq = 915e6 # Hz

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = -50 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

def send_message(text):
    #ctx = libiio.Context("ip:" + ip)
    #tx = ctx.find_device("cf-ad9361-dds-core-lpc")
    #tx_channel = tx.find_channel("voltage0", is_output=True)
    
    bits = text_to_bits(text)
    samples = bits_to_samples(bits)
    samples *= 2**13

    # Start the transmitter
    sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
    sdr.tx(samples) # début de la transmission

message = "Hello Pluto"
send_message(message)