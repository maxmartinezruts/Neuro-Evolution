# Author:   Max Martinez Ruts
# Creation: 2019

import tensorflow as tf
import numpy as np

# Create model
model_base = tf.keras.models.Sequential()

# Add input, hidden and output layers
input_layer = tf.keras.layers.Flatten()
hidden_layer = tf.keras.layers.Dense(units=6, input_shape=[3], activation='sigmoid')
output_layer = tf.keras.layers.Dense(units=1, input_shape=[6], activation='sigmoid')

model_base.add(input_layer)
model_base.add(hidden_layer)
model_base.add(output_layer)

# Initialize template ANN
input = np.asarray([[0.0, 0.0, 0.0]])
model_base.predict(input, verbose=0)

# Class containing all information of a vehicle controller (ANN)
class Brain:
    def __init__(self, model):

        # If model not yet specified, create a new model
        if model==0:
            self.model =  tf.keras.models.clone_model(model_base)
            input = np.asarray([[0,0,0]])
            self.model.predict(input, 1)[0]

        # Otherwise use the passed model
        else:
            self.model = tf.keras.models.clone_model(model, input_tensors=None)

    # Execute crossover by mixing 2 genotypes
    def crossover(self, genes_1, genes_2):

        # Generate hybrid copies from progenitors
        weights_hidden = (genes_1[0]+genes_2[0])/2
        biases_hidden = (genes_1[1]+genes_2[1])/2
        weights_outputs = (genes_1[2]+genes_2[2])/2
        biases_outputs = (genes_1[3]+genes_2[3])/2

        # Set genotype
        self.weights = [weights_hidden, biases_hidden, weights_outputs, biases_outputs]

        # Update weights and biases
        self.model.set_weights(self.weights)

    def mutate(self):
        self.weights = self.model.get_weights()

        # Create random matrices and add only random values to elements in the matrix where value specified is greater than mutation rate
        # Mutation magnitude is set equal to random normal value
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

        # Add mutation matrices to existing genotype
        self.weights[0] += w1
        self.weights[1] += b1
        self.weights[2] += w2
        self.weights[3] += b2

        # Update weights and biases
        self.model.set_weights(self.weights)

    # Set weights and biases of ANN
    def create(self):
        self.model.set_weights(self.weights)
