# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 01:40:02 2020

@author: sidhant
"""
# Question number 4:  3 layer neural network for XOR 

import numpy as np
np.random.seed(0)

def sigmoid(x): # Returns values that sums to one.
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(sx):
    
    return sx * (1 - sx)

# Cost functions.
def cost(predicted, truth):
    return truth - predicted

xor_input = np.array([[0,0], [0,1], [1,0], [1,1]])
xor_output = np.array([[0,1,1,0]]).T

X = xor_input
Y = xor_output


num_data, input_dim = X.shape

# dimensions for the intermediate layer.
hidden_dim1 = 8
hidden_dim2 = 5

# Define the shape of the output vector. 
output_dim = len(Y.T)

# weight initialization.
W1 = np.random.random((input_dim, hidden_dim1))
W2 = np.random.random((hidden_dim1,hidden_dim2))
W3 = np.random.random((hidden_dim2,output_dim))


num_epochs = 50000
learning_rate = 0.08

for epoch_n in range(num_epochs):
    print("Epoch: ",epoch_n)
    layer0 = X
    # Forward propagation.
    
    layer1 = sigmoid(np.dot(layer0, W1))
    layer2 = sigmoid(np.dot(layer1, W2))
    layer3 = sigmoid(np.dot(layer2, W3))

    # Back propagation 
    layer3_error = cost(layer3, Y)    
    layer3_delta = layer3_error * sigmoid_derivative(layer3)    
    
    layer2_error = np.dot(layer3_delta, W3.T)
    layer2_delta = layer2_error*sigmoid_derivative(layer2)
    
    layer1_error = np.dot(layer2_delta, W2.T)
    layer1_delta = layer1_error*sigmoid_derivative(layer1)
    
    # update weights
    W3 += learning_rate * np.dot(layer2.T, layer3_delta)
    W2 +=  learning_rate * np.dot(layer1.T, layer2_delta)
    W1 +=  learning_rate * np.dot(layer0.T, layer1_delta)
    
print("Input:\n",X)
print("Expected output:\n",Y) 

print("actual output:\n",layer3)  