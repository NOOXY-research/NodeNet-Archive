import numpy as np # Matrix
import NN_function as f # Activation function etc.
# Import some essential module and function

class NeuralNetwork(object):
    def __init__(self, LayersCount = 1, LayerNeuronsCount = [1]):
        self.LayersCount = LayersCount
        self.LayerNeuronsCount = LayerNeuronsCount
        self.Weight = []
        self.Bias = []
        # Initialize some general variable for NN
        for x in range(0, self.LayersCount-1):
            self.Weight.append(np.random.randn(self.LayerNeuronsCount[x], self.LayerNeuronsCount[x+1]))
            self.Bias.append(np.random.randn(1, self.LayerNeuronsCount[x+1]))
    # Initlalize NN structure

    def __str__(self):
        s = ""
        for x in range(0, self.LayersCount-1):
            s = s+"*** layer "+str(x)+" ***\n"
            s = s+"    >>>layer "+str(x)+" Neurons Count\n"
            s = s+"    "+str(self.LayerNeuronsCount[x])+"\n"
            s = s+"    >>>layer "+str(x)+" to "+str(x+1)+" Weight\n"
            s = s+str(self.Weight[x])+"\n"
            s = s+"    >>>layer "+str(x)+" to "+str(x+1)+" Bias\n"
            s = s+str(self.Bias[x])+"\n"
        # Print it layer by layer one by one
        s = s+"*** layer "+str(self.LayersCount)+" ***\n"
        s = s+"    layer "+str(self.LayersCount)+" Neurons Count\n"
        s = s+str(self.LayerNeuronsCount[self.LayersCount-1])+"\n"
        return s
    # Print detail info for Neural Network

    def feed(self, InputData):
        A = f.sigmoid(InputData)
        for x in range(0, self.LayersCount-1):
            W = np.dot(A, self.Weight[x])
            B = np.dot(np.ones((InputData.shape[0],1)), self.Bias[x])
            A = f.sigmoid(W + B)
        return A
        # A = sigmoid(BacksideSum)
        # W = A*Weight
        # B = Ones(InputDataAmount, 1)*Bias
        # BacksideSum = W+B or InputData
    # Feed data forward

def trainbyBackPropagation(MyNeuralNetwork, InputData, OutputData, speed = 0.1):
    print()
