# nodenet/utilities/datagenerator.py
# Description:
# "datagenerator.py" provide generated data for testing.
# Copyright 2018 NOOXY. All Rights Reserved.

from nodenet.imports.commons import *
import random

def sin_1x1(datasize):
    input_data = []
    output_data = []
    input_data_valid = []
    output_data_valid = []

    for x in range(0, datasize):
        randint = random.randint(-50000, 50000)
        while randint in input_data:
            randint = random.randint(-50000, 50000)
        input_data.append([(randint/50000)*np.pi*2])

    input_data_np = np.array(input_data)
    output_data_np = np.sin(input_data)

    return [input_data_np, output_data_np]
