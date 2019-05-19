# Author:   Max Martinez Ruts
# Creation: 2019

import numpy as np

def next_generation(vehicles):
    p1s = []
    p2s = []
    for vehicle in vehicles:
        index = 0
        r = np.random.uniform(0,1)
        while r > 0:
            r-=vehicles[index].fitness
            index +=1
        index -=1
        p1s.append(vehicles[index].brain.model.get_weights())

        index = 0
        r = np.random.uniform(0, 1)
        while r > 0:
            r -= vehicles[index].fitness
            index += 1
        index -= 1
        p2s.append(vehicles[index].brain.model.get_weights())

    for v in range(len(vehicles)):
        child = vehicles[v]
        child.reset()
        child.brain.crossover(p1s[v],p2s[v])
        child.brain.mutate()
        child.brain.create()
        vehicles[v] = child