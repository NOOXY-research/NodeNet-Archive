table = {'A': 'O', 'B': '@', 'N': ' ', 1: 'O', -1: '@', 0: ' '}

class ReversiUtility(object):
    def printKey(Key):
        sublocation = 0
        for location in Key:
            print(table[location]+' ', end='')
            if sublocation == 7:
                print('')
                sublocation = 0
            else:
                sublocation += 1

    def printMapping(Mapping):
        print('')
        sublocation = 0
        print('|----------------|\n|', end = '')
        for location in Mapping:
            print(table[location]+' ', end='')
            if sublocation == 7:
                print('|\n|', end = '')
                sublocation = 0
            else:
                sublocation += 1
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

    def reverseMapping(Mapping):
        newmapping = []
        for location in Mapping:
            newmapping.append(location*-1)
        return newmapping

class ReversiRecord(object):
    def __init__(self):
        self.MappingList = []
        self.TurnList = []
        self.Winner = 0
    def printRecord(self):
        for x in range(len(self.MappingList)):
            print('It\'s '+table[self.TurnList[x]]+'\'s turn. In this mapping.')
            ReversiUtility.printMapping(self.MappingList[x])
        print('Winer is '+table[self.Winner])
    def loadfromFile(self, Filename):
        f = open(Filename, 'r')
        rawstring = f.read()
        f.close()
        for location in rawstring.split():
            if ('A' in location) or ('B' in location) or ('N' in location):
                self.MappingList.append(ReversiUtility.convertKeytoMapping(location))
        for location in rawstring.split():
            if ('user' in location) :
                self.TurnList.append(1)
            elif  ('com' in location):
                self.TurnList.append(-1)
        if 'win' in rawstring:
            self.Winner = -1
        elif 'lose' in rawstring:
            self.Winner = 1
        else:
            self.Winner = 0
