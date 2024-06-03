// tngl/backends/hackrf_sweep_invoker.c
#include <stdio.h>
#include <stdlib.h>

void invoke_hackrf_sweep(const char *serial, int amp_enable, const char *freq_range,
                         int antenna_enable, int lna_gain, int vga_gain, int bin_width,
                         int one_shot, int num_sweeps, int binary_output, int inverse_fft_output,
                         const char *output_file) {
    char command[1024];
    snprintf(command, sizeof(command),
             "hackrf_sweep -d %s -a %d -f %s -p %d -l %d -g %d -w %d %s -N %d %s %s -r %s",
             serial, amp_enable, freq_range, antenna_enable, lna_gain, vga_gain, bin_width,
             one_shot ? "-1" : "", num_sweeps, binary_output ? "-B" : "",
             inverse_fft_output ? "-I" : "", output_file);

    printf("Executing command: %s\n", command);
    system(command);
}