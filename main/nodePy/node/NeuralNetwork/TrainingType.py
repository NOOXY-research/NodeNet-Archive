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

import node.IO as IO

import node.NeuralNetwork.Function as f

import node.Parameter as p
# Load parameters

def trainbyBatch(MyNeuralNetwork, Datas, Error = 0.01, MaxEpochs = -1, Profile= p.PROFILE_DEFAULT, Verbose = p.VERBOSE_DEFAULT, VerbosePerLoop = p.VERBOSE_PER_LOOP_DEFAULT, Backup = p.BACKUP_DEFAULT):
    # Parameter explianation:
    # MyNeuralNetwork: Simply your NeuralNetwork
    # INPUTDATA/OUTPUTDATA: Simply your data in numpy's matrix type
    # Error/MaxEpochs: The training will stop until its error smaller then Error or reach it MaxEpochs(max training times)
    # Speed: Same as the LearningAlgorithm.BackPropagation one.
    # MyLearningAlgorithm: You can specify your training type here.
    # Verbose/VerbosePerLoop: 'Verbose' for your verbose level, and 'VerbosePerLoop' for Verbose frequency and information capture frequency, higher it is, less Verbose frequency.
    # Backup: Save .node file per 10*verbose.
    INPUTDATA = Datas[0]
    OUTPUTDATA = Datas[1]
    INPUTVALIDATIONDATA = Datas[2]
    OUTPUTVALIDATIONDATA = Datas[3]
    # Initlalize Datas
    timescount = 0
    error = 99999
    validationerror= 99999
    errorlogs = []
    validationerrorlogs = []
    learningalgorithm = Profile['LearningAlgorithm']
    learingconfiguration = Profile
    recursion = None
    # errorlogs for pending errors for later Graphing use
    if Verbose >= 1:
        print(str(len(INPUTDATA))+' samples. Target error: '+str(Error))
        print('training...')
    while(error > Error and (timescount < MaxEpochs or MaxEpochs == -1)):
        error, recursion = learningalgorithm(MyNeuralNetwork, INPUTDATA, OUTPUTDATA, learingconfiguration, recursion)
        timescount += 1;
        if Verbose > 1 and timescount%VerbosePerLoop == 0:
            print('Training log >>>epochs: '+str(timescount)+', error: '+str(error)+', validation error: '+str(validationerror))
        # Verbose training status
        if Verbose > 2:
            errorlogs.append(error)
            if INPUTVALIDATIONDATA.all() != None:
                validationerror=f.MeanSquareError(OUTPUTVALIDATIONDATA,MyNeuralNetwork.feed(INPUTVALIDATIONDATA))
                validationerrorlogs.append(validationerror)
        # Append error to list
        if (timescount%(VerbosePerLoop) == 0) and Backup == True:
            MyNeuralNetwork.savetoFile(MyNeuralNetwork.Name+'_backup')
        # Backup Neural Network to file
    # Train until it reach its goals
    if Verbose >= 1:
        print('Train log >>>Result: ')
        print('Tried times: '+str(timescount)+', error: '+str(error)+', validation error: '+str(validationerror))
        # print('INPUTDATA: ')
        # IO.printprettyMatrix(INPUTDATA)
        # print('OUTPUTDATA: ')
        # IO.printprettyMatrix(OUTPUTDATA)
        # print('Result output: ')
        # IO.printprettyMatrix(MyNeuralNetwork.feed(INPUTDATA))
        print('')
    if Verbose > 2:
        Graph.plotByList(errorlogs)
        if INPUTVALIDATIONDATA.all() != None:
            Graph.plotByList(validationerrorlogs, 'Epochs', 'error rate', 'NN='+MyNeuralNetwork.Name+', Profile='+str(Profile)+', finalerror='+str(error), LineTags=['Error', 'Validation Error'])
# Training batchly
