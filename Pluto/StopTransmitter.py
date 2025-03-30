import adi

sdr = adi.Pluto("ip:192.168.2.1")

# Effacer le tampon juste pour être sûr
for i in range (0, 10):
    raw_data = sdr.rx()

# Arrêter la transmission
sdr.tx_destroy_buffer()