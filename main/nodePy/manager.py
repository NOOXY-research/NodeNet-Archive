# manager.py provide menus and launch start menu.
import node.Command as cmd
# Import essentail command modure for menu.

def StartMenu():
    commanddict = {
        'c': cmd.createNeuralNetwork,
        'l': cmd.loadNeuralNetwork,
        'r': cmd.recoverNeuralNetwork,
        'p': cmd.printMatrix,
        'ls': cmd.ls,
        'conf': ConfigMenu,
    }
    # Command's dictionary
    nncmdtype = ['c', 'l', 'r']
    # Command that invoke Neural network management menu
    while True:
        # cmd.clearScreen();
        print('')
        print('<<< Home Menu >>>\n[c]reate ANN. [l]oad ANN. [r]ecover ANN. [p]rint matrix(.mtrx). [conf]igure. [ls]. [e]xit.')
        command = input('>>>')
        if command == 'e':
            cmd.clearScreen()
            return 0
        if command in commanddict:
            if command in nncmdtype:
                NN = commanddict[command]()
                cmd.clearScreen()
                cmd.printLogo()
                NNManagementMenu(NN)
            else:
                cmd.clearScreen()
                cmd.printLogo()
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
        print('<<< A NeuralNetwork object @'+MyNeuralNetwork.Name+' >>>')
        print('layer structure:')
        print(MyNeuralNetwork.LayerNeuronsCount)
        print('Type "help" to be helped.')
        command = input('>>>')
        if command == 'r':
            cmd.clearScreen()
            cmd.printLogo()
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
        print('<<< Configuration Menu >>>\n[l]ist All. [s]et. [r]eturn home. ')
        print('')
        command = input('>>>')
        if command == 'r':
            cmd.clearScreen()
            cmd.printLogo()
            return 0
        if command in commanddict:
            commanddict[command]()
# Configuration menu

cmd.clearScreen()
cmd.printLogo()
StartMenu()
# Launch start menu
