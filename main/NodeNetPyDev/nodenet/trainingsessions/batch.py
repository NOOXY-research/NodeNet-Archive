# nodenet/trainingsessions/batch.py
# Description:
# "container.py" provide container to contain nodelayers, netlayers, and others in able to construct neuralnet.
# Copyright 2018 NOOXY. All Rights Reserved.

from nodenet.imports.commons import *
import nodenet.learningalgorithm as la
import nodenet.learningalgorithm.defaultconfigurations as laconf
import nodenet.interface.console as console
import nodenet.functions as f

class MiniBatchSession(object):
    def __init__(self, neuralnet=None, datasets=None, target_loss=None ,mini_batch_size=None, learning_algorithm=la.adam, learning_configuration=laconf.adam, loss_function=f.mean_square, max_epoch=None, verbose=True, verbose_interval=100):
        self.neuralnet = neuralnet
        self.input_data = None
        self.output_data = None
        self.input_data_valid = None
        self.output_data_valid = None
        self.target_loss = target_loss
        self.mini_batch_size = mini_batch_size
        self.learning_algorithm = learning_algorithm
        self.learning_configuration = learning_configuration
        self.loss_function = loss_function
        self.max_epoch = max_epoch
        self.iterations_each_epoch = None
        self.verbose = verbose
        self.verbose_interval = verbose_interval

        if datasets is not None:
            if len(datasets) <= 2:
                self.input_data = datasets[0]
                self.output_data = datasets[1]
            else:
                self.input_data = datasets[0]
                self.output_data = datasets[1]
                self.input_data_valid = datasets[2]
                self.output_data_valid = datasets[3]
            self.iterations_each_epoch = int(len(datasets[0])/mini_batch_size)

        if self.max_epoch is not None:
            self.max_iteration = self.max_epoch*self.iterations_each_epoch
        else:
            self.max_iteration = None

    def __str__(self):
        string = ''
        string = 'neuralnet : '+str(self.neuralnet)+', target loss : '+str(target_loss)+', mini batch size : '+str(self.mini_batch_size)+', max epoch : '+str(self.max_epoch)+', cost function : '+str(loss_function)
        return string

    __repr__ = __str__

    setup = __init__

    def getRandomMiniBatch(self):
        rand_range = len(self.input_data)-self.mini_batch_size
        start_index = 0
        if rand_range != 0:
            start_index = np.random.randint(len(self.input_data)-self.mini_batch_size)
        return self.input_data[start_index:start_index+self.mini_batch_size], self.output_data[start_index:start_index+self.mini_batch_size]

    def startTraining(self):
        iterations_sum = 0
        loss_record_train = [] # each epoch
        loss_record_valid = []
        latest_loss = 99999
        max_iteration = np.inf

        if self.max_iteration is not None:
            max_iteration = self.max_iteration

        console.log('training', 'start training session...')
        console.log('training', str(len(self.input_data))+' training datasets. '+str(len(self.input_data_valid))+' validation datasets.')
        while(iterations_sum <= max_iteration and latest_loss > self.target_loss):
            # Do record of loss first
            if iterations_sum%self.iterations_each_epoch == 0:
                train_loss = np.mean(self.loss_function(self.neuralnet.forward(self.input_data), self.output_data))
                valid_loss = np.mean(self.loss_function(self.neuralnet.forward(self.input_data_valid), self.output_data_valid))
                loss_record_train.append(train_loss)
                loss_record_valid.append(valid_loss)
                if (iterations_sum/self.iterations_each_epoch)%self.verbose_interval == 0 and self.verbose:
                    console.log('training', 'epochs: '+str(iterations_sum/self.iterations_each_epoch)+', train_loss: '+str(loss_record_train[-1])+', valid_loss: '+str(loss_record_valid[-1]))

            this_batch_input, this_batch_output = self.getRandomMiniBatch()
            self.neuralnet.forward(this_batch_input, trace=True)
            self.neuralnet.backward(this_batch_output, self.loss_function, self.learning_algorithm, self.learning_configuration)
            iterations_sum += 1
            latest_loss = loss_record_train[-1]

        return loss_record_train, loss_record_valid


class WholeBatchSession(object):
    pass
