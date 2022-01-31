# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:36:57 2021

@author: Arif

Simple Perceptron of Quarantine Signals

Takes the MAgeneration Signals and obtains results. 
Run this at the end of the week?
Code Example By Arif Meighan,
Learnt from tutorial
https://www.youtube.com/watch?v=kft1AJ9WVDk&t=111s
Expanded for functionality with Indicators By Arif

TODO ERROR WITH USING MORE INPUTS AS EXAMPLE, WILL NEED TO TEST WHY
Probably something todo with formatting matrix's' within the code?


"""
import numpy as np
from MAgeneration import *



def sigmoid(x):
    return 1/(1*np.exp(-x))

def sigmoid_derivative(x):
    return x * (1-x)

def train():
    dataInput = np.array([[0,0,1], 
                          [1,1,1],
                          [1,0,1],
                          [0,1,1],])
    #Above are training inputs
    #below are training outputs, we .T to transpose it to a 4x1 matrix
    
    dataOutput = np.array([[0,1,1,0]]).T
    
    np.random.seed(1)
    
    synaptic_weights = 2 * np.random.random((3,1)) - 1
    
    
    for i in range(100000):
        input_layer = dataInput
        
        outputs = sigmoid(np.dot(input_layer,synaptic_weights))
        
        error = dataOutput - outputs
        
        adjustments = error * sigmoid_derivative(outputs)
        
        synaptic_weights += np.dot(input_layer.T,adjustments)
    return synaptic_weights


def think(inputs):
    """
    Pass inputs through the neural network to get output
    """
    synaptic_weights = train()
    inputs = inputs.astype(float)
    output = sigmoid(np.dot(inputs, synaptic_weights))
    return float(output[0])

def Prediction():
    signal1 = int(NeuralSignalMA())
    signal2 = int(NeuralSignalEMA())
    signal3 = int(NeuralSignalRiskGradient())
        
    out = think(np.array([signal1,signal2,signal3]))
    return out
    
print(Prediction())