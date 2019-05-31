# Author:   Max Martinez Ruts
# Creation: 2019

import numpy as np

# Pick a progenitor
def pick_progenitor(vehicles):
    index = 0
    r = np.random.uniform(0, 1)
    while r > 0:
        r -= vehicles[index].fitness
        index += 1
    index -= 1
    return index

# Create new generation of vehicles
def next_generation(vehicles):
    p1s = []
    p2s = []
    for vehicle in vehicles:


        # Select first progenitor
        p1s.append(vehicles[pick_progenitor(vehicles)].brain.model.get_weights())

        # Select second progenitor
        p2s.append(vehicles[pick_progenitor(vehicles)].brain.model.get_weights())

    for v in range(len(vehicles)):
        # Redefine vehicle to the new generated vehicle from its progenitors
        child = vehicles[v]
        child.reset()
        child.brain.crossover(p1s[v],p2s[v])
        child.brain.mutate()
        child.brain.create()
        vehicles[v] = child