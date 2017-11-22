import random

datasize = int(input('Input size of data.\n'))
validationdatasize = int(input('Input size of Validation data.\n'))
datalist = []
validationdatalist = []
for x in range(0, datasize):
    randint = random.randint(0, 2**64-1)
    while randint in datalist:
        randint = random.randint(0, 2**64-1)
    datalist.append(randint)
for x in range(0, validationdatasize):
    randint = random.randint(0, 2**64-1)
    while (randint in datalist) or (randint in validationdatalist):
        randint = random.randint(0, 2**64-1)
    validationdatalist.append(randint)
# print(datalist)
# print(validationdatalist)
datamtrxstring = str(datasize)+' 64\n'
validationdatamtrxstring = str(validationdatasize)+' 64\n'
for x in range(0, datasize):
    string = ''
    for y in range(0, 64):
        string = string +' '+ str(bin(datalist[x]).lstrip('-0b').zfill(64))[y]
    datamtrxstring = datamtrxstring + string +'\n'

for x in range(0, validationdatasize):
    string = ''
    for y in range(0, 64):
        string = string +' '+ str(bin(validationdatalist[x]).lstrip('-0b').zfill(64))[y]
    validationdatamtrxstring = validationdatamtrxstring + string +'\n'

datamtrxstringout = str(datasize)+' 1\n'
validationdatamtrxstringout = str(validationdatasize)+' 1\n'
for x in range(0, datasize):
    string = ''
    if datalist[x]%3 == 0:
        string = '1'
    else:
        string = '-1'
    datamtrxstringout = datamtrxstringout + string +'\n'
for x in range(0, validationdatasize):
    string = ''
    if validationdatalist[x]%3 == 0:
        string = '1'
    else:
        string = '-1'
    validationdatamtrxstringout = validationdatamtrxstringout + string +'\n'
f = open('in.mtrx', 'w')
# print(datamtrxstring)
f.write(datamtrxstring)
f = open('in_valid.mtrx', 'w')
# print(validationdatamtrxstring)
f.write(validationdatamtrxstring)
f = open('out.mtrx', 'w')
# print(datamtrxstringout)
f.write(datamtrxstringout)
f = open('out_valid.mtrx', 'w')
# print(validationdatamtrxstringout)
f.write(validationdatamtrxstringout)
