f = open("befommat.csv", "r")
S = f.read()
S = S.replace("\n", " ")
S = S.replace(",", " ")
counterin = 0
counterout = 0
fin = open("in_fommator.mtrx", "w")
fout = open("out_fommator.mtrx", "w")
sout = ""
sin = ""
for value in S.split(" "):
  counterin += 1
  if counterin % 9 != 0:
    sin = sin + " " + value
  else:
    sin = sin + "\n"

for value in S.split(" "):
  counterout += 1
  if counterout % 9 != 0:
    pass
  else:
    sout = sout + value + "\n"

fin.write(str(int(counterin / 9)) + " 8\n" + sin)
fout.write(str(int(counterout / 9)) + " 1\n" + sout)
