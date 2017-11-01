table = {'A': 'O', 'B': '@', 'N': ' '}
class ReversiUtility(object):
    def printkey(key):
        sublocation = 0
        for location in key:
            print(table[location]+' ', end='')
            if sublocation == 7:
                print('')
                sublocation = 0
            else:
                sublocation += 1
ReversiUtility.printkey('NNNNNNNNNNNNNNNNNNNNNNNNNNNABNNNNNAAANNNNNNNNNNNNNNNNNNNNNNNNNNN')
