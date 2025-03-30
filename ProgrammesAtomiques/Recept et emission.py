import numpy as np
import adi
import matplotlib.pyplot as plt
import time as t



def emettre(signal,lien, center_freq, sample_rate = 1e6):
    sample_rate = 1e6

    sdr = adi.Pluto(lien)
    sdr.rx_buffer_size = 30e3
    sdr.sample_rate = int(sample_rate)
    sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
    sdr.tx_lo = int(center_freq)
    sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB

    N = len(signal) # nombre d'échantillons à transmettre en une seule fois
    t = np.arange(N)/sample_rate
    print(np.max(np.abs(signal)))
    samples = 0.1*signal/np.max(np.abs(signal)) # Simulez une sinusoïde de 100 kHz, qui devrait apparaître à 915,1 MHz au niveau du récepteur.
    samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.
    plt.plot(samples)
    plt.show()
    
    # Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
    for i in range(len(signal)):

        sdr.tx(samples) # transmettre le lot d'échantillons une fois
        







def recep(RXLO = int(433.956e6), RXFS=int(4e6), samples = 500, fft_size = 8192):





    #configure receiver settings
    sdr = adi.Pluto("ip:192.168.2.1")

    sdr.rx_rf_port_select_chan0 = "A_BALANCED"
    sdr.rx_lo = RXLO
    sdr.sample_rate = RXFS
    sdr.gain_control_mode_chan0 = "manual"
    sdr.rx_hardwaregain_chan0 = 50
    sdr.rx_buffer_size = int(8e3)

    debut = t.time()
    #collect data
    rx_samples = np.zeros((samples,fft_size), dtype=np.complex64)
    
    
    for k in range(samples):
        rx_samples[k,:8192] = sdr.rx()
        num_rows = samples

    
    fin = t.time() - debut

    rx_samples1 = np.copy(rx_samples)

    for k in range(samples):
        rx_samples[k,:8000] = sdr.rx()

    for i in range(num_rows):
        rx_samples[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i], fft_size)))**2)

    rx_samples = np.flip(rx_samples.astype('float64'), axis=0)

    rx_samples1 = np.concatenate(rx_samples1).ravel()

    if True :
        plt.imshow(rx_samples, aspect='auto', extent=[RXLO -RXFS/2,RXLO + RXFS/2,0, samples,])
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Time [5 ms]")
        plt.show()

        # plt.plot(t,np.concatenate(rx_samples1).ravel())
        # plt.show()

    return np.concatenate(rx_samples).ravel()

a = recep(RXLO = int(433.956e6), RXFS=int(4e6))

aquisition = True

if aquisition :
    a = recep(RXLO = int(433.956e6), RXFS=int(30e6))
else :
    fichier = open("signal.txt","r")
    a = eval(fichier.readlines()[0])
    fichier.close()
    print(a[0:100])

print("recp finie")
#   python3 spectrogram.py


emettre(a,"ip:192.168.2.1",433.956e6)
