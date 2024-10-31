import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

N = 15
A = 3
X_MAX = 1000

if __name__ == '__main__':
    # calculate the sequence of f(x) = a^x mod N for x = 0, 1, 2, ..., X_MAX
    seq = np.array([float(A**x % N) for x in range(X_MAX)])

    # remove "DC" component
    seq -= np.mean(seq)

    # calculate the discrete Fourier transform of the sequence and plot the magnitude
    freqs = fft.fftfreq(len(seq))
    power_spectrum = np.abs(fft.fft(seq)) ** 2

    plt.xlabel('Frequency')
    plt.ylabel("Power spectrum")

    # # plot all frequencies
    # plt.plot(freqs, power_spectrum, 'o-')
    
    # here, only plot positive frequencies since the power spectrums are all real numbers,
    # where the negative part will only be the mirror of the positive part
    plt.plot(freqs[:len(freqs)//2], power_spectrum[:len(power_spectrum)//2], 'o-')

    plt.savefig(f'part2_{A}_{N}_onlypos.png')