import numpy as np
import adi

#signal = np.sin(np.linspace(0,10000,100000)*2*np.pi*830e6)

def emettre(center_freq,lien, sample_rate = 1e6):
    sample_rate = 15e6 # Hz


    sdr = adi.Pluto(lien)
    sdr.sample_rate =int(sample_rate)
    sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
    sdr.tx_lo = int(center_freq)
    sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

    N = 10000 # nombre d'échantillons à transmettre en une seule fois
    t = np.arange(N)/sample_rate
    samples = 0.5*np.exp(2.0j*np.pi*100e3*t) # Simulez une sinusoïde de 100 kHz, qui devrait apparaître à 915,1 MHz au niveau du récepteur.
    samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.
    #sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
    # Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
    for i in range(5000):
        sdr.tx(samples) # transmettre le lot d'échantillons une fois

# Start the transmitter



emettre(433.956e6,"usb:1.9.5")
