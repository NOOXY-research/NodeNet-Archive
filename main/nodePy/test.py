import NeuralNetwork as NN
import numpy as np
MyNN = NN.NeuralNetwork(4, [3, 5, 5, 2])
InputData = np.array(([1, 1, 1],[0, 0, 0]), dtype = float)
OutputData = np.array(([0, 0],[1, 1]), dtype = float)
# print(MyNN)
print(MyNN.feed(InputData))
for x in range(0, 10000):
    NN.train.BackPropagation(MyNN, InputData, OutputData, 0.1)
print(MyNN.feed(InputData))
