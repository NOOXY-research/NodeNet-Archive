from reversi.reversi import *
import os
from os import path
files = [f for f in os.listdir('./') if (path.isfile(f) and ('.' not in f))]
for f in files:
    print(f)
number = int(input('Input number of file.\n>>>'))
if number ==-1:
    number = len(files)
myreversirecord = ReversiRecord()
myreversivaluerecord = ReversiValueRecord()
print('loading files...')
for x in range(number):
    print('loading files('+str(x)+'/'+str(number)+')...')
    filename = files[x]
    myreversirecord.loadfromFile(filename)
    myreversivaluerecord.swallowbyReversiRecord(myreversirecord)
print('extrating...')
myreversivaluerecord.extractDropRecord()
print('saving...')
myreversivaluerecord.dumptomtrx()
