# manager.py provide menus and launch start menu.
import node.Command as cmd
# Import essentail command modure for menu.

def StartMenu():
    commanddict = {
        'c': cmd.createNeuralNetwork,
        'l': cmd.loadNeuralNetwork,
        'r': cmd.recoverNeuralNetwork,
        'p': cmd.printMatrix,
        'conf': ConfigMenu,
    }
    # Command's dictionary
    nncmdtype = ['c', 'l', 'r']
    # Command that invoke Neural network management menu
    while True:
        # cmd.clearScreen();
        print('')
        print('')
        print('88b 88  dP\'Yb   dP\'Yb  Yb  dP Yb  dP  TM')
        print('88Yb88 dP   Yb dP   Yb  YbdP   YbdP  ')
        print('88 Y88 Yb   dP Yb   dP  dPYb    88   ')
        print('88  Y8  YbodP   YbodP  dP  Yb   88  Project node. ')
        print('')
        print('Copyright(c)2017 NOOXY inc. Taiwan.')
        print('')
        print('Artificial neural network (ANN) manager. Python ver 0.0.0')
        print('For more information or update ->\'http://www.nooxy.tk\'.')
        print('')
        print('<<< Home Menu >>>\nCreate ANN [c]. Load ANN [l]. Recover from latest train [r]. Print matrix(.mtrx) [p]. Configuration [conf]. Exit [e].')
        command = input('>>>')
        if command == 'e':
            cmd.clearScreen()
            return 0
        if command in commanddict:
            if command in nncmdtype:
                NNManagementMenu(commanddict[command]())
            else:
                commanddict[command]()
# Start menu

def NNManagementMenu(MyNeuralNetwork):
    def printHelp():
        print('\nCommand list:')
        print('[train] Train normallly with custom parameters.')
        print('[traind] Train with default parameters.')
        print('[trainr] Train randomly. ')
        print('[feed] Feed data and get output.')
        print('[feedm] Feed by ".mtrx" file and get output.')
        print('[feedt] Feed test file and get output.')
        print('[remap] Remap neural network\'s weight randomly .')
        print('[save/s] Save neural network to ".node" file .')
        print('[print/p] Print neural network detail.')
        print('[clr] Clear the screen :-).')
        print('[r] Back to home screen.')
        print('[h/help] This list.')
    commanddict = {
        'h': printHelp,
        'help': printHelp,
        'train': cmd.trainNeuralNetwork,
        'traind': cmd.trainNeuralNetworkbyDefault,
        'trainr': cmd.trainNeuralNetworkRandomly,
        'feed': cmd.feedNeuralNetwork,
        'feedm': cmd.feedNeuralNetworkbymtrx,
        'feedt': cmd.feedNeuralNetworkbyTestmtrx,
        'remap': cmd.remapNeuralNetwork,
        'save': cmd.saveNeuralNetwork,
        's': cmd.saveNeuralNetwork,
        'p': cmd.printNeuralNetwork,
        'print': cmd.printNeuralNetwork,
        'clr': cmd.clearScreen,
    }
    # Command's dictionary
    nncmdtype = ['train', 'traind', 'trainr', 'feed', 'feedm', 'feedt', 'save', 's', 'p', 'print']
    # Command type that need NeuralNetwork as Parameter
    returnnncmdtype = ['remap']
    # Command type that return NeuralNetwork
    while True:
        print('')
        print('\n<<< A NeuralNetwork object @'+MyNeuralNetwork.Name+' >>>')
        print('Type "help" to be helped.')
        command = input('>>>')
        if command == 'r':
            cmd.clearScreen()
            return 0
        if command in commanddict:
            if command in nncmdtype:
                commanddict[command](MyNeuralNetwork)
            elif command in returnnncmdtype:
                MyNeuralNetwork = commanddict[command](MyNeuralNetwork)
            else:
                commanddict[command]()
# Neural network management menu

def ConfigMenu():
    commanddict = {
        'l': cmd.listConfigfileValues,
        's': cmd.setValuetoConfigfile,
    }
    while True:
        print('')
        print('\n<<< Configuration Menu >>>\nList All[l]. Set[s]. Return[r]. ')
        print('')
        command = input('>>>')
        if command == 'r':
            cmd.clearScreen()
            return 0
        if command in commanddict:
            commanddict[command]()
# Configuration menu

cmd.clearScreen()
StartMenu()
# Launch start menu
