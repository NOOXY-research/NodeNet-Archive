# nodenet/tester/simpletest.py
# Description:
# "simpletest.py" provide testing lightly.
# Copyright 2018 NOOXY. All Rights Reserved.

import numpy as np
import nodenet.neuralnets as nn
import nodenet.layers as layers
import nodenet.functions as f
import nodenet.trainingsessions as sessions
import nodenet.interface.graph as graph
import nodenet.utilities.datagenerator as datagen
import nodenet.utilities.commons as util
import nodenet.interface.console as console
import nodenet.io as nnio

# Graphing test 1
console.logo()
fig = graph.Figure((2, 1))
datasets = datagen.sin_1x1(1000)
datasets = util.cut_dataset_segment_to_validation([datasets[0], datasets[1]])
console.log('tester', 'graphing test 1...')
fig.plot_2D(datasets[0].flatten(), datasets[1].flatten(), 0, 'graph of sin(x) and training result')
console.log('tester', 'graphing 1 passed.')

# NeuralNet test
console.log('tester', 'neuralnet test...')
neuralnet = nn.SimpleContainer()
layers = [
    layers.NodesVector(1, f.linear),
    layers.FullyConnected1D(1, 8),
    layers.NodesVector(8, f.tanh),
    layers.FullyConnected1D(8, 8),
    layers.NodesVector(8, f.tanh),
    layers.FullyConnected1D(8, 1),
    layers.NodesVector(1, f.linear),
]
neuralnet.setup(layers, name='tester neuralnet')
console.log('tester', str(neuralnet))
console.log('tester', 'neuralnet passed.')

# Training test
console.log('tester', 'training test...')
batch_training = sessions.MiniBatchSession()
batch_training.setup(neuralnet, datasets, target_loss=0.00001, mini_batch_size=100, max_epoch=10000, verbose_interval=1000)
loss = batch_training.startTraining()
fig.plot_traing_loss(loss, 1)
console.log('tester', 'training test passed.')

# Graphing test 2
console.log('tester', 'graphing test 2...')
inputx = np.linspace(-10, 10, 100)
outputy = []
for x in inputx:
    outputy.append(neuralnet.forward(np.array([x]))[0])
fig.plot_2D(inputx, outputy, 0, 'training')
console.log('tester', 'graphing test 2 passed.')

# IO test
console.log('tester', 'io test...')
nnio.save_neuralnet(neuralnet, 'tester')
newneuralnet = nnio.load_neuralnet('tester')
console.log('tester', str(neuralnet))
console.log('tester', 'io test passed.')

console.log('tester', 'test passed. Press any key to escape.')
input()
