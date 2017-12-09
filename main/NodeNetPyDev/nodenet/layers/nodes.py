# nodenet/layers/nodes.py
# Description:
# "nodes.py" provide node layers.
# Copyright 2018 NOOXY. All Rights Reserved.

from nodenet.imports.commons import *
import nodenet.functions as func

# Vector Nodes input: 2D vector, output: 2D vector
class NodesVector(object):
    def __init__(self, nodes_size, activatior=func.sigmoid):
        self.nodes_size = nodes_size
        self.activator = activatior
        self.latest_input_signal = None
        self.latest_sensitivity_map = None
        self.dropout = False
        self.dropout_mask = None

    def __str__(self):
        string = ''
        string += 'VectorNodes('+str(self.nodes_size)+', '+str(self.activator)+')'
        return string

    __repr__ = __str__

    def forward(self, input_signal, trace=False):
        if trace:
            self.latest_input_signal = input_signal
        return self.activator(input_signal)

    def update_gradient(self, input_sensitivity_map):
        self.latest_sensitivity_map = np.multiply(input_sensitivity_map, self.activator(self.latest_input_signal, derivative=True))

    def get_sensitivity_map(self):
        return self.latest_sensitivity_map

    def backward(self, input_sensitivity_map, *args):
        self.update_gradient(input_sensitivity_map)
        return self.get_sensitivity_map()

class NodesTensor(object):
    pass
