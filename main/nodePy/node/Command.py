# Command.py for packaged command. And for later assemble use.
import numpy as np
import node.NeuralNetwork as NN
import node.IO as IO
import math
import subprocess as sp
# For clearing the screen
VERBOSE_DEFAULT = 2
VERBOSE_PER_LOOP_DEFAULT = 10000
SPEED_DEFAULT = 0.1

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
    if IO.getValuefromConfigfile('setting.json', 'Verbose') != None:
        verbose = int(IO.getValuefromConfigfile('setting.json', 'Verbose'))
    else:
        verbose = VERBOSE_DEFAULT
    # Setting from config file
    NN.Train.trainbyBatch(MyNeuralNetwork, InputData, OutputData, errorfinal, times, speed, VerbosePerLoop=loop, Verbose=verbose)
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
    if IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times') != None:
        loop = int(IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times'))
    else:
        loop = VERBOSE_PER_LOOP_DEFAULT
    if IO.getValuefromConfigfile('setting.json', 'Verbose') != None:
        verbose = int(IO.getValuefromConfigfile('setting.json', 'Verbose'))
    else:
        verbose = VERBOSE_DEFAULT
    if IO.getValuefromConfigfile('setting.json', 'Training_Speed') != None:
        speed = float(IO.getValuefromConfigfile('setting.json', 'Training_Speed'))
    else:
        speed = SPEED_DEFAULT
    # Setting from config file
    NN.Train.trainbyBatch(MyNeuralNetwork, InputData, OutputData, errorfinal, Speed=speed, VerbosePerLoop=loop, Verbose=verbose)
    MyNeuralNetwork.savetoFile()
    print('Saved to "'+MyNeuralNetwork.Name+'.node".')
# Train neural network with default parameters

def trainNeuralNetworkRandomly(MyNeuralNetwork):
    pass
# Feed data randomly from  batch of data to train the neural network

def feedNeuralNetwork(MyNeuralNetwork):
    pass
# Feed neural network by manually input.

def feedNeuralNetworkbymtrx(MyNeuralNetwork):
    pass
# Feed neural network from ".mtrx" file.

def feedNeuralNetworkbyTestmtrx(MyNeuralNetwork):
    pass
# Feed neural network from "in_test.mtrx". And vertify it by "out_test.mtrx".

def remapNeuralNetwork(MyNeuralNetwork):
    MyNeuralNetwork = NN.NeuralNetwork(MyNeuralNetwork.LayersCount, MyNeuralNetwork.LayerNeuronsCount, Name=MyNeuralNetwork.Name)
    # Use same parameters to create neural network
    print('Remaped "'+MyNeuralNetwork.Name+'" neural network successfully.')
    return MyNeuralNetwork
# Remap the weight of the neural network

def saveNeuralNetwork(MyNeuralNetwork):
    MyNeuralNetwork.savetoFile()
    print('Saved to "'+MyNeuralNetwork.Name+'.node".')
# Save the neural network

def printNeuralNetwork(MyNeuralNetwork):
    print(MyNeuralNetwork)
# Print detail of neural network

def clearScreen():
    sp.call('clear',shell=True)
# Just simply clear th screen

# Config List
ConfigDict = {
    'v': 'Verbose',
    'Verbose': 'Verbose',
    'n': 'Loop_per_N_times',
    's': 'Training_Speed',
}
# End of Config List

def setValuetoConfigfile():
    name = input('Name Code:\n')
    value = input('Value:\n')
    IO.setValuetoConfigfile('setting.json', ConfigDict[str(name)], value)
# Set Config

def listConfigfileValues():
    print('Config list:')
    print('[v] Verbose Level. -> '+str(IO.getValuefromConfigfile('setting.json', 'Verbose')))
    print('[n] Verbose per "N" times. -> '+str(IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times')))
    print('[s] Default training speed. -> '+str(IO.getValuefromConfigfile('setting.json', 'Training_Speed')))
# List Config
