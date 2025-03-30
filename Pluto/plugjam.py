# À regarder c'edst important : https://pysdr.org/content/sampling.html
import numpy as np
import adi
import scipy
import matplotlib.pyplot as plt
import time
import os
import datetime

t = time.time()

def acquisition(RXLO  ,RXFS, fft_size = 32768,number_of_intervals = 5000):
    RXLO = int(RXLO) # center frequency to tune to
    RXFS = int(RXFS) # sample rate

    sdr = adi.Pluto("ip:192.168.2.1")
    sdr.sample_rate = int(RXFS)

    sdr.gain_control_mode_chan0 = 'manual'
    sdr.rx_hardwaregain_chan0 = -10 # dB
    sdr.sample_rate = RXFS
    sdr.rx_rf_bandwidth = RXFS
    sdr.rx_buffer_size = int(30e3)


    




    rx_samples = np.zeros((number_of_intervals,fft_size), dtype=np.complex64)
    time_samples = np.zeros(number_of_intervals)

    print("Début de l'acquisition")
    start_time = time.time() - t
    print(start_time)

    for k in range(number_of_intervals):
        rx_samples[k,:sdr.rx_buffer_size] = sdr.rx()
        time_samples[k] = time.time() - t

        if k == number_of_intervals / 2 :
            print("Moitié de l'acquisition")
    print("Fin de l'acquisition")
    end_time = time.time() - t
    print(end_time)
    signal_temporel = np.concatenate(rx_samples).ravel()

    return signal_temporel,rx_samples,(start_time,end_time)


# 2 signaux théoriques : un signal sinusoïdal à 1.93MHz, un autre signal composé de 2 sinusoïdes à 1.93MHz et 1.95MHz  

def spectrograme(fft_size,rx_samples,signal_temporel,RXFS,RXLO,number_of_intervals,temps,ecriture = False):

    blackman_window_fft_size = scipy.signal.windows.blackman(fft_size)

    blackman_window_signal_size = scipy.signal.windows.blackman(fft_size * number_of_intervals)

    t_vec = np.arange(0,float(fft_size * number_of_intervals)/float(RXFS),1./float(RXFS))

    #signal_test_1_freq = np.sin((rf_sampled_frequency - RXLO)*np.pi*2*t_vec)


    #signal_test_2_freq = np.sin((rf_sampled_frequency - RXLO)*np.pi*2*t_vec) + np.sin((rf_sampled_frequency - RXLO + int(20e3))*np.pi*2*t_vec) 

    #fft_signal_test = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(signal_test_2_freq * blackman_window_signal_size, fft_size)))**2)

# signal réel enregistré par la Pluto 

    spectrogram_signal_reel = np.zeros((number_of_intervals, fft_size), dtype=float)

    for i in range(number_of_intervals) :
        spectrogram_signal_reel[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i] * blackman_window_fft_size, fft_size)))**2)




    now = datetime.datetime.now()
    if ecriture :

        fichier = open(f"PlutoSDR/signal_temporel/temporel_{str(now)[:-7]}.txt",'w')
        fichier.writelines(str(signal_temporel.tolist()))
        fichier.close()


        fichier = open(f"PlutoSDR/signal_frequentiel/frequentiel_{str(now)[:-7]}.txt","w")
        fichier.writelines(str(spectrogram_signal_reel.tolist()))
        fichier.close()
        
    avg_db = np.average(spectrogram_signal_reel) 
    spectrogram_signal_reel_filtre = spectrogram_signal_reel > avg_db

    frequences = np.linspace(RXLO -RXFS/2, RXLO + RXFS/2, fft_size)
    print("prout",frequences[0],frequences[-1])

    temps = np.linspace(temps[0],temps[1],number_of_intervals)

    #assert(RXLO - RXFS <= rf_sampled_frequency <= RXLO + RXFS)


    #k = int((rf_sampled_frequency-(RXLO - RXFS))/(2*RXFS)*len(frequences))


    print("caca",spectrogram_signal_reel[100,100])
    plt.imshow(spectrogram_signal_reel, aspect='auto', extent=[RXLO -RXFS/2, RXLO + RXFS/2, temps[0], temps[-1]])
    plt.xlabel("Frequency")
    plt.ylabel("Time")

    plt.show()


RXLO = 490e6
RXFS = 30e6
fft_size = 32768
number_of_interval = 3000

signal_temporel, rx_samples, temps = acquisition(RXLO,RXFS,fft_size,number_of_interval)

spectrograme(fft_size, rx_samples, signal_temporel, RXFS, RXLO, number_of_interval, temps)



