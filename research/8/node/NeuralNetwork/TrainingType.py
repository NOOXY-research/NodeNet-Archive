# TrainTypes.py provide stuff related to neural network.
# Author: magneticchen
# note:
# For normal variable use lower case
# For matrix variable use all upper case
# The meaning of 'error' is equivalent to 'cost'
# Operator 'X' for matrix dot multiplication, '*' for matrix elements multiplication. In annotation.
import numpy as np
# Matrix
import node.Graph as Graph
# Import some essential module and function
import node.NeuralNetwork.LearningAlgorithm as LearningAlgorithm

import node.NeuralNetwork.Function as f

def trainbyBatch(MyNeuralNetwork, Datas, Error = 0.01, MaxTimes = -1, Speed = 0.1, MyLearningAlgorithm = LearningAlgorithm.BackPropagation, Verbose = 0, VerbosePerLoop = 10000, Backup = True):
    # Parameter explianation:
    # MyNeuralNetwork: Simply your NeuralNetwork
    # InputData/OutputData: Simply your data in numpy's matrix type
    # Error/MaxTimes: The training will stop until its error smaller then Error or reach it MaxTimes(max training times)
    # Speed: Same as the LearningAlgorithm.BackPropagation one.
    # MyLearningAlgorithm: You can specify your training type here.
    # Verbose/VerbosePerLoop: 'Verbose' for your verbose level, and 'VerbosePerLoop' for Verbose frequency and information capture frequency, higher it is, less Verbose frequency.
    # Backup: Save .node file per 10*verbose.
    InputData = Datas[0]
    OutputData = Datas[1]
    InputValidationData = Datas[2]
    OutputValidationData = Datas[3]
    # Initlalize Datas
    timescount = 0
    error = 99999
    errorlogs = []
    Validationerrorlogs = []
    # errorlogs for pending errors for later Graphing use
    if Verbose >= 1:
        print(str(len(InputData))+' samples. Target error: '+str(Error))
        print('training...')
    while(error > Error and (timescount < MaxTimes or MaxTimes == -1)):
        error = MyLearningAlgorithm(MyNeuralNetwork, InputData, OutputData, Speed)
        timescount += 1;
        if Verbose > 1 and timescount%VerbosePerLoop == 0:
            print('Training log >>>epochs: '+str(timescount)+', error: '+str(error))
        # Verbose training status
        if Verbose > 2:
            errorlogs.append(error)
            if InputValidationData.all() != None:
                Validationerrorlogs.append(f.MeanSquareError(InputValidationData,MyNeuralNetwork.feed(OutputValidationData)))
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
        Graph.plotByList(errorlogs)
        if InputValidationData.all() != None:
            Graph.plotByList(Validationerrorlogs, 'Epochs', 'error rate', 'NN='+MyNeuralNetwork.Name+', Speed='+str(Speed)+', Target_error='+str(error), LineTags=['Error', 'Validation Error'])
# Training batchly
