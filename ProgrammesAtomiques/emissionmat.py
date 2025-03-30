import numpy as np
import adi
import h5py

f = h5py.File('/home/ah/Documents/LTE20.mat','r')

data = f.get('data')

data=np.array(data)


def emission(sample_rate=30e6, center_freq=2400e6, lien="ip:192.168.2.1", temps=500) :


    sdr = adi.Pluto(lien)
    sdr.sample_rate = int(sample_rate)
    sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
    sdr.tx_lo = int(center_freq)
    sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

    N = 1e6 # nombre d'échantillons à transmettre en une seule fois
    t = np.arange(N)/sample_rate

    n = 100
    bandwidth = 20e6
    samples = 0
    bin = sample_rate/N

    for k in range (n):
        samples += (0.5/n)*np.exp(2.0j*np.pi*(round(((-n/2 +k)*bandwidth/n)/bin)*bin)*t)
    samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.

    for _ in range(temps) :
        sdr.tx(matsignal)
    return


print(data)