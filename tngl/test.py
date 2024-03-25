import unittest
import numpy as np
import os
import json
from your_module_name import HackRF, save_sigmf  # replace 'your_module_name' with the name of your Python file

class TestHackRF(unittest.TestCase):
    def setUp(self):
        self.sample_rate = 20e6
        self.center_freq = 2.437e9
        self.duration = 1
        self.hackrf = HackRF(self.sample_rate, self.center_freq, self.duration)
        self.samples = np.random.randn(self.sample_rate * self.duration) + 1j * np.random.randn(self.sample_rate * self.duration)

    def test_hackrf_initialization(self):
        self.assertEqual(self.hackrf.sample_rate, self.sample_rate)
        self.assertEqual(self.hackrf.center_freq, self.center_freq)
        self.assertEqual(self.hackrf.duration, self.duration)

    def test_save_sigmf(self):
        meta_filename = "test_meta.sigmf-meta"
        data_filename = "test_data.sigmf-data"
        metadata = {"test": "data"}
        
        save_sigmf(metadata, self.samples, meta_filename, data_filename)
        
        self.assertTrue(os.path.exists(meta_filename))
        self.assertTrue(os.path.exists(data_filename))
        
        with open(meta_filename, 'r') as f:
            loaded_meta = json.load(f)
            self.assertEqual(loaded_meta, metadata)
        
        os.remove(meta_filename)
        os.remove(data_filename)

if __name__ == '__main__':
    unittest.main()

