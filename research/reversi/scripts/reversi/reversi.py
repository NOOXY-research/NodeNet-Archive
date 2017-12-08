import reversi.IO as io
import numpy as np
import copy

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

    def printBoard(Board):
        print('')
        col = 0
        row = 0
        print('  0 1 2 3 4 5 6 7')
        print(' |----------------|\n0|', end = '')
        for location in Board:
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

    def printBoardwithDropPoint(Board, DropPoint):
        print('')
        col = 0
        row = 0
        print('  0 1 2 3 4 5 6 7 Y')
        print(' |----------------|\n0|', end = '')
        for location in Board:
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

    def getPointbyBoard(Key):
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

    def convertKeytoBoard(Key):
        board = []
        for location in Key:
            if location == 'A':
                board.append(1)
            elif location == 'B':
                board.append(-1)
            else:
                board.append(0)
        return board

    def reverseBoard(Board):
        newboard = []
        for x in Board:
            newboard.append(x*-1)
        return newboard

    def rotateBoard90degree(Board):
        newboard = []
        for col in range(8):
            for row in range(8):
                newboard.append(Board[(7-row)*8+col])
        return newboard

    def mirrorBoardXaxis(Board):
        newboard = []
        for row in range(8):
            for col in range(8):
                newboard.append(Board[(7-row)*8+col])
        return newboard

    def mirrorBoardYaxis(Board):
        newboard = []
        for row in range(8):
            for col in range(8):
                newboard.append(Board[row*8+(7-col)])
        return newboard

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

    def modifyDropPoints(Function, DropPointList):
        newlist = []
        for droppoint in DropPointList:
            newlist.append(Function(droppoint))
        return newlist

class ReversiRecord(object):

    def __init__(self):
        self.BoardList = []
        self.TurnList = []
        self.DropPointList = []
        self.Winner = 0

    def printRecord(self):
        for x in range(len(self.BoardList)):
            print('It\'s '+table[self.TurnList[x]]+'\'s turn. In this board. It drop '+str(self.DropPointList[x]))
            ReversiUtility.printBoardwithDropPoint(self.BoardList[x], self.DropPointList[x])
        print('Winer is '+table[self.Winner])

    def loadfromFile(self, Filename):
        self.BoardList = []
        self.TurnList = []
        self.DropPointList = []
        self.Winner = 0
        f = open(Filename, 'r')
        rawstring = f.read()
        f.close()
        for location in rawstring.split():
            if ('A' in location) or ('B' in location) or ('N' in location):
                self.BoardList.append(ReversiUtility.convertKeytoBoard(location))
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

class ReversiBoardsContainer(object):

    def __init__(self):
        self.Boards = []
        self.Contains = []

    def __str__(self):
        string = ''
        for x in range(len(self.Boards)):
            string += str(self.Boards[x])+' '+str(self.Contains[x])+'\n'
        return string

    def getIndex(self, Board):
        return self.getIndex_handler(Board, 0, len(self.Boards)-1)

    def getIndex_handler(self, Board, Start, End):
        if len(self.Boards)==0:
            return None
        middle = int((Start+End)/2)
        order = self.compare(Board, self.Boards[middle])
        if order == 0:
            return middle
        elif order == -1:
            if Start-End == 0:
                return None
            return self.getIndex_handler(Board, Start, middle)
        else:
            if Start-End == 0:
                return None
            return self.getIndex_handler(Board, middle+1, End)

    def getInsertIndex(self, Board):
        return self.getInsertIndex_handler(Board, 0, len(self.Boards)-1)

    def getInsertIndex_handler(self, Board, Start, End):
        if(len(self.Boards)==0):
            return 0
        middle = int((Start+End)/2)
        order = self.compare(Board, self.Boards[middle])
        if order == 0:
            return None
        elif order == -1:
            if Start-End == 0:
                return middle
            return self.getInsertIndex_handler(Board, Start, middle)
        else:
            if Start-End == 0:
                return middle+1
            return self.getInsertIndex_handler(Board, middle+1, End)

    def compare(self, Board1, Board2):
        for x in range(len(Board1)):
            if Board1[x] > Board2[x]:
                return 1
            elif Board1[x] < Board2[x]:
                return -1
        return 0

    def setContainbyBoard(self, Board, Contain):
        if self.getIndex(Board) == None:
            Index = self.getInsertIndex(Board)
            self.Boards.insert(Index, Board)
            self.Contains.insert(Index, [])
        self.Contains[self.getIndex(Board)] = Contain

    def getBoardbyIndex(self, Index):
        return self.Boards[Index]

    def getContainbyBoard(self, Board):
        return self.Contains[self.getIndex(Board)]

    def getContainbyIndex(self, Index):
        return self.Contains[Index]

    def getContainslist(self):
        return self.Contains

    def getBoardslist(self):
        return self.Boards

    def setContainbyIndex(self, Index, Contain):
        self.Contains[Index] = Contain

class ReversiValueHandler(object):
    # Transfer all perspective to 1
    def __init__(self):
        self.Boards2Counts = ReversiBoardsContainer()

    def extractBoardCounts(self):
        boards2countsdelta = copy.deepcopy(self.Boards2Counts)
        boardsdelta = boards2countsdelta.getBoardslist()
        countsdelta = boards2countsdelta.getContainslist()
        lengthdelta = len(boardsdelta)
        print('data count initial')
        print(lengthdelta)
        for x in range(lengthdelta):
            # print(len(self.Boards2Counts.getBoardslist()))
            boardcountcache = countsdelta[x]
            boardcache = ReversiUtility.rotateBoard90degree(boardsdelta[x])
            self.addBoardCount(boardcache, boardcountcache)
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addBoardCount(boardcache, boardcountcache)
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addBoardCount(boardcache, boardcountcache)
        print('data count after rotate')
        print(len(self.Boards2Counts.getBoardslist()))
        # Rotate
        for x in range(lengthdelta):
            # print(len(self.Boards2Counts.getBoardslist()))
            boardcountcache = countsdelta[x]
            boardcache = ReversiUtility.mirrorBoardXaxis(boardsdelta[x])
            self.addBoardCount(boardcache, boardcountcache)
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addBoardCount(boardcache, boardcountcache)
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addBoardCount(boardcache, boardcountcache)
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addBoardCount(boardcache, boardcountcache)
        print('data count after mirror+rotate')
        print(len(self.Boards2Counts.getBoardslist()))
        # Mirror X + Rotate

    def addBoardCount(self, Board, BoardCount):
        if self.Boards2Counts.getIndex(Board) == None:
            self.Boards2Counts.setContainbyBoard(Board, [0, 0])
        Boards2CountsIndex = self.Boards2Counts.getIndex(Board)
        oldcount = self.Boards2Counts.getContainbyIndex(Boards2CountsIndex)
        newcount = [oldcount[0]+BoardCount[0], oldcount[1]+BoardCount[1]]
        self.Boards2Counts.setContainbyIndex(Boards2CountsIndex, newcount)

    def swallowReversiRecord(self, MyReversiRecord):
        winner = MyReversiRecord.Winner
        for x in range(len(MyReversiRecord.TurnList)-1):
            thisturn = MyReversiRecord.TurnList[x]
            thisboard = MyReversiRecord.BoardList[x+1]
            if thisturn == -1:
                thisboard = ReversiUtility.reverseBoard(thisboard)
            # print(str(winner)+' '+str(thisturn)+' '+str(thisboard))
            if thisturn == winner:
                self.addBoardCount(thisboard, [1, 0])
            else:
                self.addBoardCount(thisboard, [0, 1])

    def dumptomtrx(self):
        bias = 0.85
        amplifyfactor = 5
        inputdata = []
        outputdata = []
        for x in range(len(self.Boards2Counts.getBoardslist())):
            inputdata.append(self.Boards2Counts.getBoardbyIndex(x))
            count = self.Boards2Counts.getContainbyIndex(x)
            wincount = count[0]
            losecount = count[1]
            value = wincount-losecount/(wincount+losecount)
            if wincount+losecount == 1 and wincount == 1:
                value = bias
            elif wincount+losecount == 1 and losecount == 1:
                value = -bias
            outputdata.append([amplifyfactor*value])
        InputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(inputdata)), InputData)
        InputData.write('in_value.mtrx')
        OutputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(outputdata)), OutputData)
        OutputData.write('out_value.mtrx')

class ReversiPolicyHandler(object):
    # Transfer all perspective to 1
    def __init__(self):
        self.Board2Drops = ReversiBoardsContainer()

    def extractDropPoints(self):
        board2dropsdelta = copy.deepcopy(self.Board2Drops)
        boardsdelta = board2dropsdelta.getBoardslist()
        droppointslistdelta = board2dropsdelta.getContainslist()
        lengthdelta = len(boardsdelta)
        print('data count initial')
        print(lengthdelta)
        for x in range(lengthdelta):
            # print(len(self.Boards2Counts.getBoardslist()))
            windroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, (droppointslistdelta[x])[0])
            losedroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, (droppointslistdelta[x])[1])
            droppointscache = [windroppointscache, losedroppointscache]
            boardcache = ReversiUtility.rotateBoard90degree(boardsdelta[x])
            self.addDropPoints(boardcache, droppointscache)
            windroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[0])
            losedroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[1])
            droppointscache = [windroppointscache, losedroppointscache]
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addDropPoints(boardcache, droppointscache)
            windroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[0])
            losedroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[1])
            droppointscache = [windroppointscache, losedroppointscache]
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addDropPoints(boardcache, droppointscache)
        print('data count after rotate')
        print(len(self.Board2Drops.getBoardslist()))
        # Rotate
        for x in range(lengthdelta):
            # print(len(self.Boards2Counts.getBoardslist()))
            windroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.mirrorDropPointXaxis, (droppointslistdelta[x])[0])
            losedroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.mirrorDropPointXaxis, (droppointslistdelta[x])[1])
            droppointscache = [windroppointscache, losedroppointscache]
            boardcache = ReversiUtility.mirrorBoardXaxis(boardsdelta[x])
            self.addDropPoints(boardcache, droppointscache)
            windroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[0])
            losedroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[1])
            droppointscache = [windroppointscache, losedroppointscache]
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addDropPoints(boardcache, droppointscache)
            windroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[0])
            losedroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[1])
            droppointscache = [windroppointscache, losedroppointscache]
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addDropPoints(boardcache, droppointscache)
            windroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[0])
            losedroppointscache = ReversiUtility.modifyDropPoints(ReversiUtility.rotateDropPoint90degree, droppointscache[1])
            droppointscache = [windroppointscache, losedroppointscache]
            boardcache = ReversiUtility.rotateBoard90degree(boardcache)
            self.addDropPoints(boardcache, droppointscache)
        print('data count after mirror+rotate')
        print(len(self.Board2Drops.getBoardslist()))
        # Mirror X + Rotate

    def addDropPoints(self, Board, DropPoints):
        if self.Board2Drops.getIndex(Board) == None:
            self.Board2Drops.setContainbyBoard(Board, [[], []])
        Board2DropsIndex = self.Board2Drops.getIndex(Board)
        olddroppoints = self.Board2Drops.getContainbyIndex(Board2DropsIndex)
        newcount = [olddroppoints[0]+DropPoints[0], olddroppoints[1]+DropPoints[1]]
        self.Board2Drops.setContainbyIndex(Board2DropsIndex, newcount)

    def swallowReversiRecord(self, MyReversiRecord):
        winner = MyReversiRecord.Winner
        for x in range(len(MyReversiRecord.TurnList)-1):
            thisturn = MyReversiRecord.TurnList[x]
            thisboard = MyReversiRecord.BoardList[x]
            thisdroppoint = MyReversiRecord.DropPointList[x]
            if thisturn == -1:
                thisboard = ReversiUtility.reverseBoard(thisboard)
            # print(str(winner)+' '+str(thisturn)+' '+str(thisboard))
            if thisturn == winner:
                self.addDropPoints(thisboard, [[], [thisdroppoint]])
            else:
                self.addDropPoints(thisboard, [[thisdroppoint], []])

    def dumptomtrx(self):
        amplifyfactor = 5
        tilefactor = 0
        inputdata = []
        outputdata = []
        for x in range(len(self.Board2Drops.getBoardslist())):
            inputdata.append(self.Board2Drops.getBoardbyIndex(x))
            droppoints = self.Board2Drops.getContainbyIndex(x)
            windroppoints = droppoints[0]
            losedroppoints = droppoints[1]
            winboard = np.zeros(64)
            loseboard = np.zeros(64)
            for droppoint in windroppoints:
                winboard[droppoint[0]*8+droppoint[1]] += 1
            for droppoint in losedroppoints:
                loseboard[droppoint[0]*8+droppoint[1]] += 1
            finalboard = (winboard-loseboard/(winboard+loseboard))*amplifyfactor
            where_are_NaNs = np.isnan(finalboard)
            (finalboard)[where_are_NaNs] = tilefactor
            outputdata.append(finalboard.tolist())

        InputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(inputdata)), InputData)
        InputData.write('in_policy.mtrx')
        OutputData = io.RAWWriter()
        io.writeAMatrix(np.array(tuple(outputdata)), OutputData)
        OutputData.write('out_policy.mtrx')
