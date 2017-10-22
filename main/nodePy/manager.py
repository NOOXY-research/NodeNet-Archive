# manager.py provide menus and launch start menu.
import node.Command as cmd
# import essentail command modure for menu.

def StartMenu():
    commanddict = {
        'c': cmd.createNeuralNetwork,
        'l': cmd.loadNeuralNetwork,
        'r': cmd.recoverNeuralNetwork,
        'p': cmd.printMatrix,
    }
    nncmdtype = ['c', 'l', 'r']
    while True:
        print('')
        print('')
        print('88b 88  dP\'Yb   dP\'Yb  Yb  dP Yb  dP ')
        print('88Yb88 dP   Yb dP   Yb  YbdP   YbdP  ')
        print('88 Y88 Yb   dP Yb   dP  dPYb    8P   ')
        print('88  Y8  YbodP   YbodP  dP  Yb  dP    ')
        print('')
        print('PROJECT node. Copyright(c)2017 NOOXY inc. Taiwan.')
        print('')
        print('Artificial neural network (ANN) manager. Python ver 0.0.0')
        print('For more information or update ->\'http://www.nooxy.tk\'.')
        print('')
        print('<<< Home >>>\nCreate ANN [c]. Load ANN [l]. Recover from latest train [r]. Print matrix(.mtrx) [p]. Exit [e].')
        command = input('>>>')
        if command == 'e':
            return 0
        elif command in nncmdtype:
            NNManagementMenu(commanddict[command]())
        else:
            commanddict[command]()
def NNManagementMenu(MyNeuralNetwork):
    commanddict = {
        'a':cmd.trainNeuralNetwork,
        'b':cmd.trainNeuralNetworkbyDefault,
        'c':cmd.trainNeuralNetworkRandomly,
        'd':cmd.feedNeuralNetwork,
        'e':cmd.feedNeuralNetworkbymtrx,
        'f':cmd.feedNeuralNetworkbyTestmtrx,
        'g':cmd.remapNeuralNetwork,
        's':cmd.saveNeuralNetwork,
        'p':cmd.printNeuralNetwork,
    }
    nncmdtype = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 's', 'p']
    while True:
        print('')
        print('\n<<< ANN manager @'+MyNeuralNetwork.Name+' >>>')
        print('Train [a]. Train by default [b]. Train by random [c] Feed [d]. Feed by ".mtrx" [e]. Feed test file [f]. Remap weight randomly [g]. Save ANN [s]. Print detail [p]. Return [r]. Help [h].')
        command = input('>>>')
        if command == 'r':
            return 0
        elif command in nncmdtype:
            commanddict[command](MyNeuralNetwork)
        else:
            commanddict[command]()
StartMenu()
