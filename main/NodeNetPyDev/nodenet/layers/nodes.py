# nodenet/layers/nodes.py
# Description:
# "nodes.py" provide node layers.
# Copyright 2018 NOOXY. All Rights Reserved.

import numpy as np

# Vector Nodes input: 2D vector, output: 2D vector
class Vector(object):
    def __init__(self, nodes_size, activatior):
        self.nodes_size = nodes_size
        self.activator = activatior
        self.latest_input_signal = None
        self.latest_sensitivity_map - None

    def __str__(self):
        string = 'VectorNodes('+str(self.nodes_size)+', '+str(self.activator)+')'

    def forward(self, input_signal):
        self.latest_input_signal = input_signal
        return self.activator(input_signal)

    def update_gradient(self, input_sensitivity_map):
        self.latest_sensitivity_map = np.multiply(input_sensitivity_map, self.activator(self.latest_input_signal, derivative=True))

    def get_sensitivity_map(self):
        return self.latest_sensitivity_map

    def backward(self, input_sensitivity_map, **kwargs):
        self.update_gradient(input_sensitivity_map)
        return self.get_sensitivity_map()

class Tensor(object):
    pass
