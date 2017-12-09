# nodenet/io/neuralnet.py
# Description:
# "neuralnet.py" provide access between file and neuralnet.
# Copyright 2018 NOOXY. All Rights Reserved.

import pickle

def save_neuralnet(neuralnet, filename):
    btyes = pickle.dumps(neuralnet)
    f = open(filename+'.nodenet', 'wb')
    f.write(btyes)
    f.close()

def load_neuralnet(filename):
    f = open(filename+'.nodenet', 'rb')
    btyes = f.read()
    neuralnet = pickle.loads(btyes)
    f.close()
    return neuralnet
