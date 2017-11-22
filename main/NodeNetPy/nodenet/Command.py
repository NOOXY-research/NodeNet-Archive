# Command.py for packaged command. And for later assemble use.
import numpy as np
import nodenet.NeuralNetwork.NeuralNetwork as NeuralNetwork
import nodenet.IO as IO
import math
import subprocess as sp
import nodenet.NeuralNetwork.TrainingType as TrainingType
import nodenet.Graph as Graph
import os
import nodenet.Parameter as p
# For clearing the screen

def initialize():
    if not os.path.exists(p.SAVED_PATH):
        os.makedirs(p.SAVED_PATH)
    if not os.path.exists(p.DATA_PATH):
        os.makedirs(p.DATA_PATH)

def haveinitailize():
    pass

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
    raw.open(p.DATA_PATH+name+'.mtrx')
    matrix = IO.getAMatrix(raw)
    IO.printprettyMatrix(matrix)
# Print specify matrix file
def clearScreen():
    sp.call('clear',shell=True)
# Just simply clear th screen

def list():
    print('')
    print('Saved NeuralNetwork:')
    sp.call('ls '+p.SAVED_PATH+' --color',shell=True)
# Just simply clear th screen

# Config List
ConfigDict = {
    'v': 'Verbose',
    'Verbose': 'Verbose',
    'n': 'Loop_per_N_times',
}
# End of Config List

def setValuetoConfigfile():
    listConfigfileValues()
    name = input('Name Code:\n>>>')
    value = input('Value:\n>>>')
    IO.setValuetoConfigfile('setting.json', ConfigDict[str(name)], value)
# Set Config

def listConfigfileValues():
    print('Config list:')
    print('[v] Verbose Level. -> '+str(IO.getValuefromConfigfile('setting.json', 'Verbose')))
    print('[n] Verbose per "N" times. -> '+str(IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times')))
# List Config

def printLogo():
    print('')
    try:
        sp.call('echo -e "\e[1m\e[31m88b 88  dP\'Yb   dP\'Yb  Yb  dP Yb  dP  TM\e[0m"',shell=True)
        sp.call('echo -e "\e[1m\e[34m88Yb88 dP   Yb dP   Yb  YbdP   YbdP\e[0m"',shell=True)
        sp.call('echo -e "\e[1m\e[32m88 Y88 Yb   dP Yb   dP  dPYb    88   \e[0m"',shell=True)
        sp.call('echo -e "\e[1m\e[33m88  Y8  YbodP   YbodP  dP  Yb   88  \e[39m NodeNet.\e[0m "',shell=True)
    except:
        print('88b 88  dP\'Yb   dP\'Yb  Yb  dP Yb  dP  TM')
        print('88Yb88 dP   Yb dP   Yb  YbdP   YbdP  ')
        print('88 Y88 Yb   dP Yb   dP  dPYb    88   ')
        print('88  Y8  YbodP   YbodP  dP  Yb   88   nodenet. ')
    print('')
    print('Copyright(c)2017 NOOXY inc. Taiwan.')
    print('')
    print('NodeNet (NeuralNetwork) manager. '+p.NODENETPY_VERSION)
    print('For more information or update ->\'http://www.nooxy.tk\'.')
# Print LOGO

def idx2mtrx():
    FilenameIn = input('Input input IDX file name\n')
    FilenameOut = input('Input output mtrx filename.\n')
    IO.idx2mtrx(FilenameIn, FilenameOut)
# translator
# ----------------------NeuralNetwork Start----------------------
def trainNeuralNetwork(MyNeuralNetwork):
    error = float(input('Input target error(0.1)\n>>>'))
    epochs = int(input('Input max epochs(-1)\n>>>'))
    print('Getting Datas...')
    Datas = IO.getDatas()
    if IO.getProfile(MyNeuralNetwork) == None:
        print('You must have training profile first!')
        editNeuralNetworkProfile(MyNeuralNetwork)
    Profile = IO.getProfile(MyNeuralNetwork)
    # Get Input/OutputData to matrix
    if IO.getValuefromConfigfile('setting.json', 'Verbose') != None:
        verbose = int(IO.getValuefromConfigfile('setting.json', 'Verbose'))
    else:
        verbose = p.VERBOSE_DEFAULT
    if IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times') != None:
        loop = int(IO.getValuefromConfigfile('setting.json', 'Loop_per_N_times'))
    else:
        loop = p.VERBOSE_PER_LOOP_DEFAULT
    # Setting from config file
    TrainingType.trainbyBatch(MyNeuralNetwork, Datas, error, epochs, Profile, verbose, loop)
# Train neural network with specify parameters

def printLearningAlgorithmDict():
    print('[0] BackPropagation')
    print('[1] Classical Momentum')
    print('[2] Nesterov Momentum')
    print('[3] AdaGrad')
    print('[4] ')
    print('[5] RMSprop')
    print('[6] Adam')

def editBackproprogation(MyNeuralNetwork):
    speed = float(input('Input speed value.\n>>>'))
    # targeterr = input('Input target error value.\n>>>')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'LearningAlgorithm', 'BackPropagation')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Speed', speed)
    # IO.setValuetoConfigfile(MyNeuralNetwork.Name+'_profile.json', 'Target_Error', targeterr)

def editClassicalMomentum(MyNeuralNetwork):
    speed = float(input('Input speed value.\n>>>'))
    momentumrate = float(input('Input momentum rate.\n>>>'))
    # targeterr = input('Input target error value.\n>>>')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'LearningAlgorithm', 'ClassicalMomentum')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Speed', speed)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Momentum_Rate', momentumrate)
    # IO.setValuetoConfigfile(MyNeuralNetwork.Name+'_profile.json', 'Target_Error', targeterr)

def editNesterovMomentum(MyNeuralNetwork):
    speed = float(input('Input speed value.\n>>>'))
    momentumrate = float(input('Input momentum rate.\n>>>'))
    # targeterr = input('Input target error value.\n>>>')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'LearningAlgorithm', 'NesterovMomentum')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Speed', speed)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Momentum_Rate', momentumrate)
    # IO.setValuetoConfigfile(MyNeuralNetwork.Name+'_profile.json', 'Target_Error', targeterr)

def editAdaGrad(MyNeuralNetwork):
    speed = float(input('Input speed value.\n>>>'))
    # targeterr = input('Input target error value.\n>>>')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'LearningAlgorithm', 'AdaGrad')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Speed', speed)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Epsilon', p.PROFILE_DEFAULT['Epsilon'])
    # IO.setValuetoConfigfile(MyNeuralNetwork.Name+'_profile.json', 'Target_Error', targeterr)

def editRMSprop(MyNeuralNetwork):
    speed = float(input('Input speed value('+str(p.PROFILE_DEFAULT['Speed'])+').\n>>>'))
    decayrate = float(input('Input decay rate('+str(p.PROFILE_DEFAULT['DecayRate'])+').\n>>>'))
    # targeterr = input('Input target error value.\n>>>')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'LearningAlgorithm', 'RMSprop')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Speed', speed)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'DecayRate', decayrate)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Epsilon', p.PROFILE_DEFAULT['Epsilon'])
    # IO.setValuetoConfigfile(MyNeuralNetwork.Name+'_profile.json', 'Target_Error', targeterr)

def editAdam(MyNeuralNetwork):
    speed = float(input('Input speed value('+str(p.PROFILE_DEFAULT['Speed'])+').\n>>>'))
    beta1 = float(input('Input Beta1(decay rate)('+str(p.PROFILE_DEFAULT['Beta1'])+').\n>>>'))
    beta2 = float(input('Input Beta2(decay rate)('+str(p.PROFILE_DEFAULT['Beta2'])+').\n>>>'))
    # targeterr = input('Input target error value.\n>>>')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'LearningAlgorithm', 'Adam')
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Speed', speed)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Beta1', beta1)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Beta2', beta2)
    IO.setValuetoConfigfile(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json', 'Epsilon', p.PROFILE_DEFAULT['Epsilon'])
    # IO.setValuetoConfigfile(MyNeuralNetwork.Name+'_profile.json', 'Target_Error', targeterr)

editProfileDict = {
    '0' : editBackproprogation,
    '1' : editClassicalMomentum,
    '2' : editNesterovMomentum,
    '3' : editAdaGrad,
    '4' : editAdaGrad,
    '5' : editRMSprop,
    '6' : editAdam,
}

def editNeuralNetworkProfile(MyNeuralNetwork):
    print('You are editing "'+MyNeuralNetwork.Name+'" neuralnet\'s training profile.')
    try:
        os.remove(p.SAVED_PATH+MyNeuralNetwork.Name+'_profile.json')
    except:
        pass
    printLearningAlgorithmDict()
    LearningAlgorithmType = input('Select prefers LearningAlgorithm by index.\n>>>')
    editProfileDict[LearningAlgorithmType](MyNeuralNetwork)

def printNeuralNetworkProfile(MyNeuralNetwork):
    print(MyNeuralNetwork.Name+' neuralnet\'s training profile:')
    print(IO.getProfile(MyNeuralNetwork))

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
    rawreader.open(p.DATA_PATH+name+'.mtrx')
    M = IO.getAMatrix(rawreader)
    np.set_printoptions(threshold=np.nan)
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=False)
    IO.printprettyMatrix(MyNeuralNetwork.feed(M))
    pass
# Feed neural network from ".mtrx" file.

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
