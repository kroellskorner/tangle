from libhackrf import HackRF
import matplotlib.pyplot as plt
from matplotlib.mlab import psd
import numpy as np

# Initialize HackRF
hackrf = HackRF()

# Adjust LNA and VGA gain settings
try:
    hackrf.set_lna_gain(18)  # Start with a moderate gain
    hackrf.set_vga_gain(18)  # Adjust based on the outcomes
except Exception as e:
    print(f"Error setting gains: {e}")
    hackrf.close()
    raise

# Set sample rate and center frequency
try:
    hackrf.sample_rate = 20e6
    hackrf.center_freq = 2.437e9
except Exception as e:
    print(f"Error setting sample rate or center frequency: {e}")
    hackrf.close()
    raise

# Read samples
try:
    samples = hackrf.read_samples(650000)
except Exception as e:
    print(f"Error reading samples: {e}")
    hackrf.close()
    raise

# Ensure the HackRF device is closed properly after use
finally:
    hackrf.close()

# Estimate and plot the PSD
plt.figure()
psd(samples, NFFT=1024, Fs=hackrf.sample_rate/1e6, Fc=hackrf.center_freq/1e6)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Relative power (dB)')
plt.title('Power Spectral Density (PSD)')
plt.show()
