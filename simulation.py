# Author:   Max Martinez Ruts
# Creation: 2019

import pygame
import numpy as np

# Screen parameters
width = 800
height = 800
center = np.array([width/2, height/2])
screen = pygame.display.set_mode((width, height))

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255,255, 0)

# Limit performance
fpsClock = pygame.time.Clock()
fps = 400

# Convert coordinates form cartesian to screen coordinates (used to draw in pygame screen)
def cartesian_to_screen(car_pos):
    factor = 1
    screen_pos = np.array([center[0]*factor+car_pos[0],center[1]*factor-car_pos[1]])/factor
    screen_pos = screen_pos.astype(int)
    return screen_pos

# Simulation loop
def simulate(vehicles, tmax):

    # Initialize clock
    t= 0

    while t < tmax:
        t += 1

        # Reset to black screen
        pygame.event.get()
        screen.fill((0, 0, 0))

        # Draw screen
        for vehicle in vehicles:
            # update vehicle position, velocity, acceleration and jerk
            vehicle.update()

            # Draw vehicle in screen
            pygame.draw.circle(screen, (min(30 +int(vehicle.score),255), 0, 0), cartesian_to_screen(vehicle.pos), 10)

        # Display screen
        pygame.display.flip()
        fpsClock.tick(fps)