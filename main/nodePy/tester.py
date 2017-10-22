import node.NeuralNetwork as NN
import numpy as np
MyNN = NN.NeuralNetwork(3, [2, 4, 2], Name = 'test')
InputData = np.array(([0, 0],[1, 1]), dtype = float)
OutputData = np.array(([0, 0],[1, 1]), dtype = float)
NN.Train.trainbyBatch(MyNN, InputData, OutputData, Speed = 10, Verbose = 2)
print(MyNN)
MyNN.savetoFile()
