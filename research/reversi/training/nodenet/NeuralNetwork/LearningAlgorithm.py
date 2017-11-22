# LearningAlgorithm.py provide stuff related to neural network.
# Author: magneticchen
# note:
# For normal variable use lower case
# For matrix variable use all upper case
# The meaning of 'error' is equivalent to 'cost'
# Operator 'X' for matrix dot multiplication, '*' for matrix elements multiplication. In annotation.
import math
# Sqrt
import cupy as np
# Matrix
import nodenet.NeuralNetwork.Function as f
# Activation function etc.

def BackPropagationBase(NeuralNetwork, InputData, OutputData, getWeightChange, getBiasChange):
    # 'Speed' is the training speed, which 'weight adjustment' = speed * djdw
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
    for layer in range(0, NeuralNetwork.LayersCount-1):
        W = np.dot(A[-1], NeuralNetwork.Weight[layer])
        B = np.dot(np.ones((InputData.shape[0],1)), NeuralNetwork.Bias[layer])
        Z.append(W+B)
        A.append(f.sigmoid(Z[-1]))
        # For variable explianation go NeuralNetwork.feed()
    # Push data forward and collect all Z and A
    DELTA.insert(0, np.multiply(-(f.sigmoid(OutputData)-A[NeuralNetwork.LayersCount-1]), f.Derivativeofsigmoid(Z[NeuralNetwork.LayersCount-1])))
    for layer in range(NeuralNetwork.LayersCount-2, -1, -1):
        DJDW.insert(0, np.dot(np.transpose(A[layer]), DELTA[0]))
        # remark that DELTA[0] is always the latest one
        DELTA.insert(0, np.multiply(np.dot(DELTA[0], np.transpose(NeuralNetwork.Weight[layer])), f.Derivativeofsigmoid(Z[layer])))
        # Delta = Deltafront X transpose(ThisLayerWeight) * DerivativeofActivationFunction(ThisLayerBacksideSum)
        # For variable explianation go NeuralNetwork.feed()
    # Get all tangen of weight relative to cost(error)
    for layer in range(0, NeuralNetwork.LayersCount-1):
        NeuralNetwork.Weight[layer] = NeuralNetwork.Weight[layer] + getWeightChange(DJDW, layer)
        NeuralNetwork.Bias[layer] = NeuralNetwork.Bias[layer] + getBiasChange(DELTA, layer)
    # Add adjustment to each weight
    error = f.MeanSquareError(OutputData, Z[NeuralNetwork.LayersCount-1])
    return error
# A type of training is called BackPropagation for DFF

def BackPropagation(NeuralNetwork, InputData, OutputData, LearningConfiguration, Recursion = None):
    speed = LearningConfiguration['Speed']
    def getWeightChange(DJDW, LayerIndex):
        return -speed*DJDW[LayerIndex]
    # Apply weight changes

    def getBiasChange(DELTA, LayerIndex):
        return -speed*np.dot(np.ones((1, InputData.shape[0])), DELTA[LayerIndex+1])
    # Apply bias changes

    return BackPropagationBase(NeuralNetwork, InputData, OutputData, getWeightChange, getBiasChange), None
# A type of training is called BackPropagation for DFF

def ClassicalMomentum(NeuralNetwork, InputData, OutputData, LearningConfiguration, Recursion = None):
    # Recursion for providing volume of momentum otherwise after this function ended. The record will disappear.
    speed = LearningConfiguration['Speed']
    momentumrate = LearningConfiguration['Momentum_Rate']
    weightmomentum = []
    biasmomentum = []
    if Recursion == None:
        for layer in range(0, NeuralNetwork.LayersCount-1):
            weightmomentum.append(np.zeros((NeuralNetwork.LayerNeuronsCount[layer], NeuralNetwork.LayerNeuronsCount[layer+1])))
            biasmomentum.append(np.zeros((1, NeuralNetwork.LayerNeuronsCount[layer+1])))
        # Initlalize momentum with right size
    else:
        weightmomentum = Recursion[0]
        biasmomentum = Recursion[1]
        # Recover status from Recursion Parameter
    # Initlalize momentum

    def getWeightChange(DJDW, LayerIndex):
        weightchange = -speed*DJDW[LayerIndex] + momentumrate*weightmomentum[LayerIndex]
        weightmomentum[LayerIndex] = weightchange
        return weightchange
    # Apply weight changes

    def getBiasChange(DELTA, LayerIndex):
        biaschange = -speed*np.dot(np.ones((1, InputData.shape[0])), DELTA[LayerIndex+1]) + momentumrate*biasmomentum[LayerIndex]
        biasmomentum[LayerIndex] = biaschange
        return biaschange
    # Apply bias changes

    return BackPropagationBase(NeuralNetwork, InputData, OutputData, getWeightChange, getBiasChange), [weightmomentum, biasmomentum]
# A type of training is called ClassicalMomentum for DFF

def NesterovMomentum(NeuralNetwork, InputData, OutputData, LearningConfiguration, Recursion = None):
    # Recursion for providing volume of momentum otherwise after this function ended. The record will disappear.
    speed = LearningConfiguration['Speed']
    momentumrate = LearningConfiguration['Momentum_Rate']
    weightmomentum = []
    biasmomentum = []
    first = False
    if Recursion == None:
        first = True
        for layer in range(0, NeuralNetwork.LayersCount-1):
            weightmomentum.append(np.zeros((NeuralNetwork.LayerNeuronsCount[layer], NeuralNetwork.LayerNeuronsCount[layer+1])))
            biasmomentum.append(np.zeros((1, NeuralNetwork.LayerNeuronsCount[layer+1])))
        # Initlalize momentum with right size
    else:
        weightmomentum = Recursion[0]
        biasmomentum = Recursion[1]
        # Recover status from Recursion Parameter
    # Initlalize momentum

    def getWeightChange(DJDW, LayerIndex):
        if first == True:
            weightchange = -momentumrate*speed*DJDW[LayerIndex]
        else:
            weightchange = -speed*DJDW[LayerIndex] + momentumrate*weightmomentum[LayerIndex]
        weightmomentum[LayerIndex] = weightchange
        return weightchange
    # Apply weight changes

    def getBiasChange(DELTA, LayerIndex):
        if first == True:
            biaschange = -momentumrate*speed*np.dot(np.ones((1, InputData.shape[0])), DELTA[LayerIndex+1])
        else:
            biaschange = -speed*np.dot(np.ones((1, InputData.shape[0])), DELTA[LayerIndex+1]) + momentumrate*biasmomentum[LayerIndex]
        biasmomentum[LayerIndex] = biaschange
        return biaschange
    # Apply bias changes

    return BackPropagationBase(NeuralNetwork, InputData, OutputData, getWeightChange, getBiasChange), [weightmomentum, biasmomentum]
# A type of training is called NesterovMomentum for DFF

def AdaGrad(NeuralNetwork, InputData, OutputData, LearningConfiguration, Recursion = None):
    # Recursion for providing volume of momentum otherwise after this function ended. The record will disappear.
    speed = LearningConfiguration['Speed']
    epsilon = LearningConfiguration['Epsilon']
    weightsquaresum = []
    biassquaresum = []
    # Nessasary parameters for AdaGrad

    if Recursion == None:
        for layer in range(0, NeuralNetwork.LayersCount-1):
            weightsquaresum.append(np.zeros((NeuralNetwork.LayerNeuronsCount[layer], NeuralNetwork.LayerNeuronsCount[layer+1])))
            biassquaresum.append(np.zeros((1, NeuralNetwork.LayerNeuronsCount[layer+1])))
        # Initlalize squaresum with right size
    else:
        weightsquaresum = Recursion[0]
        biassquaresum = Recursion[1]
        # Recover status from Recursion Parameter
    # Initlalize squaresum

    def getWeightChange(DJDW, LayerIndex):
        weightsquaresum[LayerIndex] += np.power(DJDW[LayerIndex], 2 )
        weightchange = -speed*DJDW[LayerIndex]/(np.sqrt(weightsquaresum[LayerIndex])+epsilon)
        return weightchange
    # Apply weight changes

    def getBiasChange(DELTA, LayerIndex):
        biasgradient = np.dot(np.ones((1, InputData.shape[0])), DELTA[LayerIndex+1])
        biassquaresum[LayerIndex] += np.power(biasgradient, 2 )
        biaschange = -speed*biasgradient/(np.sqrt(biassquaresum[LayerIndex])+epsilon)
        return biaschange
    # Apply bias changes
    return BackPropagationBase(NeuralNetwork, InputData, OutputData, getWeightChange, getBiasChange), [weightsquaresum, biassquaresum]
# A type of training is called AdaGrad for DFF

def Adadelta(NeuralNetwork, InputData, OutputData, LearningConfiguration, Recursion = None):
    # Recursion for providing volume of momentum otherwise after this function ended. The record will disappear.
    pass

def RMSprop(NeuralNetwork, InputData, OutputData, LearningConfiguration, Recursion = None):
        # Recursion for providing volume of momentum otherwise after this function ended. The record will disappear.
        speed = LearningConfiguration['Speed']
        epsilon = LearningConfiguration['Epsilon']
        decayrate = LearningConfiguration['DecayRate']
        weightsquaresum = []
        biassquaresum = []
        # Nessasary parameters for AdaGrad

        if Recursion == None:
            for layer in range(0, NeuralNetwork.LayersCount-1):
                weightsquaresum.append(np.zeros((NeuralNetwork.LayerNeuronsCount[layer], NeuralNetwork.LayerNeuronsCount[layer+1])))
                biassquaresum.append(np.zeros((1, NeuralNetwork.LayerNeuronsCount[layer+1])))
            # Initlalize squaresum with right size
        else:
            weightsquaresum = Recursion[0]
            biassquaresum = Recursion[1]
            # Recover status from Recursion Parameter
        # Initlalize squaresum

        def getWeightChange(DJDW, LayerIndex):
            weightsquaresum[LayerIndex] = (decayrate)*weightsquaresum[LayerIndex] + (1-decayrate)*np.power(DJDW[LayerIndex], 2 )
            weightchange = -speed*DJDW[LayerIndex]/(np.sqrt(weightsquaresum[LayerIndex])+epsilon)
            return weightchange
        # Apply weight changes

        def getBiasChange(DELTA, LayerIndex):
            biasgradient = np.dot(np.ones((1, InputData.shape[0])), DELTA[LayerIndex+1])
            biassquaresum[LayerIndex] = (decayrate)*biassquaresum[LayerIndex] + (1-decayrate)*np.power(biasgradient, 2 )
            biaschange = -speed*biasgradient/(np.sqrt(biassquaresum[LayerIndex])+epsilon)
            return biaschange
        # Apply bias changes
        return BackPropagationBase(NeuralNetwork, InputData, OutputData, getWeightChange, getBiasChange), [weightsquaresum, biassquaresum]
# A type of training is called RMSprop for DFF

def Adam(NeuralNetwork, InputData, OutputData, LearningConfiguration, Recursion = None):
        # Recursion for providing volume of momentum otherwise after this function ended. The record will disappear.
        speed = LearningConfiguration['Speed']
        epsilon = LearningConfiguration['Epsilon']
        beta1 = LearningConfiguration['Beta1']
        beta2 = LearningConfiguration['Beta2']
        weightm = []
        biasm = []
        weightv = []
        biasv = []
        # Nessasary parameters for AdaGrad

        if Recursion == None:
            for layer in range(0, NeuralNetwork.LayersCount-1):
                weightm.append(np.zeros((NeuralNetwork.LayerNeuronsCount[layer], NeuralNetwork.LayerNeuronsCount[layer+1])))
                biasm.append(np.zeros((1, NeuralNetwork.LayerNeuronsCount[layer+1])))
                weightv.append(np.zeros((NeuralNetwork.LayerNeuronsCount[layer], NeuralNetwork.LayerNeuronsCount[layer+1])))
                biasv.append(np.zeros((1, NeuralNetwork.LayerNeuronsCount[layer+1])))
            # Initlalize squaresum with right size
        else:
            weightm = Recursion[0]
            biasm = Recursion[1]
            weightv = Recursion[2]
            biasv = Recursion[3]
            # Recover status from Recursion Parameter
        # Initlalize squaresum

        def getWeightChange(DJDW, LayerIndex):
            weightm[LayerIndex] = (beta1)*weightm[LayerIndex] + (1-beta1)*DJDW[LayerIndex]
            weightv[LayerIndex] = (beta2)*weightv[LayerIndex] + (1-beta2)*np.power(DJDW[LayerIndex], 2 )
            weightchange = -speed*weightm[LayerIndex]/(np.sqrt(weightv[LayerIndex])+epsilon)
            return weightchange
        # Apply weight changes

        def getBiasChange(DELTA, LayerIndex):
            biasgradient = np.dot(np.ones((1, InputData.shape[0])), DELTA[LayerIndex+1])
            biasm[LayerIndex] = (beta1)*biasm[LayerIndex] + (1-beta1)*biasgradient
            biasv[LayerIndex] = (beta2)*biasv[LayerIndex] + (1-beta2)*np.power(biasgradient, 2 )
            biaschange = -speed*biasgradient/(np.sqrt(biasv[LayerIndex])+epsilon)
            return biaschange
        # Apply bias changes
        return BackPropagationBase(NeuralNetwork, InputData, OutputData, getWeightChange, getBiasChange), [weightm, biasm, weightv, biasv]
# A type of training is called Adam for DFF
