# À regarder c'edst important : https://pysdr.org/content/sampling.html


import numpy as np
import adi
import scipy
import matplotlib.pyplot as plt
import time

t = time.time()

rf_sampled_frequency = int(866.93e6)
RXLO = int(865e6) # center frequency to tune to
RXFS = int(30e6) # sample rate
# RXBW = int(200e6)

sdr = adi.Pluto("ip:192.168.2.11")
sdr.sample_rate = int(RXFS)

sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0 # dB
sdr.rx_lo = RXLO
sdr.sample_rate = RXFS
sdr.rx_rf_bandwidth = RXFS
sdr.rx_buffer_size = 32768


fft_size = 32768 


number_of_intervals = 500


rx_samples = np.zeros((fft_size), dtype=np.complex64)

print("Début de l'acquisition")
start_time = time.time() - t
print(start_time)
rx_samples = sdr.rx()

# for k in range(number_of_intervals):
#     rx_samples[k,:sdr.rx_buffer_size] = sdr.rx()

# signal_temporel = []
# for k in range(number_of_intervals):
#     signal_temporel = signal_temporel + rx_samples[k,:sdr.rx_buffer_size].tolist()
#     if k == number_of_intervals / 2 :
#         print("Moitié de l'acquisition")
print("Fin de l'acquisition")
# signal_temporel = np.array(signal_temporel)


# 2 signaux théoriques : un signal sinusoïdal à 1.93MHz, un autre signal composé de 2 sinusoïdes à 1.93MHz et 1.95MHz  

blackman_window = scipy.signal.windows.blackman(fft_size)

t_vec = np.arange(0,float(fft_size)/float(RXFS),1./float(RXFS))

signal_test_1_freq = np.sin((rf_sampled_frequency - RXLO)*np.pi*2*t_vec)


signal_test_2_freq = np.sin((rf_sampled_frequency - RXLO)*np.pi*2*t_vec) + np.sin((rf_sampled_frequency - RXLO + int(20e3))*np.pi*2*t_vec) 

fft_signal_test = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(signal_test_2_freq * blackman_window, fft_size)))**2)

# signal réel enregistré par la Pluto 

fft_signal_reel = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples/float(1e3) * blackman_window, fft_size)))**2)







temps = np.linspace(0,1, signal_test_2_freq.size)

frequences = np.linspace(- RXFS / 2,RXFS / 2, fft_signal_test.size)


# for k in range(number_of_intervals) :
#     rx_samples[k,:sdr.rx_buffer_size] = signal_test[k*sdr.rx_buffer_size:(k+1)*sdr.rx_buffer_size]

figure, axis = plt.subplots(2, 1)
axis[0].plot(temps, rx_samples) 
axis[0].set_title("Signal temporel")
axis[1].plot(frequences, fft_signal_reel) 
axis[1].set_ylim(bottom = 0)
axis[1].set_title("TF")
plt.show()
# b, a = scipy.signal.butter(4, ((rf_sampled_frequency - 1e6 - RXLO)/RXFS + 1/2,(rf_sampled_frequency + 1e6 - RXLO)/RXFS +1/2), 'bandpass', analog=False)
# signal_bandpass = scipy.signal.filtfilt(b, a, signal_test)


# print("Fin de l'acquisition")
# end_time = time.time() - t

# temps = np.linspace(0,end_time - start_time,signal_test.size)
# w, h = scipy.signal.freqs(b, a)


# figure, axis = plt.subplots(3, 1)

# axis[0].plot(temps, signal_test) 
# axis[0].set_title("Signal bruité")
# axis[1].plot(temps, signal_bandpass) 
# axis[1].set_title("Signal débruité ?")
# axis[2].semilogx((w - 1/2)*RXFS + RXLO, 20 * np.log10(abs(h)))
# axis[2].set_title('Butterworth filter frequency response')

# axis[2].margins(0, 0.1)
# axis[2].grid(which='both', axis='both')
# axis[2].axvline(rf_sampled_frequency, color='green') # cutoff frequency
# plt.show()


# print(end_time)
# print("Durée")
# duration = end_time - start_time
# print(duration)



# num_rows = number_of_intervals

# power_array = np.zeros(num_rows)

# blackman_window = scipy.signal.windows.blackman(fft_size)

# psd = np.zeros((number_of_intervals, fft_size), dtype=np.complex64)

# bb_sampled_frequency = rf_sampled_frequency - RXLO


# for i in range(num_rows):
#     psd[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i] * 1/(10e3) * blackman_window, fft_size)))**2)


# psd = psd.astype('float64')

# max_power = np.max(psd, axis=0)


# plt.imshow(psd, aspect='auto', extent=[RXLO -RXFS/2 ,RXLO + RXFS/2, 0, duration])
# plt.show()

# f = np.linspace(RXLO - RXFS / 2, RXLO + RXFS / 2, len(max_power))

# plt.plot(f,max_power)
# plt.show()




# f = np.linspace(0,duration,number_of_intervals)

# plt.plot(f,power_array)








