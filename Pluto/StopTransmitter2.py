import adi

sdr = adi.Pluto("usb:1.4.5")

# Effacer le tampon juste pour être sûr
for i in range (0, 10):
    raw_data = sdr.rx()

# Arrêter la transmission
sdr.tx_destroy_buffer()
sdr.tx_cyclic_buffer = False