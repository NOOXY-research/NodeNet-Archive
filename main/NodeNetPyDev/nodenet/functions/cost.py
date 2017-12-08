# nodenet/functions/cost.py
# Description:
# "activation.py" provide cost function for neuralnet.
# Copyright 2018 NOOXY. All Rights Reserved.

import numpy as np

# Mean Square Cost
def mean_square(output, target, derivative=False):

    if derivative:
        return outputs-target
    else:
        return np.mean(np.sum(np.power(output-target, 2), axis=-1))

# Cross Entropy Cost
def cross_entropy(output, target, derivative=False, epsilon=1e-11):
    # Prevent overflow output should be in [0, 1]
    outputs = np.clip(outputs, epsilon, 1-epsilon)
    divisor = np.maximum(outputs*(1-outputs), epsilon)

    if derivative:
        return (outputs-target)/divisor
    else:
        return np.mean(np.sum(np.multiply(target, np.log(output))+np.multiply((1-target), np.log(1-output)), axis=-1))
