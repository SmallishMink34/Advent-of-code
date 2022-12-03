liste = open('Day 3/input.txt', 'r')

input = liste.readlines()

all_letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dico ={}

for i in range(len(all_letter)):
    dico[all_letter[i]] = i+1

Save_letter = []
last_i  = i
print(len(input))
for i in range(0, len(input), 3):
    for i1 in range(len(input[i+0])):
        for i2 in range(len(input[i+1])):
            for i3 in range(len(input[i+2])):
                if input[i+0][i1] == input[i+1][i2] == input[i+2][i3] and last_i != input[i+0]:
                    Save_letter.append(input[i+0][i1])
                    last_i = input[i+0]
                    print(i)
compteur = 0
for i in Save_letter:
    compteur += dico[i]
print(compteur)
        