# tngl/backends/hackrf.pyx
cdef extern void invoke_hackrf_sweep(const char *serial, int amp_enable, const char *freq_range,
                                     int antenna_enable, int lna_gain, int vga_gain, int bin_width,
                                     int one_shot, int num_sweeps, int binary_output, int inverse_fft_output,
                                     const char *output_file)

def run_hackrf_sweep(serial, amp_enable, freq_range, antenna_enable, lna_gain, vga_gain,
                     bin_width, one_shot, num_sweeps, binary_output, inverse_fft_output, output_file):
    invoke_hackrf_sweep(serial.encode('utf-8'), amp_enable, freq_range.encode('utf-8'), antenna_enable,
                        lna_gain, vga_gain, bin_width, one_shot, num_sweeps, binary_output,
                        inverse_fft_output, output_file.encode('utf-8'))
