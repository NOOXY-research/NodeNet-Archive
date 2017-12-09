# nodenet/neuralnets/container.py
# Description:
# "container.py" provide container to contain nodelayers, netlayers, and others in able to construct neuralnet.
# Copyright 2018 NOOXY. All Rights Reserved.

# The simplest type of container
class SimpleContainer(object):
    #
    def __init__(self, layers=None, name='Unamed NeuralNet'):
        self.name = name
        self.layers = layers
        self.latest_output = None

    def __str__(self):
        string = ''
        string += self.name +' : \n'
        for x in self.layers:
            string += 'layer('+str(self.layers.index(x))+'): '+str(x)+'\n'
        return string

    __repr__ = __str__

    setup = __init__

    def forward(self, input_data, trace=False):
        this_output = input_data
        for layer in self.layers:
            # print(this_output)
            this_output = layer.forward(this_output, trace)
        self.latest_output = this_output
        # print('end')
        return this_output

    def backward(self, target_data, loss_function, learning_algorithm, learning_configuration):
        sensitivity_map = loss_function(self.latest_output, target_data, derivative=True)
        for layer in reversed(self.layers):
            sensitivity_map = layer.backward(sensitivity_map, learning_algorithm, learning_configuration)
        return sensitivity_map

#
class LinkedContainer(object):
    pass
