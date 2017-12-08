# nodenet/learningalgorithm/backpropagations.py
# Description:
# "backpropagations.py" provide backpropagation type of training.
# Copyright 2018 NOOXY. All Rights Reserved.

import numpy as np

# Vanilla BackPropagation
def vanilla(gradient, configuration, cache):
    # Load learning configuration
    learning_rate = configuration['learning_rate']
    return -learning_rate*gradient

# BackPropagation with vanilla momentum
def vanilla_momentum(gradient, configuration, cache):
    # Load learning configuration
    learning_rate = configuration['learning_rate']
    momentum_rate = configuration['momentum_rate']
    momentum = None
    # Recover variables from cache
    if type(cache) != NoneType:
        momentum = cache[0]
    else:
        momentum = np.zeros(gradient.shape)
    newgrandient = -learning_rate*gradient+momentum_rate*momentum
    return newgrandient, [newgrandient]

# BackPropagation with nesterov momentum
def nesterov_momentum(gradient, configuration, cache):
    # Load learning configuration
    learning_rate = configuration['learning_rate']
    momentum_rate = configuration['momentum_rate']
    momentum = None
    # Recover variables from cache
    if type(cache) != NoneType:
        momentum = cache[0]
        newgrandient = -learning_rate*gradient+momentum_rate*momentum
    else:
        momentum = np.zeros(gradient.shape)
        newgrandient = np.zeros(gradient.shape)
    newmomentum = -learning_rate*gradient+momentum_rate*momentum
    return newgrandient, [newmomentum]

# AdaGrad BackPropagation
def adagrad(gradient, configuration, cache):
    # Load learning configuration
    learning_rate = configuration['learning_rate']
    epsilon = configuration['epsilon']
    squaresum = None
    # Recover variables from cache
    if type(cache) != NoneType:
        squaresum = cache[0]
    else:
        squaresum = np.zeros(gradient.shape)
    squaresum += np.power(gradient, 2)
    newgrandient = -learning_rate*gradient/(np.sqrt(squaresum)+epsilon)
    return newgrandient, [squaresum]

# AdaDelta BackPropagation
def adadelta(gradient, configuration, cache):
    # Load learning configuration
    epsilon = configuration['epsilon']
    decay_rate = configuration['decay_rate']
    squaresumdelta = None
    squaresumgradient = None
    # Recover variables from cache
    if type(cache) != NoneType:
        squaresumdelta = cache[0]
        squaresumgradient = cache[1]
    else:
        squaresumdelta = np.zeros(gradient.shape)
        squaresumgradient = np.zeros(gradient.shape)
    squaresumgradient = decay_rate*squaresumgradient + (1-decay_rate)*np.power(gradient, 2)
    newgrandient = -np.dot((np.sqrt(squaresumdelta)+epsilon)/(np.sqrt(squaresumgradient)+epsilon), gradient)
    squaresumdelta = decay_rate*squaresumdelta + (1-decay_rate)*np.power(newgrandient, 2)
    return newgrandient, [squaresumdelta, squaresumgradient]

# RMSprop BackPropagation
def rmsprop(gradient, configuration, cache):
    # Load learning configuration
    learning_rate = configuration['learning_rate']
    epsilon = configuration['epsilon']
    decay_rate = configuration['decay_rate']
    squaresum = None
    # Recover variables from cache
    if type(cache) != NoneType:
        squaresum = cache[0]
    else:
        squaresum = np.zeros(gradient.shape)
    squaresum += decay_rate*squaresum + (1-decay_rate)*np.power(gradient, 2)
    newgrandient = -learning_rate*gradient/(np.sqrt(squaresum)+epsilon)
    return newgrandient, [squaresum]

# Adam BackPropagation
def adam(gradient, configuration, cache):
    # Load learning configuration
    learning_rate = configuration['learning_rate']
    epsilon = configuration['epsilon']
    beta1 = configuration['beta1']
    beta2 = configuration['beta2']
    grandientm = None
    grandientv = None
    # Recover variables from cache
    if type(cache) != NoneType:
        grandientm = cache[0]
        grandientv = cache[1]
        t = cache[2]
    else:
        grandientm = np.zeros(gradient.shape)
        grandientv = np.zeros(gradient.shape)
        t = 1
    grandientm = beta1*grandientm + (1-beta1)*grandient
    grandientv = beta2*grandientv + (1-beta2)*np.power(gradient, 2)
    grandientm_delta = grandientm/(1-beta1**t)
    grandientv_delta = grandientv/(1-beta2**t)
    newgrandient = -learning_rate*grandientm_delta/(np.sqrt(grandientv_delta)+epsilon)
    return newgrandient, [grandientm, grandientv, t]
