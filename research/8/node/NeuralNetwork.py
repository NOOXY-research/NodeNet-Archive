# NeuralNetwork.py provide stuff related to neural network.
# Author: magneticchen
# note:
# For normal variable use lower case
# For matrix variable use all upper case
# The meaning of 'error' is equivalent to 'cost'
# Operator 'X' for matrix dot multiplication, '*' for matrix elements multiplication. In annotation.
import math
# Sqrt
import numpy as np
# Matrix
import node.Function as f
# Activation function etc.
import node.IO as IO
# File related function
import node.Graph as Graph
# Import some essential module and function

class NeuralNetwork(object):
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
            print('warning: Loading '+Filename+'.node error!')
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

class TrainTypes(object):
# TrainTypes collection
    def BackPropagation(MyNeuralNetwork, InputData, OutputData, speed = 0.1):
        # 'speed' is the training speed, which 'weight adjustment' = speed * djdw
        DJDW = []
        DELTA = []
        A = []
        Z = []
        # djdw = tangen of weight relative to cost(error), actually 'dj/dw'
        # delta = FrontsideError X DerivativeofActivationFunction(BacksideSum)
        # a = ActivationFunction(BacksideSum)
        # Z = BacksideSum
        Z.append(InputData)
        A.append(f.sigmoid(Z[-1]))
        for layer in range(0, MyNeuralNetwork.LayersCount-1):
            W = np.dot(A[-1], MyNeuralNetwork.Weight[layer])
            B = np.dot(np.ones((InputData.shape[0],1)), MyNeuralNetwork.Bias[layer])
            Z.append(W+B)
            A.append(f.sigmoid(Z[-1]))
            # For variable explianation go NeuralNetwork.feed()
        # Push data forward and collect all Z and A
        DELTA.insert(0, np.multiply(-(f.sigmoid(OutputData)-A[MyNeuralNetwork.LayersCount-1]), f.Derivativeofsigmoid(Z[MyNeuralNetwork.LayersCount-1])))
        for layer in range(MyNeuralNetwork.LayersCount-2, -1, -1):
            DJDW.insert(0, np.dot(np.transpose(A[layer]), DELTA[0]))
            # remark that DELTA[0] is always the latest one
            DELTA.insert(0, np.multiply(np.dot(DELTA[0], np.transpose(MyNeuralNetwork.Weight[layer])), f.Derivativeofsigmoid(Z[layer])))
            # Delta = Deltafront X transpose(ThisLayerWeight) * DerivativeofActivationFunction(ThisLayerBacksideSum)
            # For variable explianation go NeuralNetwork.feed()
        # Get all tangen of weight relative to cost(error)
        for layer in range(0, MyNeuralNetwork.LayersCount-1):
            MyNeuralNetwork.Weight[layer] = MyNeuralNetwork.Weight[layer]-speed*DJDW[layer]
            MyNeuralNetwork.Bias[layer] = MyNeuralNetwork.Bias[layer]-speed*np.dot(np.ones((1, InputData.shape[0])), DELTA[layer+1])
        # Add adjustment to each weight
        error = math.sqrt(np.sum((f.sigmoid(OutputData)-A[MyNeuralNetwork.LayersCount-1])**2))
        return error
    # A type of training is called BackPropagation

class Train(object):
# More advance training management
    def trainbyBatch(MyNeuralNetwork, InputData, OutputData, Error = 0.01, MaxTimes = -1, Speed = 0.1, MyTrainTypes = TrainTypes.BackPropagation, Verbose = 0, VerbosePerLoop = 10000, Backup = True):
        # Parameter explianation:
        # MyNeuralNetwork: Simply your NeuralNetwork
        # InputData/OutputData: Simply your data in numpy's matrix type
        # Error/MaxTimes: The training will stop until its error smaller then Error or reach it MaxTimes(max training times)
        # Speed: Same as the TrainTypes.BackPropagation one.
        # MyTrainTypes: You can specify your training type here.
        # Verbose/VerbosePerLoop: 'Verbose' for your verbose level, and 'VerbosePerLoop' for Verbose frequency and information capture frequency, higher it is, less Verbose frequency.
        # Backup: Save .node file per 10*verbose.
        timescount = 0
        error = 99999
        errorlogs = []
        while(error > Error and (timescount < MaxTimes or MaxTimes == -1)):
            error = MyTrainTypes(MyNeuralNetwork, InputData, OutputData, Speed)
            timescount += 1;
            if Verbose > 1 and timescount%VerbosePerLoop == 0:
                print('Train log >>>Tried times: '+str(timescount)+', error: '+str(error))
            # Verbose training status
            if Verbose > 2 and timescount%100 == 0:
                errorlogs.append(error)
            # Append error to list
            if timescount%(VerbosePerLoop) == 0:
                MyNeuralNetwork.savetoFile(MyNeuralNetwork.Name+'_latest')
            # Backup Neural Network to file
        # Train until it reach its goals
        if Verbose >= 1:
            print('Train log >>>Result: ')
            print('Tried times: '+str(timescount)+', error: '+str(error))
            print('InputData: ')
            print(InputData)
            print('OutputData: ')
            print(OutputData)
            print('Result output: ')
            print(MyNeuralNetwork.feed(InputData))
            print('')
        if Verbose > 2:
            Graph.plotByList(errorlogs, 'Training times (*100 times)', 'error', 'NN='+MyNeuralNetwork.Name+', Speed='+str(Speed)+', Target_error='+str(error)+', Tried_times='+str(timescount))
    # Training batchly