# NeuralNetwork.py provide stuff related to neural network.
# Author: magneticchen
# note:
# For normal variable use lower case
# For matrix variable use all upper case
# The meaning of 'error' is equivalent to 'cost'
# Operator 'X' for matrix dot multiplication, '*' for matrix elements multiplication. In annotation.
import numpy as np
# Matrix
import node.NeuralNetwork.Function as f
# Activation function etc.
import node.IO as IO
# File related function

class DFF(object):
# Classical NeuralNetwork object
    def __init__(self, LayersCount = 1, LayerNeuronsCount = [1], Name = 'Unamed_Neural_Network'):
        self.LayersCount = LayersCount
        self.LayerNeuronsCount = LayerNeuronsCount
        self.Weight = []
        self.Bias = []
        self.Name = Name
        # Initialize some general variable for NN
        for x in range(0, self.LayersCount-1):
            self.Weight.append(np.random.randn(self.LayerNeuronsCount[x], self.LayerNeuronsCount[x+1]))
            self.Bias.append(np.random.randn(1, self.LayerNeuronsCount[x+1]))
    # Initlalize NN structure

    def __str__(self):
        s = 'An '+self.Name+'@NeuralNetwork object\nDetail:\n\n'
        for layer in range(0, self.LayersCount-1):
            s = s+'*** layer'+str(layer)+' ('+str(self.LayerNeuronsCount[layer])+' Neurons) ***\n'
            s = s+'>>>layer'+str(layer)+' to layer'+str(layer+1)+' Weight\n'
            s = s+str(self.Weight[layer])+'\n'
            s = s+'>>>layer'+str(layer)+' to layer'+str(layer+1)+' Bias\n'
            s = s+str(self.Bias[layer])+'\n\n'
        # Print its layer by layer one by one
        s = s+'*** layer'+str(self.LayersCount)+' ('+str(self.LayerNeuronsCount[self.LayersCount-1])+' Neurons) ***\n'
        # Last layer
        return s
    # Print detail info for Neural Network

    def feed(self, InputData):
        A = f.sigmoid(InputData)
        for layer in range(0, self.LayersCount-1):
            W = np.dot(A, self.Weight[layer])
            B = np.dot(np.ones((InputData.shape[0],1)), self.Bias[layer])
            A = f.sigmoid(W+B)
        return f.logit(A)
        # Variable explianation
        # A: ActivationFunction(BacksideSum)
        # W: A X Weight
        # B: Ones(InputDataAmount, 1) X Bias
        # BacksideSum = W + B or InputData
    # Feed data forward

    def loadfromFile(self, Filename):
        try:
            MyRAWReader = IO.RAWReader()
            MyRAWReader.open(Filename+'.node')
            self.Name = Filename;
            self.LayersCount = int(MyRAWReader.pop())
            self.LayerNeuronsCount = []
            self.Weight = []
            self.Bias = []
            # Get the LayersCount first and Initlalize LayerNeuronsCount, Weight and Bias
            for layer in range(0, self.LayersCount):
                self.LayerNeuronsCount.append(int(MyRAWReader.pop()))
            # Get each layer's neurons count one by one
            for layer in range(0, self.LayersCount-1):
                self.Weight.append(IO.getAMatrix(MyRAWReader))
            # Get each layer's weight one by one
            for layer in range(0, self.LayersCount-1):
                self.Bias.append(IO.getAMatrix(MyRAWReader))
            # Get each layer's bias one by one
        except:
            print('warning: Loading '+Filename+'.node  error!')
        # Prevent file not exist
    # Load Neural Network from .node File

    def savetoFile(self, Filename = ''):
        if Filename == '':
            Filename = self.Name
        MyRAWWriter = IO.RAWWriter()
        MyRAWWriter.append(int(self.LayersCount))
        for layer in range(0, self.LayersCount):
            MyRAWWriter.append(int(self.LayerNeuronsCount[layer]))
        # Save each layer's neurons count one by one
        MyRAWWriter.newline()
        for layer in range(0, self.LayersCount-1):
            IO.writeAMatrix(self.Weight[layer], MyRAWWriter)
        # Save each layer's weight one by one
        for layer in range(0, self.LayersCount-1):
            IO.writeAMatrix(self.Bias[layer], MyRAWWriter)
        # Save each layer's bias one by one
        MyRAWWriter.write(Filename+'.node')
    # Save Neural Network to .node File
# Definition of Deep Feedforwrd NeuralNetwork
