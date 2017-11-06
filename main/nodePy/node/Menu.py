# manager.py provide menus and launch start menu.
import node.Command as cmd
# Import essentail command modure for menu.

def StartMenu():
    commanddict = {
        'c': cmd.createNeuralNetwork,
        'o': cmd.loadNeuralNetwork,
        'r': cmd.recoverNeuralNetwork,
        'l': cmd.loadLatestNeuralNetwork,
        'p': cmd.printMatrix,
        'list': cmd.list,
        'idx2mtrx': cmd.idx2mtrx,
        'conf': ConfigMenu,
    }
    # Command's dictionary
    nncmdtype = ['c', 'o', 'l', 'r']
    # Command that invoke Neural network management menu
    while True:
        # cmd.clearScreen();
        print('')
        print('<<< Home Menu >>>')
        print('[c]reate. [o]pen. [l]atest('+cmd.getLatestNeuralNetworkName()+'). [r]ecover. NeuralNetwork')
        print('[p]rint matrix(.mtrx). [conf]igure. [list]. [e]xit.')
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
        print('[train] Train the neural network  .')
        print('[edit] Edit neural network training profile.')
        print('[trainr] Train randomly. ')
        print('[feed] Feed data and get output.')
        print('[feedm] Feed by ".mtrx" file and get output.')
        # print('[feedt] Feed test file and get output.')
        print('[remap] Remap neural network\'s weight randomly .')
        print('[save/s] Save neural network to ".node" file .')
        print('[saveas] Save neural network as new ".node" file .')
        print('[print/p] Print neural network detail.')
        print('[plot] Plot neural network(1 input 1 output only).')
        print('[clr] Clear the screen :-).')
        print('[r] Back to home screen.')
        print('[h/help] This list.')

    commanddict = {
        'h': printHelp,
        'help': printHelp,
        'train': cmd.trainNeuralNetwork,
        'edit': cmd.editNeuralNetworkProfile,
        'trainr': cmd.trainNeuralNetworkRandomly,
        'feed': cmd.feedNeuralNetwork,
        'feedm': cmd.feedNeuralNetworkbymtrx,
        # 'feedt': cmd.feedNeuralNetworkbyTestmtrx,
        'remap': cmd.remapNeuralNetwork,
        'save': cmd.saveNeuralNetwork,
        'saveas': cmd.saveNeuralNetworkAs,
        's': cmd.saveNeuralNetwork,
        'p': cmd.printNeuralNetwork,
        'print': cmd.printNeuralNetwork,
        'plot': cmd.plotNeuralNetwork,
        'clr': cmd.clearScreen,
    }
    # Command's dictionary
    nncmdtype = ['train', 'edit', 'trainr', 'feed', 'feedm', 'feedt', 'save', 's', 'saveas', 'p', 'print', 'plot']
    # Command type that need NeuralNetwork as Parameter
    returnnncmdtype = ['remap']
    # Command type that return NeuralNetwork
    while True:
        print('')
        print('<<< A NeuralNetwork object @'+MyNeuralNetwork.Name+' >>>')
        print('layer structure:')
        print(MyNeuralNetwork.LayerNeuronsCount)
        cmd.printNeuralNetworkProfile(MyNeuralNetwork)
        print()
        print('Type "help" to be helped. To save neural network key "save"!')
        command = input('>>>')
        if command == 'r':
            cmd.clearScreen()
            cmd.printLogo()
            return 0
        if command in commanddict:
            if command in nncmdtype:
                try:
                    commanddict[command](MyNeuralNetwork)
                except(KeyboardInterrupt, SystemExit):
                    print('\n***YOU INTERRUPT TRAINING. STATE NOT CHANGE.***\n')
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
