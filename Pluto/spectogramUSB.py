
"""

    RXLO center frequency to tune to
    RXBW bandwidth
    RXFS sample rate


This program uses the PlutoSDR to capture a second of samples and then compute the fft's over 5ms intervals
in order to generate a spectrogram. 
Some things to take into consideration:
    *Since the pluto returns IQ complex samples, it is sufficient for the sample rate to be equal to the bandwidth
    *A bandwidth/sample rate of 3MHz was chosen since the vqd seems to be limited to at least a 2MHz frequency rate
    *The buffer only returns 30,000 samples which is 5ms of samples, but the rx_samples array is zero-padded to 32768 
    which is a power of two so that the fft computation can be done faster
Future considerations:
    *I will create this into a class for testing purposes such as determining if polling one batch of samples and then
    computing the fft repeatedly is more efficient than using daemon threads
    *I will do the computations using Welch's method rather than a regular fft since it is supposedly faster, yet 
    rounds data which may or may not be beneficial
"""

import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import adi

def spectrogram(RXLO = int(430e6), RXFS=int(30e6), samples = 200, fft_size = 32768, affichage = False):





    #configure receiver settings
    sdr = adi.Pluto("usb:1.7.5")

    sdr.rx_rf_port_select_chan0 = "A_BALANCED"
    sdr.rx_lo = RXLO
    sdr.sample_rate = RXFS
    sdr.gain_control_mode_chan0 = "manual"
    sdr.rx_hardwaregain_chan0 = 0
    sdr.rx_buffer_size = int(30e3)

    #collect data
    rx_samples = np.zeros((samples,fft_size), dtype=np.complex64)

    for k in range(samples):
        rx_samples[k,:30000] = sdr.rx()


    num_rows = samples
    for i in range(num_rows):
        rx_samples[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i], fft_size)))**2)

    # rx_samples = np.flip(rx_samples.astype('float64'), axis=0)

    rx_samples = rx_samples.astype('float64')

    if affichage :
        plt.imshow(rx_samples, aspect='auto', extent=[RXLO -RXFS/2,RXLO + RXFS/2,samples, 0])
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Time [5 ms]")
        plt.show()

    return rx_samples


def max_freq(RXLO = int(430e6), RXFS=int(30e6), samples = 200, fft_size = 32768, affichage = False) :


    a = spectrogram(RXLO, RXFS, samples, fft_size, affichage)

    max_a = a.max()
    max_temps_index, max_freq_index = np.where(a == max_a)
    print(max_a, max_freq_index, max_temps_index)
    max_freq = RXLO - RXFS / 2 + max_freq_index * RXFS / fft_size
    return max_freq


print(max_freq(RXLO = int(610e6), RXFS=int(30e6), samples = 500, fft_size = 32768, affichage = True))
