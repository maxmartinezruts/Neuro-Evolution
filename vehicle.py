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
        self.pos = np.array([0.0,0.0])
        self.vel = np.array([0.0,0.0])
        self.acc = np.random.uniform(-1,1,2)/30
        self.postrack = []
        self.veltrack = []
        self.acctrack = []
        self.score = 0
        self.fitness = 0
        self.brain = nn.Brain(model)

    def update(self):
        if -width/2 < self.pos[0] < width/2:
            input = np.asarray([[self.pos[0], self.vel[0], self.acc[0]]])
            output = self.brain.model.predict(input, 1)[0]
            self.jou = np.array([output[0]-0.5,0])
            self.acc += self.jou
            self.acc += np.random.uniform(-1,1,2)/20
            self.acc[1] = 0
            self.vel += self.acc
            self.pos += self.vel
            self.score += math.e**(-(self.pos[0]/(width/2))**2)

        self.postrack.append(self.pos[0])
        self.veltrack.append(self.vel[0])
        self.acctrack.append(self.acc[0])

    def reset(self):
        self.pos = np.array([0.0, 0.0])
        self.vel = np.array([0.0, 0.0])
        self.acc = np.random.uniform(-1, 1, 2) / 30
        self.postrack = []
        self.postrack = []
        self.veltrack = []
        self.acctrack = []
        self.score = 0
        self.fitness = 0