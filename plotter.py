# Author:   Max Martinez Ruts
# Creation: 2019

import matplotlib.pyplot as plt
import numpy as np

histograms = []
medians = []
means = []
mins = []
maxs = []

def save(scores, generation, tmax, population_size):
    histograms.append(scores)
    medians.append(np.median(scores))
    means.append(np.mean(scores))
    maxs.append(np.max(scores))
    mins.append(np.min(scores))
    fig = plt.figure()
    plt.plot(np.arange(0, generation), means, label='Mean')
    plt.plot(np.arange(0, generation), medians, label='Median')
    plt.plot(np.arange(0, generation), mins, label='Min')
    plt.plot(np.arange(0, generation), maxs, label='Max')
    plt.legend(loc='upper left')
    plt.xlabel('Generation [-]')
    plt.ylabel('Score [-]')
    fig.savefig('progression/___progress_' + str(generation) + '.png')

    fig = plt.figure()
    plt.hist(histograms[-1], bins=np.linspace(0, tmax ** 1.3, 40))
    plt.xlim(0, tmax ** 1.3)
    plt.ylim(0, population_size)
    plt.xlabel('Score [-]')
    plt.ylabel('Frequence [-]')
    plt.title('Generation ' + str(generation))
    fig.savefig('histograms/___histogram_' + str(generation) + '.png')
    print('------------')
    print(np.median(scores), np.mean(scores))
