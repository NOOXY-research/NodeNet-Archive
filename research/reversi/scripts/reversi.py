table = {'A': 'O', 'B': '@', 'N': ' '}
Input = []
Output = []

class ReversiUtility(object):
    def printKey(key):
        sublocation = 0
        for location in key:
            print(table[location]+' ', end='')
            if sublocation == 7:
                print('')
                sublocation = 0
            else:
                sublocation += 1

    def getPointbyKey(key):
        userpoint = 0
        compoint = 0
        for location in key:
            if location == 'A':
                userpoint += 1
            elif location == 'B':
                compoint += 1
            else:
                pass
        return userpoint, compoint

    def appendData(In, Out):
        Input.append(In)
        Output.append(Out)

    def dumpDatatomtrx(Filename):
        length = len(Input)
        Inputstring = str(length)+' 64\n'
        Outputstring = str(length)+' 64\n'
        for x in Input:
            for y in x:
                if y == 'A':
                    Inputstring += ' '
                elif y == 'B':
                    Inputstring += ' '
                else:
        # Input first
    def turnKey90degree(key):
        pass

    def mirrorKeyXaxis(Key):
        pass

    def mirrorKeyYaxis(Key):
        pass
    def reverseKey(Key):
        pass
x = ReversiUtility.getPointbyKey('BBBBBBBBBNABBBBBBBAAABBBBABAAABBBAABAAABBABABAABBAABAAABBABBBBBB')
print(x)
