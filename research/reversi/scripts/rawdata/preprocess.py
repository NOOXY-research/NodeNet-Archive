import os
from os import path
class process():
    def __init__(self):
        self.MappingList = []
        self.TurnList = []
        self.DropPointList = []
        self.Winner = 0

    def swallow(self, Filename):
        self.MappingList = []
        self.TurnList = []
        self.DropPointList = []
        self.Winner = 0
        f = open(Filename, 'r')
        rawstring = f.read()
        f.close()
        for location in range(len(rawstring.split())):
            if '-1' not in rawstring.split()[location-1] and (('A' in rawstring.split()[location]) or ('B' in rawstring.split()[location]) or ('N' in rawstring.split()[location])):
                if rawstring.split()[location+4] !=  rawstring.split()[location]:
                    if ('A' in rawstring.split()[location+4]) or ('B' in rawstring.split()[location+4]) or ('N' in rawstring.split()[location+4]):
                        self.MappingList.append(rawstring.split()[location])
                        if rawstring.split()[location+4] not in self.MappingList:
                            if rawstring.split()[location+4].count('A')-rawstring.split()[location].count('A')>0:
                                self.DropPointList.append((int(rawstring.split()[location-2]), int(rawstring.split()[location-1])))
                                self.TurnList.append(1)
                            else:
                                self.DropPointList.append((int(rawstring.split()[location-2]), int(rawstring.split()[location-1])))
                                self.TurnList.append(-1)
                    # else:
                    #     self.MappingList.append(rawstring.split()[location])
                    #     if ('N' in rawstring.split()[location]):
                    #         self.DropPointList.append((int(rawstring.split()[location-2]), int(rawstring.split()[location-1])))
                    #         self.TurnList.append(-1)
                    #     else:
                    #         self.DropPointList.append((int(rawstring.split()[location-2]), int(rawstring.split()[location-1])))
                    #         self.TurnList.append(1)

        if 'win' in rawstring:
            self.Winner = -1
        elif 'lose' in rawstring:
            self.Winner = 1
        else:
            self.Winner = 0
    def savetofile(self, Filename):
        rawstring = ""
        for x in range(len(self.MappingList)):
            if self.TurnList[x] == 1:
                rawstring += "user "+str((self.DropPointList[x])[0])+" "+str((self.DropPointList[x])[1])+" "+self.MappingList[x]+"\n"
            else:
                rawstring += "com "+str((self.DropPointList[x])[0])+" "+str((self.DropPointList[x])[1])+" "+self.MappingList[x]+"\n"
        if self.Winner == -1:
            rawstring+= "win"
        else:
            rawstring+= "lose"
        f = open('data/'+Filename, 'w')
        f.write(rawstring)
        f.close();

files = [f for f in os.listdir('./') if (path.isfile(f) and ('.' not in f))]
for f in files:
    print(f)
number = int(input('Input number of file..\n>>>'))
if number ==-1:
    number = len(files)
for x in range(number):
    p = process()
    print('loading "'+files[x]+'" files('+str(x+1)+'/'+str(number)+')...')
    filename = files[x]
    p.swallow(filename)
    p.savetofile('record'+str(x)+'_'+filename[0]+filename[1]+filename[2]+filename[3]+filename[4])
