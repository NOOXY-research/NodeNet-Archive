import reversi.IO as io
import numpy as np
from collections import deque
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
    def reverseMapping(Mapping):
        newmapping = []
        for x in Mapping:
            newmapping.append(x*-1)
        return newmapping

    def rotateMapping90degree(Mapping):
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

    def rotateDropPoint90degree(DropPoint):
        newdrop = ()
        newdrop += (DropPoint[1],)
        newdrop += ((7-DropPoint[0]),)
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

    def modifyDropPoints(function, droppointlist):
        newlist = []
        for droppoint in droppointlist:
            newlist.append(function(droppoint))
        return newlist

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
        self.MappingList = []
        self.TurnList = []
        self.DropPointList = []
        self.Winner = 0
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

class ReversiValueRecord(object):
    # Default perspective is 1
    def __init__(self):
        self.WinMappings = []
        self.LoseMappings = []
        self.WinMappingsCounts = []
        self.LoseMappingsCounts = []

    def extractDropRecord(self):
        WinMappingsDelta   =  self.WinMappings.copy()
        LoseMappingsDelta  =  self.LoseMappings.copy()
        WinMappingsCountsDelta   =  self.WinMappingsCounts.copy()
        LoseMappingsCountsDelta  =  self.LoseMappingsCounts.copy()

        for x in range(len(WinMappingsDelta)):
            mappingcache = ReversiUtility.rotateMapping90degree(WinMappingsDelta[x])
            self.addMap(True, mappingcache, WinMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(True, mappingcache, WinMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(True, mappingcache, WinMappingsCountsDelta[x])

        for x in range(len(LoseMappingsDelta)):
            mappingcache = ReversiUtility.rotateMapping90degree(LoseMappingsDelta[x])
            self.addMap(False, mappingcache, LoseMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(False, mappingcache, LoseMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(False, mappingcache, LoseMappingsCountsDelta[x])

        # Rotate
        for x in range(len(WinMappingsDelta)):
            mappingcache = ReversiUtility.mirrorMappingXaxis(WinMappingsDelta[x])
            self.addMap(True, mappingcache, WinMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(True, mappingcache, WinMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(True, mappingcache, WinMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(True, mappingcache, WinMappingsCountsDelta[x])

        for x in range(len(LoseMappingsDelta)):
            mappingcache = ReversiUtility.mirrorMappingXaxis(LoseMappingsDelta[x])
            self.addMap(False, mappingcache, LoseMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(False, mappingcache, LoseMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(False, mappingcache, LoseMappingsCountsDelta[x])
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            self.addMap(False, mappingcache, LoseMappingsCountsDelta[x])
        # Mirror X + Rotate
        # Mirror Y + Rotate same as x no need

    def addMap(self, Win, Mapping, Count):
        if Win:
            if Mapping not in self.WinMappings:
                self.WinMappings.append(Mapping)
                self.WinMappingsCounts.append(0)
            self.WinMappingsCounts[self.WinMappings.index(Mapping)] += Count
        else:
            if Mapping not in self.LoseMappings:
                self.LoseMappings.append(Mapping)
                self.LoseMappingsCounts.append(0)
            self.LoseMappingsCounts[self.LoseMappings.index(Mapping)] += Count

    def swallowbyReversiRecord(self, MyReversiRecord):
        for x in range(len(MyReversiRecord.TurnList)-1):
            if MyReversiRecord.TurnList[x] == -1:
                maptranslation = ReversiUtility.reverseMapping(MyReversiRecord.MappingList[x+1])
            else:
                maptranslation = MyReversiRecord.MappingList[x+1]
            if MyReversiRecord.TurnList[x] == MyReversiRecord.Winner:
                self.addMap(True, maptranslation, 1)
            else:
                self.addMap(False, maptranslation, 1)

    def dumptomtrx(self):
        finalinputmapping = deque([])
        finaloutputvalues = deque([])
        print('rendering data...')
        for x in range(len(self.WinMappings)):
            if self.WinMappings[x] not in finalinputmapping:
                finalinputmapping.append(self.WinMappings[x])
                finaloutputvalues.append([self.WinMappingsCounts[x]])

        for x in range(len(self.LoseMappings)):
            if self.LoseMappings[x] not in finalinputmapping:
                finalinputmapping.append(self.LoseMappings[x])
                finaloutputvalues.append([0])
        for x in range(len(finalinputmapping)):
            location = (finaloutputvalues[x])[0]
            base = None
            if finalinputmapping[x] in self.LoseMappings:
                base = (location+self.LoseMappingsCounts[self.LoseMappings.index(finalinputmapping[x])])
            else:
                base = location
            (finaloutputvalues[x])[0] = location / base
            # print(location)
            # input()

        # Finish input
        print('saving data...')
        InputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(finalinputmapping)), InputData)
        InputData.write('in_value.mtrx')
        OutputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(finaloutputvalues)), OutputData)
        OutputData.write('out_value.mtrx')
    # Value
class ReversiPolicyDropsRecord(object):
    # Default perspective is 1
    def __init__(self):
        self.WinDrops = []
        self.LoseDrops = []
        self.WinMappings = []
        self.LoseMappings = []
    def printReversiDropsRecord(self):
        print('win drop:')
        for x in range(len(self.WinDrops)):
            print(str(self.WinMappings[x])+' '+str(self.WinDrops[x]))
        print('lose drop:')
        for x in range(len(self.LoseDrops)):
            print(str(self.LoseMappings[x])+' '+str(self.LoseDrops[x]))

    def extractDropRecord(self):
        WinDropsDelta  =  self.WinDrops.copy()
        LoseDropsDelta =  self.LoseDrops.copy()
        WinMappingsDelta   =  self.WinMappings.copy()
        LoseMappingsDelta  =  self.LoseMappings.copy()

        for x in range(len(WinDropsDelta)):
            mappingcache = ReversiUtility.rotateMapping90degree(WinMappingsDelta[x])
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, WinDropsDelta[x])
            self.addDrop(True, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(True, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(True, mappingcache, droppointcache)

        for x in range(len(LoseDropsDelta)):
            mappingcache = ReversiUtility.rotateMapping90degree(LoseMappingsDelta[x])
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, LoseDropsDelta[x])
            self.addDrop(False, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(False, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(False, mappingcache, droppointcache)

        # Rotate
        for x in range(len(WinDropsDelta)):
            mappingcache = ReversiUtility.mirrorMappingXaxis(WinMappingsDelta[x])
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.mirrorDropPointXaxis, WinDropsDelta[x])
            self.addDrop(True, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(True, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(True, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(True, mappingcache, droppointcache)

        for x in range(len(LoseDropsDelta)):
            mappingcache = ReversiUtility.mirrorMappingXaxis(LoseMappingsDelta[x])
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.mirrorDropPointXaxis, LoseDropsDelta[x])
            self.addDrop(False, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(False, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(False, mappingcache, droppointcache)
            mappingcache = ReversiUtility.rotateMapping90degree(mappingcache)
            droppointcache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointcache)
            self.addDrop(False, mappingcache, droppointcache)
        # Mirror X + Rotate

        # Mirror Y + Rotate same as x no need

    def addDrop(self, Win, Mapping, Drops):
        if Win:
            if Mapping not in self.WinMappings:
                self.WinMappings.append(Mapping)
                self.WinDrops.append([])
            self.WinDrops[self.WinMappings.index(Mapping)] = self.WinDrops[self.WinMappings.index(Mapping)] + Drops
        else:
            if Mapping not in self.LoseMappings:
                self.LoseMappings.append(Mapping)
                self.LoseDrops.append([])
            self.LoseDrops[self.LoseMappings.index(Mapping)] = self.LoseDrops[self.LoseMappings.index(Mapping)] + Drops

    def swallowbyReversiRecord(self, MyReversiRecord):
        for x in range(len(MyReversiRecord.TurnList)-1):
            if MyReversiRecord.TurnList[x] == -1:
                maptranslation = ReversiUtility.reverseMapping(MyReversiRecord.MappingList[x])
            else:
                maptranslation = MyReversiRecord.MappingList[x]
            if MyReversiRecord.TurnList[x] == MyReversiRecord.Winner:
                self.addDrop(True, maptranslation, [MyReversiRecord.DropPointList[x],])
            else:
                self.addDrop(False, maptranslation, [MyReversiRecord.DropPointList[x],])

    def dumptomtrx(self):
        finalinputmapping = deque([])
        finaloutputmappingnp = deque([])
        MappingsIndex = deque([])
        print('rendering input data...')
        for x in range(len(self.WinMappings)):
            if self.WinMappings[x] not in finalinputmapping:
                finalinputmapping.append(self.WinMappings[x])
                MappingsIndex.append([x, -1])
        for x in range(len(self.LoseMappings)):
            if self.LoseMappings[x] not in finalinputmapping:
                finalinputmapping.append(self.LoseMappings[x])
                MappingsIndex.append([-1, x])
            else:
                (MappingsIndex[finalinputmapping.index(self.LoseMappings[x])])[1] = x
        # Finish input
        for x in range(len(finalinputmapping)):
            finaloutputmappingnp.append(np.zeros(64))
        # Initialize output
        print('rendering win data...')
        for x in range(len(self.WinMappings)):
            addmap = np.zeros(64)
            for y in self.WinDrops[x]:
                addmap[y[0]*8+y[1]] += 1
            finaloutputmappingnp[finalinputmapping.index(self.WinMappings[x])] += addmap
        # Win output render
        print('rendering lose data...')
        # for x in range(len(self.LoseMappings)):
        #     addmap = np.zeros(64)
        #     for y in self.LoseDrops[x]:
        #         addmap[y[0]*8+y[1]] += -1
        #     finaloutputmappingnp[finalinputmapping.index(self.LoseMappings[x])] += addmap
        # Lose output render
        print('finalizing data...')

        for x in range(len(finaloutputmappingnp)):
            count = 0
            devidemap = np.zeros(64)
            if (MappingsIndex[x])[0] != -1:
                for y in self.WinDrops[(MappingsIndex[x])[0]]:
                    devidemap[y[0]*8+y[1]] += 1
            if (MappingsIndex[x])[1] != -1:
                for y in self.LoseDrops[(MappingsIndex[x])[1]]:
                    devidemap[y[0]*8+y[1]] += 1

            finaloutputmappingnp[x] = (finaloutputmappingnp[x]/devidemap)*5
            where_are_NaNs = np.isnan(finaloutputmappingnp[x])
            (finaloutputmappingnp[x])[where_are_NaNs] = 0
        # Finalize render with normalization
        finaloutputmapping = []
        for x in finaloutputmappingnp:
            finaloutputmapping.append(x.tolist())
        print('saving data...')
        InputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(finalinputmapping)), InputData)
        InputData.write('in_policy.mtrx')
        OutputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(finaloutputmapping)), OutputData)
        OutputData.write('out_policy.mtrx')
    # Classify
