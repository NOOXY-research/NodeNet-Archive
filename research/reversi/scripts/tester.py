from reversi.reversi import *
myreversirecord = ReversiRecord()
myreversidropsrecord = ReversiDropsRecord()
while(1):
    filename = input('Input your UUID.\n>>>')
    if filename == '':
        break
    myreversirecord.loadfromFile(filename)
    myreversidropsrecord.swallowbyReversiRecord(myreversirecord)

myreversidropsrecord.extractDropRecord()
myreversidropsrecord.printReversiDropsRecord()
myreversidropsrecord.dumptomtrx()
