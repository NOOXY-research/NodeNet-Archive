import numpy as np
import NN_function as f
# import some essential modure and function
class NN(object):
    def __init__(self, inputLayerSize, outputLayerSize, hiddenLayerSize):
        #Initialize some general variable for NN
        self.inputLayerSize = inputLayerSize
        self.outputLayerSize = outputLayerSize
        self.hiddenLayerSize = hiddenLayerSize
