# manager.py provide menus and launch start menu.
import node.Command as cmd
# import essentail command modure for menu.

def StartMenu():
    commanddict = {
        'c': cmd.createNeuralNetwork,
        'l': cmd.loadNeuralNetwork,
    }
    nncmdtype = ['c', 'l']
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

    }
    while True:
        print('')
        print('\n<<< ANN manager @'+MyNeuralNetwork.Name+' >>>')
        print('Train [a]. Train by default [b]. Train by random [c] Feed [d]. Feed by ".mtrx" [e]. Feed test file [f]. Remap weight randomly [g]. Save ANN [s]. Print detail [p]. Return [r]. Help [h].')
        command = input('>>>')
StartMenu()
