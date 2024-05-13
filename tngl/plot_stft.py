import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

from libhackrf import *

hackrf = HackRF()

# Adjust LNA and VGA gain settings
hackrf.set_lna_gain(8) # Start with a moderate gain
hackrf.set_vga_gain(8) # Adjust based on the outcomes

hackrf.sample_rate = 20e6
hackrf.center_freq = 2.437e9

samples = hackrf.read_samples(650000)


# Parameters for STFT
nperseg = 1024  # Number of points per segment for STFT

# Compute the STFT
frequencies, times, Zxx = stft(np.log(10, samples), fs=hackrf.sample_rate/1e6, nperseg=nperseg)

# Plot the STFT
plt.figure(figsize=(10, 6))
plt.pcolormesh(times, frequencies, np.abs(Zxx), shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Intensity')
plt.show()