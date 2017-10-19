import numpy as np
# import numpy mathematical python module
def sigmoid(z):
    return 1/(1+np.exp(-z))
# A type of activation function
