import numpy as np
import adi


def emettre(center_freq,lien, sample_rate = 1e6):
    sample_rate = 15e6 # Hz


    sdr = adi.Pluto(lien)
    sdr.sample_rate = int(sample_rate)
    sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
    sdr.tx_lo = int(center_freq)
    sdr.tx_hardwaregain_chan0 = -50 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

    N = 1e5# nombre d'échantillons à transmettre en une seule fois
    t = np.arange(N)/sample_rate
    samples = 0.5*np.exp(2.0j*np.pi*100e3*t) # Simulez une sinusoïde de 100 kHz, qui devrait apparaître à 915,1 MHz au niveau du récepteur.
    samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.

    # Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
    for i in range(100):
        sdr.tx(samples) # transmettre le lot d'échantillons une fois
for j in range(100):
    emettre(2400e6,"usb:1.4.5")