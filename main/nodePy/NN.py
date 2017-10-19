import numpy as np
import NN_function as f
# import some essential module and function
class NN(object):
    def __init__(self, LayersCount = 1, LayerNeuronsCount = [1]):
        self.LayersCount = LayersCount
        self.LayerNeuronsCount = LayerNeuronsCount
        self.Weight = []
        self.Bias = []
        #Initialize some general variable for NN
        for x in range(0, LayersCount-1):
            print(x)
            self.Weight.append(np.random.randn(self.LayerNeuronsCount[x], self.LayerNeuronsCount[x+1]))
            print(self.Weight[x])
        #initlalize NN structure

def trainbyBackPropagation():
