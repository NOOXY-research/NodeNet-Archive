# Command.py for packaged command. And for later assemble use.
import numpy as np
import node.NeuralNetwork.NeuralNetwork as NeuralNetwork
import node.IO as IO
import math
import subprocess as sp
import node.NeuralNetwork.TrainingType as TrainingType
import node.Graph as Graph
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
    nn = NeuralNetwork.DFF(layerscount, layerneuronscount, name)
    nn.savetoFile()
    IO.setValuetoConfigfile('setting.json', 'latestNN', nn.Name)
    return nn
# Create Neural Network and return it

def loadNeuralNetwork():
    name = input('Input NeuralNetwork\'s name to be loaded.\n>>>')
    nn = NeuralNetwork.DFF()
    nn.loadfromFile(name)
    IO.setValuetoConfigfile('setting.json', 'latestNN', nn.Name)
    return nn
# Load Neural Network and return it

def getLatestNeuralNetworkName():
    return IO.getValuefromConfigfile('setting.json', 'latestNN')
# Get latest neural network name

def loadLatestNeuralNetwork():
    name = IO.getValuefromConfigfile('setting.json', 'latestNN')
    nn = NeuralNetwork.DFF()
    if name != None:
        nn.loadfromFile(name)
    else:
        print('No latest NeuralNetwork')
    return nn
# Load latest Neural Network and return it

def recoverNeuralNetwork():
    name = input('Input NeuralNetwork\'s name to be recovered.\n>>>')
    nn = NeuralNetwork.DFF()
    nn.loadfromFile(name+'_backup')
    nn.Name = name
    IO.setValuetoConfigfile('setting.json', 'latestNN', nn.Name)
    return nn
# Load latest Neural Network not saved and return it

def printMatrix():
    name = input('Input matrix\'s name to be printed. (Read from ".mtrx" file)\n>>>')
    raw = IO.RAWReader()
    raw.open(name+'.mtrx')
    matrix = IO.getAMatrix(raw)
    IO.printprettyMatrix(matrix)
# Print specify matrix file

def trainNeuralNetwork(MyNeuralNetwork):
    print('Input "target error(0.1)", "speed(0.01)" , "max training times (-1 for infinite)"')
    rawinput = input('>>>')
    rawinput = rawinput.split()
    error = float(rawinput[0])
    speed = float(rawinput[1])
    times = int(rawinput[2])
    Datas = IO.getDatas()
    # Get Input/OutputData to matrix
    if IO.getValuefromConfigfile('setting.json', 'Verbose') != None:
        verbose = int(IO.getValuefromConfigfile('setting.json', 'Verbose'))
    else:
        verbose = VERBOSE_DEFAULT
    if IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times') != None:
        loop = int(IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times'))
    else:
        loop = VERBOSE_PER_LOOP_DEFAULT
    # Setting from config file
    TrainingType.trainbyBatch(MyNeuralNetwork, Datas, error, times, speed, VerbosePerLoop=loop, Verbose=verbose)
# Train neural network with specify parameters

def trainNeuralNetworkbyDefault(MyNeuralNetwork):
    print('Input "target error(0.1)".')
    rawinput = input('>>>')
    rawinput = rawinput.split()
    error = float(rawinput[0])
    Datas = IO.getDatas()
    # Get Input/OutputData to matrix
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
    TrainingType.trainbyBatch(MyNeuralNetwork, Datas, error, Speed=speed, VerbosePerLoop=loop, Verbose=verbose)
# Train neural network with default parameters

def trainNeuralNetworkRandomly(MyNeuralNetwork):
    print('Sorry the function\'s development not completed')
# Feed data randomly from  batch of data to train the neural network

def feedNeuralNetwork(MyNeuralNetwork):
    # string = input('input "row(number of data amount)", "column(number of input layer\'s neuron size)"\n')
    # string = string + ' ' + input('And then input "elements" row after row.\n')
    string= '1 '+str(MyNeuralNetwork.LayerNeuronsCount[0])+' '
    # Single set of data 1 * input size
    string = string+input('Input single data set.(split by space and press enter)\n')
    rawreader = IO.RAWReader()
    rawreader.openString(string)
    M = IO.getAMatrix(rawreader)
    IO.printprettyMatrix(MyNeuralNetwork.feed(M))
# Feed neural network by manually input.

def feedNeuralNetworkbymtrx(MyNeuralNetwork):
    name = input('Input .mtrx\'s file name.\n')
    rawreader = IO.RAWReader()
    rawreader.open(name+'.mtrx')
    M = IO.getAMatrix(rawreader)
    np.set_printoptions(threshold=np.nan)
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=False)
    IO.printprettyMatrix(MyNeuralNetwork.feed(M))
    pass
# Feed neural network from ".mtrx" file.

# def feedNeuralNetworkbyTestmtrx(MyNeuralNetwork):
#     pass
# # Feed neural network from "in_test.mtrx". And vertify it by "out_test.mtrx".

def remapNeuralNetwork(MyNeuralNetwork):
    MyNeuralNetwork = NeuralNetwork.DFF(MyNeuralNetwork.LayersCount, MyNeuralNetwork.LayerNeuronsCount, Name=MyNeuralNetwork.Name)
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

def ls():
    print('')
    print('ls:')
    sp.call('ls --color',shell=True)
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
    listConfigfileValues()
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

def printLogo():
    print('')
    try:
        sp.call('echo -e "\e[1m\e[31m88b 88  dP\'Yb   dP\'Yb  Yb  dP Yb  dP  TM\e[0m"',shell=True)
        sp.call('echo -e "\e[1m\e[34m88Yb88 dP   Yb dP   Yb  YbdP   YbdP\e[0m"',shell=True)
        sp.call('echo -e "\e[1m\e[32m88 Y88 Yb   dP Yb   dP  dPYb    88   \e[0m"',shell=True)
        sp.call('echo -e "\e[1m\e[33m88  Y8  YbodP   YbodP  dP  Yb   88  \e[39mProject node.\e[0m "',shell=True)
    except:
        print('88b 88  dP\'Yb   dP\'Yb  Yb  dP Yb  dP  TM')
        print('88Yb88 dP   Yb dP   Yb  YbdP   YbdP  ')
        print('88 Y88 Yb   dP Yb   dP  dPYb    88   ')
        print('88  Y8  YbodP   YbodP  dP  Yb   88  Project node. ')
    print('')
    print('Copyright(c)2017 NOOXY inc. Taiwan.')
    print('')
    print('Artificial neural network (ANN) manager. Python ver 0.0.0')
    print('For more information or update ->\'http://www.nooxy.tk\'.')
# Print LOGO

def idx2mtrx():
    FilenameIn = input('Input input IDX file name\n')
    FilenameOut = input('Input output mtrx filename.\n')
    IO.idx2mtrx(FilenameIn, FilenameOut)
# translator

def saveNeuralNetworkAs(MyNeuralNetwork):
    name = input('Input new neural network\'s name.\n')
    MyNeuralNetwork.savetoFile(name)
    print('Saved as "'+name+'.node".')

def plotNeuralNetwork(MyNeuralNetwork):
    xstart = float(input('Input start value of input.\n>>>'))
    xend = float(input('Input end value of input.\n>>>'))
    xlist = np.linspace(xstart, xend, num=1000)
    ylist = []
    for x in xlist:
        ylist.append(MyNeuralNetwork.feed(np.array(([x]), dtype=float))[0])
    Graph.plotByList(ylist, 'input', 'output', MyNeuralNetwork.Name+'\'s plotting', Xlist=xlist)
