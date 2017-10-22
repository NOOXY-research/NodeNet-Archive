# Command.py for packaged command. And for later assemble use.
import numpy as np
import node.NeuralNetwork as NN
import node.IO as IO
import math

def createNeuralNetwork():
    name = input('Input NeuralNetwork\'s name to be created.\n>>>')
    layerscount = int(input('Input "'+name+'" NeuralNetwork\'s layers count.\n>>>'))
    layerneuronscount = []
    for layer in range(0, layerscount):
        layerneuronscount.append(int(input('Input layer('+str(layer+1)+'\\'+str(layerscount)+')\'s neurons count.\n>>>')))
    nn = NN.NeuralNetwork(layerscount, layerneuronscount, name)
    nn.savetoFile()
    return nn
# Create Neural Network and return it

def loadNeuralNetwork():
    name = input('Input NeuralNetwork\'s name to be loaded.\n>>>')
    nn = NN.NeuralNetwork()
    nn.loadfromFile(name)
    return nn
# Load Neural Network and return it

def recoverNeuralNetwork():
    name = input('Input NeuralNetwork\'s name to be recovered.\n>>>')
    nn = NN.NeuralNetwork()
    nn.loadfromFile(name+'_latest')
    nn.Name = name
    return nn
# Load latest Neural Network not saved and return it

def printMatrix():
    name = input('Input matrix\'s name to be recovered. (Read from ".mtrx" file)\n>>>')
    raw = IO.RAWReader()
    raw.open(name+'.mtrx')
    matrix = IO.getAMatrix(raw)
    np.set_printoptions(threshold=np.nan)
    print(matrix)
# Print specify matrix file

def trainNeuralNetwork(MyNeuralNetwork):
    print('Input "min error value per data(0.1)", "speed(0.01)" , "max training times (-1 for infinite)", "times per loop(100)".')
    rawinput = input('>>>')
    rawinput = rawinput.split()
    print(rawinput)
    error = float(rawinput[0])
    speed = float(rawinput[1])
    times = int(rawinput[2])
    loop = int(rawinput[3])
    rawreader = IO.RAWReader()
    rawreader.open('in.mtrx')
    InputData = IO.getAMatrix(rawreader)
    rawreader.open('out.mtrx')
    OutputData = IO.getAMatrix(rawreader)
    # Get Input/OutputData to matrix
    errorfinal = math.sqrt(math.pow(error, 2)*len(InputData))
    # Translate error per data(row) to whole error
    print('Final error:'+str(errorfinal))
    NN.Train.trainbyBatch(MyNeuralNetwork, InputData, OutputData, errorfinal, times, speed, VerbosePerLoop=loop, Verbose=2)
    MyNeuralNetwork.savetoFile()
    print('Saved to "'+MyNeuralNetwork.Name+'.node".')
# Train neural network with specify parameters

def trainNeuralNetworkbyDefault(MyNeuralNetwork):
    print('Input "min error value per data(0.1)".')
    rawinput = input('>>>')
    rawinput = rawinput.split()
    error = float(rawinput[0])
    rawreader = IO.RAWReader()
    rawreader.open('in.mtrx')
    InputData = IO.getAMatrix(rawreader)
    rawreader.open('out.mtrx')
    OutputData = IO.getAMatrix(rawreader)
    # Get Input/OutputData to matrix
    errorfinal = math.sqrt(math.pow(error, 2)*len(InputData))
    # Translate error per data(row) to whole error
    print('Final error:'+str(errorfinal))
    NN.Train.trainbyBatch(MyNeuralNetwork, InputData, OutputData, errorfinal, Verbose=2)
    MyNeuralNetwork.savetoFile()
    print('Saved to "'+MyNeuralNetwork.Name+'.node".')
# Train neural network with default parameters

def trainNeuralNetworkRandomly(MyNeuralNetwork):
    pass

def feedNeuralNetwork(MyNeuralNetwork):
    pass

def feedNeuralNetworkbymtrx(MyNeuralNetwork):
    pass

def feedNeuralNetworkbyTestmtrx(MyNeuralNetwork):
    pass

def remapNeuralNetwork(MyNeuralNetwork):
    pass

def saveNeuralNetwork(MyNeuralNetwork):
    pass

def printNeuralNetwork(MyNeuralNetwork):
    pass
