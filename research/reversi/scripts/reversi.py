table = {'A': 'O', 'B': '@', 'N': ' ', 1: 'O', -1: '@', 0: ' '}

class ReversiUtility(object):
    def printKey(Key):
        col = 0
        for location in Key:
            print(table[location]+' ', end='')
            if col == 7:
                print('')
                col = 0
            else:
                col += 1

    def printMapping(Mapping):
        print('')
        col = 0
        row = 0
        print('  0 1 2 3 4 5 6 7')
        print(' |----------------|\n0|', end = '')
        for location in Mapping:
            print(table[location]+' ', end='')
            if col == 7:
                if row < 7:
                    print('|\n'+str(row+1)+'|', end = '')
                else:
                    print('|\n |',end='')
                row += 1
                col = 0
            else:
                col += 1
        print('----------------|')
        print('')

    def printMappingwithDropPoint(Mapping, DropPoint):
        print('')
        col = 0
        row = 0
        print('  0 1 2 3 4 5 6 7 Y')
        print(' |----------------|\n0|', end = '')
        for location in Mapping:
            if DropPoint[0] == row and DropPoint[1] == col:
                print('X ', end='')
            else:
                print(table[location]+' ', end='')
            if col == 7:
                if row < 7:
                    print('|\n'+str(row+1)+'|', end = '')
                else:
                    print('|\nX|',end='')
                row += 1
                col = 0
            else:
                col += 1
        print('----------------|')
        print('')

    def getPointbyKey(Key):
        userpoint = 0
        compoint = 0
        for location in Key:
            if location == 'A':
                userpoint += 1
            elif location == 'B':
                compoint += 1
            else:
                pass
        return userpoint, compoint

    def getPointbyMapping(Key):
        userpoint = 0
        compoint = 0
        for location in Key:
            if location == 'A':
                userpoint += 1
            elif location == 'B':
                compoint += 1
            else:
                pass
        return userpoint, compoint

    def convertKeytoMapping(Key):
        mapping = []
        for location in Key:
            if location == 'A':
                mapping.append(1)
            elif location == 'B':
                mapping.append(-1)
            else:
                mapping.append(0)
        return mapping

    def appendData(In, Out):
        Input.append(In)
        Output.append(Out)

    # def dumpMappingtomtrx(Filename):
    #     length = len(Input)
    #     Inputstring = str(length)+' 64\n'
    #     Outputstring = str(length)+' 64\n'
    #     for x in Input:
    #         for y in x:
    #             if y == 1:
    #                 Inputstring += ' '
    #             elif y == -1:
    #                 Inputstring += ' '
    #             else:
    #                 pass
        # Input first
    def turnMapping90degree(Mapping):
        newmapping = []
        for col in range(8):
            for row in range(8):
                newmapping.append(Mapping[(7-row)*8+col])
        return newmapping

    def mirrorMappingXaxis(Mapping):
        newmapping = []
        for row in range(8):
            for col in range(8):
                newmapping.append(Mapping[(7-row)*8+col])
        return newmapping

    def mirrorMappingYaxis(Mapping):
        newmapping = []
        for row in range(8):
            for col in range(8):
                newmapping.append(Mapping[row*8+(7-col)])
        return newmapping

    def turnDropPoint90degree(DropPoint):
        newdrop = ()
        newdrop += (DropPoint[1],)
        newdrop += (DropPoint[0],)
        return newdrop

    def mirrorDropPointXaxis(DropPoint):
        newdrop = ()
        newdrop += (7-DropPoint[0],)
        newdrop += (DropPoint[1],)
        return newdrop

    def mirrorDropPointYaxis(DropPoint):
        newdrop = ()
        newdrop += (DropPoint[0],)
        newdrop += (7-DropPoint[1],)
        return newdrop

class ReversiRecord(object):
    def __init__(self):
        self.MappingList = []
        self.TurnList = []
        self.DropPointList = []
        self.Winner = 0
    def printRecord(self):
        for x in range(len(self.MappingList)):
            print('It\'s '+table[self.TurnList[x]]+'\'s turn. In this mapping. It drop '+str(self.DropPointList[x]))
            ReversiUtility.printMappingwithDropPoint(self.MappingList[x], self.DropPointList[x])
        print('Winer is '+table[self.Winner])
    def loadfromFile(self, Filename):
        f = open(Filename, 'r')
        rawstring = f.read()
        f.close()
        for location in rawstring.split():
            if ('A' in location) or ('B' in location) or ('N' in location):
                self.MappingList.append(ReversiUtility.convertKeytoMapping(location))
        for location in range(len(rawstring.split())):
            if ('user' in rawstring.split()[location]) :
                self.TurnList.append(1)
                self.DropPointList.append((int(rawstring.split()[location+1]), int(rawstring.split()[location+2])))
            elif  ('com' in rawstring.split()[location]):
                self.TurnList.append(-1)
                self.DropPointList.append((int(rawstring.split()[location+1]), int(rawstring.split()[location+2])))
        if 'win' in rawstring:
            self.Winner = -1
        elif 'lose' in rawstring:
            self.Winner = 1
        else:
            self.Winner = 0

class ReversiDropsRecord(object):
    def __init__(self):
        self.DropsRecordDict = {}
    def appendDropRecord(self, Mapping, DropPoint):
        self.DropsRecordDict.update({Mapping, self.DropsRecordDict[Mapping]+[DropPoint,]})
    def extractDropRecord(self):
        pass
    def swallowWinnerbyReversiRecord(self):
        pass
    def dumptomtrx(self):
        pass
# Every record format [] : [(),(),()]
#              mapping^    ^list of drop points
