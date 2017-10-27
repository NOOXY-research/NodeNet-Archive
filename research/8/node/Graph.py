# NeuralNetwork.py provide graphing.
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
# Ploting
def plotByList(MyList, xlabel, ylabel, Title):
    plt.plot(MyList)
    plt.title(Title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show(block=False)
