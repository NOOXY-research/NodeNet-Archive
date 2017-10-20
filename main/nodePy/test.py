import NeuralNetwork as NN
import numpy as np
MyNN = NN.NeuralNetwork(4, [3, 5, 5, 2])
# InputData = np.array(([1, 1, 1],[0, 0, 0]), dtype = float)
# OutputData = np.array(([0, 0],[1, 1]), dtype = float)
# NN.Train.trainbyBatch(MyNN, InputData, OutputData, Verbose=1)
MyNN.loadfromFile('140')
print(MyNN)
MyNN.savetoFile('nodePy')
