# Parameter.py shares variables that be refered globally
import nodenet.NeuralNetwork.LearningAlgorithm as LA

NODENETPY_VERSION = 'Python aphla 1.1.5'
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
'Adadelta' : LA.Adadelta,
'RMSprop' : LA.RMSprop,
'Adam' : LA.Adam,
}
# General

PROFILE_DEFAULT = {
'LearningAlgorithm' : LA.BackPropagation,
'MomentumRate' : 0.8,
'Speed' : 0.01,
'Epsilon' : 1e-8,
'DecayRate' : 0.9,
'Beta1' : 0.9,
'Beta2' : 0.999,
}
# Neural Network
