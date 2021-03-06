# LearningAlgorithm.py provide stuff related to neural network.
# Author: magneticchen
# note:
# For normal variable use lower case
# For matrix variable use all upper case
# The meaning of 'error' is equivalent to 'cost'
# Operator 'X' for matrix dot multiplication, '*' for matrix elements multiplication. In annotation.
import math
# Sqrt
import numpy as np
# Matrix
import node.NeuralNetwork.Function as f
# Activation function etc.

def BackPropagation(MyNeuralNetwork, InputData, OutputData, speed = 0.1):
    # 'speed' is the training speed, which 'weight adjustment' = speed * djdw
    DJDW = []
    DELTA = []
    A = []
    Z = []
    # djdw = tangen of weight relative to cost(error), actually 'dj/dw'
    # delta = FrontsideError X DerivativeofActivationFunction(BacksideSum)
    # a = ActivationFunction(BacksideSum)
    # Z = BacksideSum
    Z.append(InputData)
    A.append(f.sigmoid(Z[-1]))
    for layer in range(0, MyNeuralNetwork.LayersCount-1):
        W = np.dot(A[-1], MyNeuralNetwork.Weight[layer])
        B = np.dot(np.ones((InputData.shape[0],1)), MyNeuralNetwork.Bias[layer])
        Z.append(W+B)
        A.append(f.sigmoid(Z[-1]))
        # For variable explianation go NeuralNetwork.feed()
    # Push data forward and collect all Z and A
    DELTA.insert(0, np.multiply(-(f.sigmoid(OutputData)-A[MyNeuralNetwork.LayersCount-1]), f.Derivativeofsigmoid(Z[MyNeuralNetwork.LayersCount-1])))
    for layer in range(MyNeuralNetwork.LayersCount-2, -1, -1):
        DJDW.insert(0, np.dot(np.transpose(A[layer]), DELTA[0]))
        # remark that DELTA[0] is always the latest one
        DELTA.insert(0, np.multiply(np.dot(DELTA[0], np.transpose(MyNeuralNetwork.Weight[layer])), f.Derivativeofsigmoid(Z[layer])))
        # Delta = Deltafront X transpose(ThisLayerWeight) * DerivativeofActivationFunction(ThisLayerBacksideSum)
        # For variable explianation go NeuralNetwork.feed()
    # Get all tangen of weight relative to cost(error)
    for layer in range(0, MyNeuralNetwork.LayersCount-1):
        MyNeuralNetwork.Weight[layer] = MyNeuralNetwork.Weight[layer]-speed*DJDW[layer]
        MyNeuralNetwork.Bias[layer] = MyNeuralNetwork.Bias[layer]-speed*np.dot(np.ones((1, InputData.shape[0])), DELTA[layer+1])
    # Add adjustment to each weight
    error = f.MeanSquareError(OutputData, Z[MyNeuralNetwork.LayersCount-1])
    return error
# A type of training is called BackPropagation for DFF
