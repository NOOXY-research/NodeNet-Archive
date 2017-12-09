# nodenet/learningalgorithm/defaultconfiguration.py
# Description:
# "defaultconfiguration.py" provide default parameters for each learnling algorithm.
# Copyright 2018 NOOXY. All Rights Reserved.

vanilla = {
    'learning_rate' : 0.01,
}

vanilla_momentum = {
    'learning_rate' : 0.01,
    'momentumrate' : 0.9,
}

nesterov_momentum = {
    'learning_rate' : 0.01,
    'momentumrate' : 0.9,
}

adagrad = {
    'learning_rate' : 0.01,
    'epsilon' : 10e-8,
}

adadelta = {
    'epsilon' : 10e-8,
    'decay_rate' : 0.9,
}

rmsprop = {
    'learning_rate' : 0.01,
    'epsilon' : 10e-8,
    'decay_rate' : 0.9,
}

adam = {
    'learning_rate' : 0.001,
    'epsilon' : 10e-8,
    'beta1' : 0.9,
    'beta2' : 0.999,
}
