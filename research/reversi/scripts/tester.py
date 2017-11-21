from reversi.reversi import *
myreversirecord = ReversiRecord()
myreversidropsrecord = ReversiDropsRecord()
while(1):
    filename = input('Input your UUID.\n>>>')
    myreversirecord.loadfromFile(filename)
    myreversirecord.printRecord()
    myreversidropsrecord.swallowbyReversiRecord(myreversirecord)
    myreversidropsrecord.extractDropRecord()
    myreversidropsrecord.printReversiDropsRecord()
    myreversidropsrecord.dumptomtrx()
