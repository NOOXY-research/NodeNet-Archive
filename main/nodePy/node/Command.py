# Command.py for packaged command. And for later assemble use.
import numpy as np
import node.NeuralNetwork as NN

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
    return nn
# Load latest Neural Network not saved and return it
