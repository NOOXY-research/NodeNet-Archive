import node.NeuralNetwork as NN
import numpy as np
import node.IO as io
MyNN = NN.NeuralNetwork(5, [8, 8, 8, 8, 8], Name='nodePy')
RAWReader = io.RAWReader()
RAWReader.open('in.mtrx')
InputData = io.getAMatrix(RAWReader)
RAWReader.open('out.mtrx')
OutputData = io.getAMatrix(RAWReader)
# MyNN.loadfromFile('nodeC')
print(MyNN)
NN.Train.trainbyBatch(MyNN, InputData, OutputData, Speed = 0.01,Verbose = 2)
MyNN.savetoFile()
print(MyNN.feed(InputData))
