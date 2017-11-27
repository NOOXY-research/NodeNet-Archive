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
myreversidropsrecord = ReversiDropsRecord()
print('loading files...')
for x in range(number):
    print('loading files('+str(x)+'/'+str(number)+')...')
    filename = files[x]
    myreversirecord.loadfromFile(filename)
    myreversidropsrecord.swallowbyReversiRecord(myreversirecord)
print('extrating...')
myreversidropsrecord.extractDropRecord()
print('saving...')
myreversidropsrecord.dumptomtrx1()
