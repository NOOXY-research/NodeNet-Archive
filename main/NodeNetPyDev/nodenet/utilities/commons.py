# nodenet/utilities/commons.py
# Description:
# "commons.py" provide commons utilities that can be use widely.
# Copyright 2018 NOOXY. All Rights Reserved.

from nodenet.imports.commons import *

def cut_dataset_segment_to_validation(datasets, valid_ratio = 0.1):
    dimension = len(datasets[0].shape)
    valid_data_size = int(len(datasets[0])*0.1)
    input_data = datasets[0]
    output_data = datasets[1]
    input_data_valid = np.empty([0]+list(input_data.shape[1:len(input_data.shape)]))
    output_data_valid = np.empty([0]+list(input_data.shape[1:len(input_data.shape)]))
    for x in range(valid_data_size):
        index = np.random.randint(len(input_data))
        input_data_valid = np.concatenate((input_data_valid, [input_data[index]]))
        output_data_valid = np.concatenate((output_data_valid, [output_data[index]]))
        input_data = np.delete(input_data, index, axis=0)
        output_data = np.delete(output_data, index, axis=0)
    return [input_data, output_data, input_data_valid, output_data_valid]
