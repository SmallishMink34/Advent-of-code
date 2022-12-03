liste = open('Day 2/File.txt', 'r')
# Sert a rien 
coups_1 = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
}
#POint des coups
coups_2 = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}
# partie 2 cas :
lose = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y',
}

draw = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z',
}

winning = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X',
}
# Point en fonction des cas
win = {
    'A X' : 0,
    'A Y' : 3,
    'A Z' : 6,
    'B X' : 0,
    'B Y' : 3,
    'B Z' : 6,
    'C X' : 0,
    'C Y' : 3,
    'C Z' : 6,
}

somme_point = 0
coups_2_p = 0 # Point gagnée avec le coups
for i in liste.readlines():
    if i.strip().split(" ")[1] == 'X':
        print(lose[i.strip().split(" ")[0]])
        coups_2_p = coups_2[lose[i.strip().split(" ")[0]]]
    if i.strip().split(" ")[1] == 'Y':
        coups_2_p = coups_2[draw[i.strip().split(" ")[0]]]
    if i.strip().split(" ")[1] == 'Z':
        coups_2_p = coups_2[winning[i.strip().split(" ")[0]]]
    somme_point += coups_2_p + win[i.strip()]

print(somme_point)
