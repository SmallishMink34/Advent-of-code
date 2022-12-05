move = open("Day 5\input.txt", "r")
crate = open("Day 5\input2.txt", "r")

Arrang = []
for i in range(9):
    Arrang.append([' '])
    Arrang[i] = [' ']* 8

liste_c = crate.readlines()
liste_m = move.readlines()

for i in range(len(liste_c)):
    for i2 in range(len(liste_c[i].split(','))):
        if liste_c[i].split(',')[i2].strip().replace('[','').replace(']','') != '':
            Arrang[i2][i] = liste_c[i].split(',')[i2].strip().replace('[','').replace(']','')

       
for i in Arrang:
    i.reverse()
    
for i in range(9):
    for i2 in range(7, 0, -1):
        if Arrang[i][i2] == ' ':
            del Arrang[i][i2]

def printl(l):
    for i in l:
        print(i)

def move(frome, to, count):
    value = len(Arrang[frome-1])-count
    temp = Arrang[frome-1][value:len(Arrang[frome-1])]
    del Arrang[frome-1][value:len(Arrang[frome-1])]
    for i in temp:
        Arrang[to-1].append(i)
        
count = 0
for i in liste_m:
    count += 1
    move(int(i.split(' ')[3]), int(i.split(' ')[5]), int(i.split(' ')[1]))

for i in Arrang:
    print(i[-1], end='')