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

def trainbyBatch(MyNeuralNetwork, InputData, OutputData, Error = 0.01, MaxTimes = -1, Speed = 0.1, MyLearningAlgorithm = LearningAlgorithm.BackPropagation, Verbose = 0, VerbosePerLoop = 10000, Backup = True):
    # Parameter explianation:
    # MyNeuralNetwork: Simply your NeuralNetwork
    # InputData/OutputData: Simply your data in numpy's matrix type
    # Error/MaxTimes: The training will stop until its error smaller then Error or reach it MaxTimes(max training times)
    # Speed: Same as the LearningAlgorithm.BackPropagation one.
    # MyLearningAlgorithm: You can specify your training type here.
    # Verbose/VerbosePerLoop: 'Verbose' for your verbose level, and 'VerbosePerLoop' for Verbose frequency and information capture frequency, higher it is, less Verbose frequency.
    # Backup: Save .node file per 10*verbose.
    timescount = 0
    error = 99999
    errorlogs = []
    # errorlogs for pending errors for later Graphing use

    while(error > Error and (timescount < MaxTimes or MaxTimes == -1)):
        error = MyLearningAlgorithm(MyNeuralNetwork, InputData, OutputData, Speed)
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
