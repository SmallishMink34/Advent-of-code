liste = open('Day 3/input.txt', 'r')

input = liste.readlines()

all_letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dico ={}

for i in range(len(all_letter)):
    dico[all_letter[i]] = i+1

Save_letter = []
last_i  = i
print(len(input))
for i in input:

    for i2 in range(len(i)//2):
        for i3 in range(len(i)//2, len(i)):
            if i[i2] == i[i3] and last_i != i:
                Save_letter.append(i[i2])
                last_i = i
                
compteur = 0
for i in Save_letter:
    compteur += dico[i]
print(compteur)
        