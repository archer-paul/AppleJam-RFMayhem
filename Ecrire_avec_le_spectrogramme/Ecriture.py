import numpy as np
import matplotlib.pyplot as plt
import adi
import time

texte = "APPLEJAM"

def emission_lettre(lettre,sdr):
    img = np.average(plt.imread(f"/cal/exterieurs/tsoubise-23/Desktop/Applejam/applejam/Ecrire_avec_le_spectrogramme/{lettre}1.png"),axis = 2).T
    n = len(img[0])
    samples = []
    for nx,x in enumerate(img):
        pix = []
        n = len(x)
        if False :
            plt.imshow([x])
            plt.show()
        debut = time.time()
        for ny,y in enumerate(x):
            if y < 0.95 :
                pix.append(ny/(len(x)-1)*30e6-15e6)
        
        samples.append(emettre(sdr,pix,n))
    
    return np.array(samples)




sample_rate = 30e6 # Hz
center_freq = 2400e6 # Hz


sdr = adi.Pluto("usb:1.8.5")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate) # la coupure du filtre, il suffit de la régler sur la même fréquence d'échantillonnage.
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Augmenter pour augmenter la puissance tx, la plage valide est de -90 à 0 dB
sdr.tx_cyclic_buffer = True
sdr.tx_enabled_channels = [0]





def emettre(sdr,pix,p):
    sample_rate = 30e6 # Hz



    bandwidth = 30e6

    N = int(1000) # nombre d'échantillons à transmettre en une seule fois
    n = N//p
    bin = sample_rate/N
    t = np.arange(N)/sample_rate
    samples = np.zeros((len(t)), dtype = complex)


    for k in pix:
        for i in range(n):
            samples += (0.9/n)*np.exp(2.0j*np.pi*(round(((-N/2 +k*n+i)*bandwidth/N)/bin)*bin)*t)
            #print(round(((-N/2 +k+i)*bandwidth/N)/bin)*bin//1e6)
    samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.


    

    if False: 
        print(np.array(pix)//int(1e6))
           # Transmettez notre lot d'échantillons 100 fois, ce qui devrait représenter 1 seconde d'échantillons au total, si l'USB peut suivre.
    if False : 
        sdr.tx_destroy_buffer()
        sdr.tx(samples) # transmettre le lot d'échantillons une fois
    
    else :
        return samples

 
"""
   n = 20
    bandwidth = 20e6
    samples = 0
    for k in range (n):

    samples *= 2**14 # Le PlutoSDR s'attend à ce que les échantillons soient compris entre -2^14 et +2^14, et non -1 et +1 comme certaines SDRs.
"""

def spectrogram(signal, samples = 200, fft_size = 32768, affichage = True):

    """
    n = len(signal)
    print("n",n)
    p = n//samples
    print("p",p)
    rx_samples = np.zeros((samples,fft_size), dtype = complex)shape
1000
    for k in range(samples):
        rx_samples[k,:p] = signal[k*p:(k+1)*p]
    """
    rx_samples = []
    print(fft_size)
    samples = round(len(signal)/fft_size)
    for k in range(samples):
        rx_samples.append(signal[k*fft_size:(k+1)*fft_size])
    rx_samples = np.array(rx_samples)




    rx_samples2 = signal
    num_rows = samples
    for i in range(num_rows):
        rx_samples[i,:] = 20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i], int(fft_size)))))
    
    if True:
        plt.imshow(rx_samples, aspect='auto', extent=[-15e6,15e6,samples, 0])
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Time [5 ms]")
        plt.show()


        plt.plot(np.linspace(0,len(rx_samples2),len(rx_samples2)),rx_samples2)
        plt.show()



def cos_sureleve(f,t):
    return (1+np.cos(t*2*f*np.pi))/1
samples = []
fft_size = 0
for t in texte:
    if len(samples) > 0:
        lettre = emission_lettre(t,sdr)
        assert(fft_size == int(2**(np.log2(lettre.shape[1])//1+1)))
        lettre = np.concatenate((lettre,np.zeros((len(lettre),fft_size-len(lettre[0])))), axis = 1)
        samples = np.concatenate((samples,lettre), axis = 1)
    else :
        samples = emission_lettre(t,sdr)
        fft_size = int(2**(np.log2(samples.shape[1])//1+1))
        samples = np.concatenate((samples,np.zeros((len(samples),fft_size-len(samples[0])))), axis = 1)

samples = np.concatenate(np.copy(samples)).ravel()

spectrogram(samples, fft_size = fft_size)









'''fft_size = 32768
RXLO = center_freq

RXFS=bandwidth
affichage = True
samples2 = 200
#collect data
rx_samples = np.zeros((samples2,fft_size), dtype=np.complex64)
for k in range(samples2):
    rx_samples[k,:30000] = sdr.rx()1000
num_rows = samples2
for i in range(num_rows):
    rx_samples[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i], fft_size)))**2)
# rx_samples = np.flip(rx_samples.astype('float64'), axis=0)
rx_samples = rx_samples.astype('float64')
if affichage :
    plt.imshow(rx_samples, aspect='auto', extent=[RXLO -RXFS/2,RXLO + RXFS/2,samples, 0])
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Time [5 ms]")
    plt.show()'''






# Start the transmitter
"""
sdr.tx_cyclic_buffer = True # Activer les tampons cycliques
sdr.tx(samples) # début de la transmission


plt.plot(samples)

plt.show()

"""
