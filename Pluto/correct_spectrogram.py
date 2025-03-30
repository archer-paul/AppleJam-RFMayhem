import numpy as np
import adi
import scipy
import matplotlib.pyplot as plt
import time

t = time.time()

rf_sampled_frequency = int(433.92e6)
RXLO = int(2430e6) # center frequency to tune to
RXFS = int(10e6) # sample rate

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(RXFS)

sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0 # dB
sdr.rx_lo = RXLO
sdr.sample_rate = RXFS
sdr.rx_rf_bandwidth = RXFS
sdr.rx_buffer_size = 30000


number_of_intervals = 6000


rx_samples = np.zeros((number_of_intervals,32768), dtype=np.complex64)

print("Début de l'acquisition")
start_time = time.time() - t
print(start_time)

for k in range(number_of_intervals):
    rx_samples[k,:sdr.rx_buffer_size] = sdr.rx()
print("Fin de l'acquisition")
end_time = time.time() - t
print(end_time)
print("Durée")
duration = end_time - start_time
print(duration)



fft_size = 32768
num_rows = number_of_intervals

power_array = np.zeros(num_rows)

blackman_window = scipy.signal.windows.blackman(fft_size)

psd = np.zeros((number_of_intervals, fft_size), dtype=np.complex64)

bb_sampled_frequency = rf_sampled_frequency - RXLO


for i in range(num_rows):
    psd[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rx_samples[i] * 1/(10e3) * blackman_window, fft_size)))**2)


psd = psd.astype('float64')

max_power = np.max(psd, axis=0)


plt.imshow(psd, aspect='auto', extent=[RXLO -RXFS/2 ,RXLO + RXFS/2, 0, duration])
plt.show()

f = np.linspace(RXLO - RXFS / 2, RXLO + RXFS / 2, len(max_power))

plt.plot(f,max_power)
plt.show()




# f = np.linspace(0,duration,number_of_intervals)

# plt.plot(f,power_array)








