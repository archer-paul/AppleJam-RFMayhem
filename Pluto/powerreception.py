import numpy as np
import adi
import scipy
import matplotlib.pyplot as plt
import time

t = time.time()

rf_sampled_frequency = int(2437e6)
RXLO = int(2430e6) # center frequency to tune to
RXFS = int(10e6) # sample rate

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(RXFS)

sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0 # dB
sdr.rx_lo = RXLO
sdr.sample_rate = RXFS
sdr.rx_rf_bandwidth = RXFS
sdr.rx_buffer_size = 1000


number_of_intervals = 11663


rx_samples = np.zeros((number_of_intervals,1024), dtype=np.complex64)

print("Début de l'acquisition")
start_time = time.time() - t
print(start_time)

for k in range(number_of_intervals):
    rx_samples[k,:1000] = sdr.rx()
print("Fin de l'acquisition")
end_time = time.time() - t
print(end_time)
print("Durée")
duration = end_time - start_time
print(duration)



fft_size = 1024
num_rows = number_of_intervals

power_array = np.zeros(num_rows)

blackman_window = scipy.signal.windows.blackman(fft_size)

psd = np.zeros((number_of_intervals, 1024), dtype=np.complex64)

bb_sampled_frequency = rf_sampled_frequency - RXLO


for i in range(num_rows):
    psd[i,:] = 10*np.log10(np.abs((np.fft.fft(rx_samples[i] * 1/(10e3) * blackman_window, 1024)))**2)
    correct_bin = round(bb_sampled_frequency * fft_size / RXFS)
    power_array[i] = psd[i,correct_bin]


power_array = power_array.astype('float64')



f = np.linspace(0,duration,number_of_intervals)

plt.plot(f,power_array)

plt.show()



print(power_array)




