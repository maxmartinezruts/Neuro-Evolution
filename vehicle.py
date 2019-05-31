# Author:   Max Martinez Ruts
# Creation: 2019

import numpy as np
import math
import neural_network as nn

# Screen parameters
width = 800
height = 800

class Vehicle:
    def __init__(self, model=0):

        # Initialize dynamics
        self.pos = np.array([0.0,0.0])
        self.vel = np.array([0.0,0.0])
        self.acc = np.random.uniform(-1,1,2)/30

        # Helpers for tracking dynamics
        self.postrack = []
        self.veltrack = []
        self.acctrack = []

        # Initialize scores
        self.score = 0
        self.fitness = 0

        # Generate ANN
        self.brain = nn.Brain(model)

    def update(self):

        # If vehicle is within the bounds of the screen:
        if -width/2 < self.pos[0] < width/2:

            # Input is vehicle dynamics (pos, vel, acc)
            input = np.asarray([[self.pos[0], self.vel[0], self.acc[0]]])

            # Output is predicted jerk
            output = self.brain.model.predict(input, 1)[0]

            # Map jerk from 0,1 to -0.5,0.5
            self.jou = np.array([output[0]-0.5,0])

            # apply disturbance
            self.acc += np.random.uniform(-1,1,2)/20

            # Apply dynamics
            self.acc += self.jou
            self.acc[1] = 0
            self.vel += self.acc
            self.pos += self.vel

            # Add score contribution
            self.score += math.e**(-(self.pos[0]/(width/2))**2)

        self.postrack.append(self.pos[0])
        self.veltrack.append(self.vel[0])
        self.acctrack.append(self.acc[0])

    def reset(self):

        # Reset parameters (needed to recycle vehicles during different generations)
        self.pos = np.array([0.0, 0.0])
        self.vel = np.array([0.0, 0.0])
        self.acc = np.random.uniform(-1, 1, 2) / 30
        self.postrack = []
        self.postrack = []
        self.veltrack = []
        self.acctrack = []
        self.score = 0
        self.fitness = 0