# Author:   Max Martinez Ruts
# Creation: 2019

import pygame
import time
import genetic_algorithm as ga
import vehicle as vh
import simulation as sm
import plotter as pl

tmax = 500
population_size = 30
vehicles = []

# Create all vehicles
for n in range(population_size):
    vehicles.append(vh.Vehicle())
    vehicles[-1].brain.mutate()


for generation in range(1,100):

    # Simulation loop
    sm.simulate(vehicles, tmax)

    # Dramatize scores and determine total score of generation
    collective_score = 0
    scores = []
    for vehicle in vehicles:
        vehicle.score = vehicle.score**1.3
        collective_score += vehicle.score
        scores.append(vehicle.score)

    # Save histograms and progression over generations
    pl.save(scores, generation, tmax, population_size)

    # Determine fitness scores
    for vehicle in vehicles:
        vehicle.fitness = vehicle.score/collective_score

    # Create next generation
    ga.next_generation(vehicles)

# Close simulation
pygame.quit()

