# Function.py provide mathematical function for NeuralNetwork.py
import numpy as np
# import numpy mathematical python module

def sigmoid(Z):
    A = 1/(1+np.exp(-Z))
    where_are_NaNs = np.isnan(A)
    A[where_are_NaNs] = 0
    return A
def Derivativeofsigmoid(Z):
    A = np.exp(-Z)/np.power((1+np.exp(-Z)), 2)
    where_are_NaNs = np.isnan(A)
    A[where_are_NaNs] = 0
    return A
def logit(Z):
    A = np.log(Z/(1-Z))
    where_are_NaNs = np.isnan(A)
    return A
# A type of activation function
