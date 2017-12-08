import random
import numpy as np

datasize = int(input('Input size of data.\n'))
validationdatasize = int(input('Input size of Validation data.\n'))
datalist = []
validationdatalist = []
for x in range(0, datasize):
    randint = random.randint(-50000, 50000)
    while randint in datalist:
        randint = random.randint(-50000, 50000)
    datalist.append((randint/50000)*np.pi*2)
for x in range(0, validationdatasize):
    randint = random.randint(-50000, 50000)
    while (randint in datalist) or (randint in validationdatalist):
        randint = random.randint(-50000, 50000)
    validationdatalist.append((randint/50000)*np.pi*2)
# print(datalist)
# print(validationdatalist)
datamtrxstring = str(datasize)+' 1\n'
validationdatamtrxstring = str(validationdatasize)+' 1\n'
for x in range(0, datasize):
    datamtrxstring = datamtrxstring +str(datalist[x])+'\n'

for x in range(0, validationdatasize):
    validationdatamtrxstring = validationdatamtrxstring + str(validationdatalist[x]) +'\n'

datamtrxstringout = str(datasize)+' 1\n'
validationdatamtrxstringout = str(validationdatasize)+' 1\n'
for x in range(0, datasize):
    datamtrxstringout = datamtrxstringout + str(np.sin(datalist[x])) +'\n'
for x in range(0, validationdatasize):
    validationdatamtrxstringout = validationdatamtrxstringout + str(np.sin(validationdatalist[x])) +'\n'
f = open('in.mtrx', 'w')
print(datamtrxstring)
f.write(datamtrxstring)
f = open('in_valid.mtrx', 'w')
print(validationdatamtrxstring)
f.write(validationdatamtrxstring)
f = open('out.mtrx', 'w')
print(datamtrxstringout)
f.write(datamtrxstringout)
f = open('out_valid.mtrx', 'w')
print(validationdatamtrxstringout)
f.write(validationdatamtrxstringout)
