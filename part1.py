import numpy as np
import matplotlib.pyplot as plt

N = 15
A = 3
X_MAX = 31

if __name__ == '__main__':
    # calculate the sequence of f(x) = a^x mod N for x = 1, 2, ..., (X_MAX - 1)
    # ignore x = 0 since it will always be 1 for any a and N
    seq = np.array([(A**x % N) for x in range(1, X_MAX)])

    # plot the sequence
    plt.xlabel('x')
    plt.ylabel(f"f(x) = {A}^x mod {N}")
    plt.plot(seq)
    plt.savefig(f'part1_{A}_{N}.png')

    # find the period of the sequence automatically
    print([i for i in range(X_MAX - 1) if seq[i] == seq[0]])