import numpy as np
import libiio

def text_to_bits(text):
    return np.unpackbits(np.frombuffer(text.encode(), dtype=np.uint8))

def bits_to_samples(bits):
    return np.where(bits == 0, -1.0, 1.0)

def send_message(ip, text):
    ctx = libiio.Context("ip:" + ip)
    tx = ctx.find_device("cf-ad9361-dds-core-lpc")
    tx_channel = tx.find_channel("voltage0", is_output=True)
    
    bits = text_to_bits(text)
    samples = bits_to_samples(bits)
    
    buffer = libiio.Buffer(tx, len(samples), cyclic=True)
    buffer.write(samples.tobytes())
    buffer.push()
    
    buffer.destroy()
    ctx.destroy()

send_ip = "192.168.2.1"  # IP de l'émetteur Pluto SDR
message = "Hello Pluto"
send_message(send_ip, message)
