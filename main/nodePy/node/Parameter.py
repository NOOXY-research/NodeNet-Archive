# Parameter.py shares variables that be refered globally
import node.NeuralNetwork.LearningAlgorithm as LA

NODEPY_VERSION = 'Python aphla 1.1.4'
VERBOSE_PER_LOOP_DEFAULT = 10000
SAVED_PATH = 'saved/'
DATA_PATH = 'data/'
BACKUP_DEFAULT = True
VERBOSE_DEFAULT = 2
LearningAlgorithmDict = {
'BackPropagation' : LA.BackPropagation,
'ClassicalMomentum' : LA.ClassicalMomentum,
'NesterovMomentum' : LA.NesterovMomentum,
'AdaGrad' : LA.AdaGrad,
'Adam' : LA.Adam,
'Adadelta' : LA.Adadelta,
'RMSprop' : LA.RMSprop,
}
# General

PROFILE_DEFAULT = {
'LearningAlgorithm': LA.BackPropagation,
'Momentum_Rate': 0,
'Speed': 0.1,
'Epsilon': 1e-8,
}
# Neural Network
