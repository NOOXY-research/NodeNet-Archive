import node.NeuralNetwork as NN
import numpy as np
import node.IO as IO
# MyNN = NN.NeuralNetwork(3, [2, 4, 2], Name = 'test')
# InputData = np.array(([0, 0],[1, 1]), dtype = float)
# OutputData = np.array(([0, 0],[1, 1]), dtype = float)
# NN.Train.trainbyBatch(MyNN, InputData, OutputData, Speed = 10, Verbose = 2)
# print(MyNN)
# MyNN.savetoFile()
# ANN test

IO.setValuetoConfigfile("test.json", "Number1", 3)
IO.setValuetoConfigfile("test.json", "Number2", 2)
IO.setValuetoConfigfile("test.json", "Number3", 1)
print(IO.getValuefromConfigfile("test.json", "Number1"))
print(IO.getValuefromConfigfile("test.json", "Number2"))
print(IO.getValuefromConfigfile("test.json", "Number3"))
# IO test