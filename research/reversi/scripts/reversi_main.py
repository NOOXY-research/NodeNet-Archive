from reversi import *

# mymapping = ReversiUtility.convertKeytoMapping('BBBBBBBBBNABBBBBBBAAABBBBABAAABBBAABAAABBABABAABBAABAAABBABBBBBB')
# ReversiUtility.printMapping(mymapping)
# mymapping2 = ReversiUtility.turnMapping90degree(mymapping)
# ReversiUtility.printMapping(mymapping2)
# mymapping3 = ReversiUtility.reverseMapping(mymapping)
# ReversiUtility.printMapping(mymapping3)
# mymapping4 = ReversiUtility.mirrorMappingXaxis(mymapping)
# ReversiUtility.printMapping(mymapping4)
# mymapping5 = ReversiUtility.mirrorMappingYaxis(mymapping)
# ReversiUtility.printMapping(mymapping5)
# mymapping6 = ReversiUtility.mirrorMappingXaxis(mymapping5)
# ReversiUtility.printMapping(mymapping6)

myreversirecord = ReversiRecord()
myreversirecord.loadfromFile('3a80ccee-b87d-cb80-cef0-31ad07408d1a')
myreversirecord.printRecord()
