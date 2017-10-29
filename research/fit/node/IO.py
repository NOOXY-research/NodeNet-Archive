# IO.py provide Interface to access files. e.g ".node" file.
import numpy as np
import json
import struct

class RAWReader(object):
    def __init__(self):
        self.SlicedString = []
    # Initialize
    def open(self, Filename):
        try:
            f = open(Filename, 'r')
        except:
            print('Warning: RAWReader readfile "'+Filename+'" not exist.')
        self.SlicedString = (f.read()).split()
        f.close()
    # Translate file to splited list
    def pop(self):
        if len(self.SlicedString) > 0:
            return self.SlicedString.pop(0)
        else:
            return None
    # Mock C++ >> operator
# A reader mock C++ style

class RAWWriter(object):
    def __init__(self):
        self.SlicedString = []
    # Initialize
    def write(self, Filename):
        f = open(Filename, 'w')
        for word in self.SlicedString:
            f.write(str(word)+" ")
        f.close()
        self.SlicedString = []
    # Translate file to splited list
    def append(self, Word):
        self.SlicedString.append(Word)
    # Mock C++ << operator
    def newline(self):
        self.SlicedString.append('\n')
    # Add a new line
# A writer mock C++ style

def getAMatrix(MyRAWReader):
    rowsize = int(MyRAWReader.pop())
    colsize = int(MyRAWReader.pop())
    matrix = []
    for row in range(0, rowsize):
        rowlist = []
        for col in range(0, colsize):
            rowlist.append(float(MyRAWReader.pop()))
        matrix.append(rowlist)
    ANSER = np.array(tuple(matrix), dtype=float)
    return ANSER
# Get one cupy matrix by RAWReader

def writeAMatrix(Matrix, MyRAWWriter):
    rowsize = len(Matrix)
    colsize = len(Matrix[0])
    MyRAWWriter.append(rowsize)
    MyRAWWriter.append(colsize)
    MyRAWWriter.newline()
    for row in range(0, rowsize):
        rowlist = Matrix[row]
        for colelement in Matrix[row]:
            MyRAWWriter.append(colelement)
        MyRAWWriter.newline()
# Write one numpy matrix by RAWReader

def getValuefromConfigfile(Filename, ValueTitle):
    try:
        f = open(Filename, 'r')
        config = json.loads(f.read())
        f.close()
        # Load json file to config
        return config[ValueTitle]
    except:
        return None
# Get specify value from file

def setValuetoConfigfile(Filename, ValueTitle, Value):
    config = {}
    try:
        f = open(Filename, 'r')
        config = json.loads(f.read())
        f.close()
    except:
        pass
    # Load json file to config
    f = open(Filename, 'w')
    config[ValueTitle] = Value
    f.write(json.dumps(config, sort_keys=True, indent=4))
    f.close()
# Set specify value from file

def getDatas():
    try:
        rawreader = RAWReader()
        rawreader.open('in.mtrx')
        InputData = getAMatrix(rawreader)
        rawreader.open('out.mtrx')
        OutputData = getAMatrix(rawreader)
        rawreader.open('in_valid.mtrx')
        InputValidationData = getAMatrix(rawreader)
        rawreader.open('out_valid.mtrx')
        OutputValidationData = getAMatrix(rawreader)
        return [InputData, OutputData, InputValidationData, OutputValidationData]
    except:
        print('Warning: get data failed.')

def read_idx(filename):
    with open(filename, 'rb') as f:
        zero, data_type, dims = struct.unpack('>HBB', f.read(4))
        shape = tuple(struct.unpack('>I', f.read(4))[0] for d in range(dims))
        return np.fromstring(f.read(), dtype=np.uint8).reshape(shape)
# A function that can read MNIST's idx file format into numpy arrays

def idx2mtrx(FilenameIn, FilenameOut):
    print('processing...')
    rawwriter = RAWWriter()
    idx = read_idx(FilenameIn)
    OUT = np.array((idx[0].flatten(),))
    datalen = len(idx)
    count = 0
    print(str(len(idx))+' data finded')
    print('flatting...')
    print('------------------------------')
    for x in range(1, len(idx)):
        OUT = np.concatenate((OUT,  np.array((idx[x].flatten(),))), axis=0)
        count += 1
        if count >= datalen/30:
            count = 0
            print('*', end='')
    print('')
    print('saving...')
    writeAMatrix(OUT, rawwriter)
    rawwriter.write(FilenameOut+'.mtrx')
    print('saved to'+FilenameOut+'.mtrx')
