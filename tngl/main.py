import numpy as np
import json
import os
from scipy.signal import stft
import matplotlib.pyplot as plt

# Placeholder for HackRF setup and sample collection
class HackRF:
    def __init__(self, sample_rate, center_freq, duration):
        self.sample_rate = sample_rate
        self.center_freq = center_freq
        self.duration = duration

    def collect_samples(self):
        # This method should collect samples from the HackRF device
        # Placeholder for actual HackRF sample collection
        return np.random.randn(self.sample_rate * self.duration) + 1j * np.random.randn(self.sample_rate * self.duration)

def save_sigmf(data, meta_filename, data_filename):
    with open(meta_filename, 'w') as f:
        json.dump(data, f)
    with open(data_filename, 'wb') as f:
        f.write(np.float32(np.real(samples)).tobytes())
        f.write(np.float32(np.imag(samples)).tobytes())

def plot_stft(samples, sample_rate):
    f, t, Zxx = stft(samples, fs=sample_rate, nperseg=1024)
    plt.pcolormesh(t, f, np.abs(Zxx), shading='gouraud')
    plt.title('STFT Magnitude')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

# Configuration
sample_rate = 20e6  # 20 MS/s
center_freq = 2.437e9  # WiFi Channel 6
duration_per_file = 1  # seconds
total_duration = 5  # seconds

# Main collection and analysis loop
for i in range(total_duration):
    hackrf = HackRF(sample_rate, center_freq, duration_per_file)
    samples = hackrf.collect_samples()

    # Save samples in SigMF format
    metadata = {
        "global": {
            "core:datatype": "cf32_le",
            "core:sample_rate": sample_rate,
            "core:version": "0.0.1",
            "core:description": "WiFi signal collection",
            "core:frequency": center_freq,
        },
        "captures": [
            {"core:time": "PLACEHOLDER_FOR_UNIX_EPOCH_TIMESTAMP", "core:frequency": center_freq}
        ]
    }
    save_sigmf(metadata, f"wifi_capture_{i}.sigmf-meta", f"wifi_capture_{i}.sigmf-data")

    # Plot STFT for this segment
    plot_stft(samples, sample_rate)

