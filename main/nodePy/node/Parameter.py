# Parameter.py shares variables that be refered globally
import node.NeuralNetwork.LearningAlgorithm as LA

NODEPY_VERSION = 'Python aphla 1.1.0'
VERBOSE_PER_LOOP_DEFAULT = 10000
SAVED_PATH = 'saved/'
DATA_PATH = 'data/'
BACKUP_DEFAULT = True
VERBOSE_DEFAULT = 2
LearningAlgorithmDict = {
'BackPropagation' : LA.BackPropagation,
'BackPropagationwithMomentum' : LA.BackPropagationwithMomentum,
}
# General

MOMENTUM_DEFAULT = 0
SPEED_DEFAULT = 0.1
PROFILE_DEFAULT = {
'LearningAlgorithm': LA.BackPropagation,
'SPEED': SPEED_DEFAULT,
}
# Neural Network
