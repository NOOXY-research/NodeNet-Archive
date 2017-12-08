# nodenet/neuralnets/container.py
# Description:
# "container.py" provide container to contain nodelayers, netlayers, and others in able to construct neuralnet.
# Copyright 2018 NOOXY. All Rights Reserved.

# The container
class NeuralNetworkContainer(object):
    #
    def __init__(self):
        self.layers = []
        self.latest_output = None

    def __str__(self):
        string = ''
        string += str(self.layers)
        return string

    def forward(self, input_data):
        this_output = input_data
        for layer in self.layers:
            this_output = layer.forward(this_output)
        self.latest_output = this_output
        return this_output

    def backward(self, target_data, cost_function, learning_algorithm, learning_configuration):
        sensitivity_map = cost_function(self.latest_output, target_data, derivative=True)
        for layer in reversed(self.layers):
            sensitivity_map = layer.backward(sensitivity_map, learning_algorithm, learning_configuration)
        return sensitivity_map
