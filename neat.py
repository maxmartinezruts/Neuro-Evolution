import tensorflow as tf
import matplotlib.pyplot as plt

import numpy as np
import pygame
import time
import math

# Convert coordinates form cartesian to screen coordinates (used to draw in pygame screen)
def cartesian_to_screen(car_pos):
    factor = 1
    screen_pos = np.array([center[0]*factor+car_pos[0],center[1]*factor-car_pos[1]])/factor
    screen_pos = screen_pos.astype(int)
    return screen_pos
class Brain:
    def __init__(self, model):
        if model==0:
            self.model =  tf.keras.models.clone_model(model_base)

        else:
            self.model = tf.keras.models.clone_model(model, input_tensors=None)



    def mutate(self, weights):
        w1 = np.random.randn(3,6)
        r = np.random.rand(3,6)
        w1 = np.where(r>0.9,w1,0)

        b1 = np.random.randn(6)
        r = np.random.rand(6)
        b1 = np.where(r> 0.9, b1, 0)

        w2 = np.random.randn(6,1)
        r = np.random.rand(6, 1)
        w2 = np.where(r > 0.9, w2, 0)

        b2 = np.random.randn(1)/2
        r = np.random.rand(1)
        b2 = np.where(r > 0.9, b2, 0)
        weights[0] += w1
        weights[1] += b1
        weights[2] += w2
        weights[3] += b2
        self.model.set_weights(weights)
        return weights


class Vehicle:
    def __init__(self, model=0):
        self.pos = np.array([0.0,0.0])
        self.vel = np.array([0.0,0.0])
        self.acc = np.random.uniform(-1,1,2)/30
        self.score = 0
        self.fitness = 0
        self.brain = Brain(model)


    def update(self):
        if -width/2 < self.pos[0] < width/2:
            input = np.asarray([[self.pos[0], self.vel[0], self.acc[0]]])
            output = self.brain.model.predict(input, 1)[0]
            print(output)
            self.acc += np.array([output[0]-0.5,0])
            self.score += math.e**(-(self.pos[0]/(width/2))**2)
            self.acc += np.random.uniform(-1,1,2)/20
            self.acc[1] = 0
            self.vel += self.acc
            self.pos += self.vel



population_size = 100
vehicles = []
last_vehicles =[]
counter = 0
histograms = []
medians = []
means = []
mins = []
maxs = []

model_base = tf.keras.models.Sequential()
input_layer = tf.keras.layers.Flatten()
hidden_layer = tf.keras.layers.Dense(units=6, input_shape=[3], activation='sigmoid')
output_layer = tf.keras.layers.Dense(units=1, input_shape=[6], activation='sigmoid')
model_base.add(input_layer)
model_base.add(hidden_layer)
model_base.add(output_layer)
input = np.asarray([[0.0, 0.0, 0.0]])
start = time.time()
model_base.predict(input, verbose=0)

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

fpsClock = pygame.time.Clock()

for n in range(population_size):
    vehicles.append(Vehicle())
time.sleep(1)
fps = 400
tmax = 500

print(time.time() - start)
for generation in range(1,50):
    t = 0

    # Game loop
    while t<tmax:

        t+=1
        pygame.event.get()

        screen.fill((0, 0, 0))
        # Draw screen
        for vehicle in vehicles:
            vehicle.update()
            pygame.draw.circle(screen, (min(30 +int(vehicle.score),255), 0, 0), cartesian_to_screen(vehicle.pos), 10)

        pygame.display.flip()
        fpsClock.tick(fps)

    collective_score = 0
    scores = []
    for vehicle in vehicles:
        vehicle.score = vehicle.score**1.3
        collective_score += vehicle.score
        scores.append(vehicle.score)
    histograms.append(scores)
    medians.append(np.median(scores))
    means.append(np.mean(scores))
    maxs.append(np.max(scores))
    mins.append(np.min(scores))
    fig = plt.figure()
    plt.plot(np.arange(0,generation),means, label='Mean')
    plt.plot(np.arange(0,generation),medians, label='Median')
    plt.plot(np.arange(0,generation),mins, label='Min')
    plt.plot(np.arange(0,generation),maxs, label='Max')
    plt.legend(loc='upper left')
    plt.xlabel('Generation [-]')
    plt.ylabel('Score [-]')
    fig.savefig('progression/___progress_'  + str(generation)+'.png')

    # plt.show()
    fig = plt.figure()
    plt.hist(histograms[-1],  bins=np.linspace(0,tmax**1.3,40))
    plt.xlim(0,tmax**1.3)
    plt.ylim(0,population_size)
    plt.xlabel('Score [-]')
    plt.ylabel('Frequence [-]')
    plt.title('Generation ' + str(generation))
    fig.savefig('histograms/___histogram_'  + str(generation)+'.png')

    # plt.show()
    median_score = np.median(scores)
    for vehicle in vehicles:
        vehicle.fitness = vehicle.score/collective_score
    new_weights = []

    print('------------')
    print(collective_score, median_score, np.mean(scores))
    for vehicle in vehicles:
        index = 0
        r = np.random.uniform(0,1)
        while r > 0:
            r-=vehicles[index].fitness
            index +=1
        index -=1
        # print(vehicles[index].brain.model.get_weights[0])
        new_weights.append(vehicles[index].brain.model.get_weights())

        

    for v in range(len(vehicles)):
        child = vehicles[v]
        child.pos = np.array([0.0, 0.0])
        child.vel = np.array([0.0, 0.0])
        child.acc = np.random.uniform(-1, 1, 2) / 30
        child.score = 0
        child.fitness = 0
        weights =
        child.brain.mutate(new_weights[v])
        vehicles[v] = child

# Close simulation
pygame.quit()

