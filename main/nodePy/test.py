import node.NeuralNetwork as NN
import numpy as np
MyNN = NN.NeuralNetwork()
InputData =
# OutputData = np.array(([0, 0],[1, 1]), dtype = float)
MyNN.loadfromFile('test')
# NN.Train.trainbyBatch(MyNN, InputData, OutputData, Verbose=1)
print(MyNN)
print(MyNN.feed(InputData))
