import adi
sdr = adi.Pluto('ip:192.168.2.1') # ou quel que soit l'IP de votre Pluton
sdr.sample_rate = int(2.5e6)
sdr.rx()