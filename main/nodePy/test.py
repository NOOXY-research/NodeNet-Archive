import NeuralNetwork as NN
import numpy as np
MyNN = NN.NeuralNetwork(4, [2, 3, 5, 2])
Data = np.random.randn(10, 2)
print(MyNN)
